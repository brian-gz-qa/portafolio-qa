# -*- coding: utf-8 -*-
"""Genera imagenes 1200x630 para publicaciones de LinkedIn sobre QA (HTML -> PNG via Edge)."""
import sys, os, random, datetime
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
from playwright.sync_api import sync_playwright

# ---- Config del tema ----
TITULOS = {
    "errores_casos": {
        "titulo": "5 errores al escribir\ncasos de prueba",
        "subtitulo": "(y cómo evitarlos)",
        "accent": "#0a66c2",
        "bg": "#0b1f3a",
        "tags": "QA • Manual Testing • Test Cases",
    },
    "api_basico": {
        "titulo": "Primeros pasos\nprobando APIs",
        "subtitulo": "Postman, métodos HTTP y status codes",
        "accent": "#ff6b35",
        "bg": "#1a0f2e",
        "tags": "QA • API Testing • Postman",
    },
    "bug_jira": {
        "titulo": "¿Cómo reportar\nun bug de verdad?",
        "subtitulo": "La plantilla que usan los buenos QAs",
        "accent": "#00b8a9",
        "bg": "#0f2b2b",
        "tags": "QA • Bug Report • Jira",
    },
    "equivalencia": {
        "titulo": "Clases de equivalencia:\nprueba menos, cubre más",
        "subtitulo": "Técnica #1 de diseño de casos de prueba",
        "accent": "#7c4dff",
        "bg": "#1c1333",
        "tags": "QA • Test Design • ISTQB",
    },
    "pregunta": {
        "titulo": "¿Sabías que...?\n",
        "subtitulo": "Dato curioso de QA para hoy",
        "accent": "#e63946",
        "bg": "#2b0f18",
        "tags": "QA • Curiosidades",
    },
}

def build_html(tema, texto_extra=""):
    t = TITULOS[tema]
    fecha = datetime.date.today().strftime("%d/%m/%Y")
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
    * {{ margin:0; padding:0; box-sizing:border-box; }}
    body {{ width:1200px; height:630px; font-family:'Segoe UI', Arial, sans-serif; overflow:hidden; }}
    .card {{ width:1200px; height:630px; background:linear-gradient(135deg, {t['bg']} 0%, #000 100%); color:#fff; display:flex; flex-direction:column; justify-content:space-between; padding:60px 70px; position:relative; }}
    .top {{ display:flex; justify-content:space-between; align-items:center; }}
    .brand {{ font-size:20px; font-weight:700; letter-spacing:1px; color:{t['accent']}; }}
    .date {{ font-size:16px; opacity:.7; }}
    h1 {{ font-size:58px; line-height:1.15; font-weight:800; margin:20px 0 10px 0; }}
    .sub {{ font-size:26px; opacity:.85; margin-bottom:25px; }}
    .accent-bar {{ width:90px; height:10px; background:{t['accent']}; border-radius:6px; margin-bottom:30px; }}
    .tags {{ font-size:18px; opacity:.6; letter-spacing:.5px; }}
    .extra {{ font-size:24px; margin-top:20px; background:rgba(255,255,255,.08); border-left:6px solid {t['accent']}; padding:16px 20px; border-radius:4px; }}
    .footer {{ display:flex; justify-content:space-between; align-items:center; }}
    .handle {{ font-size:18px; opacity:.8; }}
    </style></head><body>
    <div class="card">
      <div class="top"><div class="brand">BRIAN GONZÁLEZ · QA</div><div class="date">{fecha}</div></div>
      <div>
        <div class="accent-bar"></div>
        <h1>{t['titulo']}</h1>
        <div class="sub">{t['subtitulo']}</div>
        {f'<div class=\"extra\">{texto_extra}</div>' if texto_extra else ''}
      </div>
      <div class="footer">
        <div class="tags">{t['tags']}</div>
        <div class="handle">#QAEngineer #SoftwareTesting</div>
      </div>
    </div>
    </body></html>"""

def generar(tema, out_path, texto_extra=""):
    html = build_html(tema, texto_extra)
    tmp = os.path.abspath("tmp_contenido.html")
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(html)
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
        ctx = browser.contexts[0]
        page = ctx.new_page()
        page.set_viewport_size({"width": 1200, "height": 630})
        page.goto("file:///" + tmp, wait_until="load", timeout=30000)
        page.wait_for_timeout(1500)
        page.screenshot(path=out_path, clip={"x": 0, "y": 0, "width": 1200, "height": 630})
        page.close()
        browser.close()
    os.remove(tmp)
    print("[*] Imagen guardada:", out_path, os.path.getsize(out_path), "bytes")

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("tema", choices=list(TITULOS.keys()))
    ap.add_argument("-o", "--out", default="imagen_contenido.png")
    ap.add_argument("-e", "--extra", default="")
    a = ap.parse_args()
    generar(a.tema, a.out, a.extra)
