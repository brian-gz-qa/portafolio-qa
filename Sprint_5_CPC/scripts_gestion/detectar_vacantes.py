# -*- coding: utf-8 -*-
"""
DETECCIÓN AUTOMÁTICA DE VACANTES QA (para la rutina diaria)
-----------------------------------------------------------
Busca vacantes de QA junior/trainee en Colombia y remoto (LinkedIn Jobs),
las puntúa según la coincidencia con el perfil de Brian y genera un
reporte diario con las mejores opciones y enlaces.

Uso:  python detectar_vacantes.py          (usa el navegador de la rutina)
      python detectar_vacantes.py --solos  (solo simula/puntua desde archivo)
"""
import sys, os, random, time, json, datetime, re
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# --- Perfil de Brian (para puntuar coincidencia) ---
KEYWORDS_PERFIL = {
    # (keyword, puntos, es_requisito_duro)
    "qa": 3, "tester": 3, "analista de calidad": 3, "quality": 2, "test": 1,
    "junior": 4, "trainee": 5, "sin experiencia": 5, "practicante": 4, "aprendiz": 3,
    "manual": 3, "funcional": 2, "api": 3, "postman": 3, "jira": 2, "sql": 2,
    "python": 2, "scrum": 1, "agile": 1, "remoto": 2, "hibrido": 1, "automation": 1,
}
KEYWORDS_NEGATIVAS = {
    "senior": 5, "sr.": 5, "lead": 5, "principal": 4, "manager": 4,
    "5 años": 4, "4 años": 4, "3 años": 3, "2 años": 3, "semi senior": 3,
    "automatizador senior": 4, "devops": 2, "data scientist": 3,
}

def puntuar_vacante(titulo, empresa="", ubicacion="", descripcion=""):
    """Puntua una vacante por coincidencia con el perfil. Devuelve (puntaje, razones).
    Regla dura: si el titulo no menciona QA/tester/calidad/testing, no es candidata aunque tenga 'junior'.
    """
    texto = f"{titulo} {empresa} {ubicacion} {descripcion}".lower()
    # Regla dura: debe ser QA/testing/calidad de software
    es_qa = any(k in titulo.lower() for k in ["qa", "tester", "test", "calidad", "quality", "pruebas", "testing"])
    if not es_qa:
        return -1, ["no es QA"]
    puntos = 0
    razones = []
    for kw, pts in KEYWORDS_PERFIL.items():
        if kw in texto:
            puntos += pts
            razones.append(f"+{pts} '{kw}'")
    for kw, pts in KEYWORDS_NEGATIVAS.items():
        if kw in texto:
            puntos -= pts
            razones.append(f"-{pts} '{kw}'")
    return puntos, razones

def buscar_linkedin(page, keywords, ubicacion="Colombia"):
    """Busca vacantes en LinkedIn Jobs y devuelve lista de dicts."""
    url = f"https://www.linkedin.com/jobs/search/?keywords={keywords}&location={ubicacion}&f_TPR=r604800"
    try:
        page.goto(url, wait_until="domcontentloaded", timeout=60000)
        time.sleep(random.uniform(6, 9))
        # scroll moderado (como persona que revisa empleos)
        for _ in range(3):
            page.mouse.wheel(0, 600)
            time.sleep(random.uniform(1.5, 2.5))
        cards = page.evaluate('''() => {
          const cs = Array.from(document.querySelectorAll('[data-occludable-job-id]'));
          const out = [];
          for (const c of cs) {
            const t = (c.innerText || '');
            if (!t || t.trim().length < 20) continue;
            const prom = t.includes('Promocionado');
            const lines = t.split(String.fromCharCode(10)).filter(x => x.trim());
            // primer par de lineas = titulo + empresa
            const titulo = lines[0] || '';
            const empresa = lines[1] || '';
            const id = c.getAttribute('data-occludable-job-id') || '';
            out.push({id: id, titulo: titulo.slice(0, 90), empresa: empresa.slice(0, 60), promocionado: prom, texto: t.slice(0, 400)});
          }
          return out;
        }''')
        return cards
    except Exception as e:
        print("[!] Error buscando en LinkedIn:", str(e)[:70])
        return []

def buscar_elempleo(page):
    """Busca en elempleo (portal colombiano, sin sesion)."""
    url = "https://www.elempleo.com/co/ofertas-empleo/trabajo-tester-qa-junior"
    try:
        page.goto(url, wait_until="domcontentloaded", timeout=60000)
        time.sleep(random.uniform(5, 8))
        txt = page.evaluate("document.body.innerText")
        # extraer bloques de ofertas por patron de salario/ubicacion
        jobs = []
        for m in re.finditer(r"([A-Z][^\n]{5,80})\nCOP\n(?:industry\n)?([^\n]{2,50})\n(?:Hace [^\n]+)\n([^\n]{2,60})", txt):
            titulo, empresa, meta = m.group(1).strip(), m.group(2).strip(), m.group(3).strip()
            if titulo and titulo not in [j["titulo"] for j in jobs]:
                jobs.append({"id": "elempleo", "titulo": titulo[:90], "empresa": empresa[:60],
                             "ubicacion": meta[:60], "promocionado": False, "texto": f"{titulo} {empresa} {meta}"})
        return jobs
    except Exception as e:
        print("[!] Error buscando en elempleo:", str(e)[:70])
        return []

def generar_reporte(vacantes, out_path="vacantes_hoy.txt"):
    """Puntua, ordena y guarda el reporte diario."""
    puntuadas = []
    for v in vacantes:
        pts, razones = puntuar_vacante(v.get("titulo", ""), v.get("empresa", ""),
                                       v.get("ubicacion", ""), v.get("texto", ""))
        if pts < 0:
            continue  # no es vacante de QA
        if v.get("promocionado") and pts < 5:
            continue  # saltar promocionados irrelevantes
        v["puntos"] = pts
        v["razones"] = razones
        puntuadas.append(v)
    puntuadas.sort(key=lambda x: x["puntos"], reverse=True)

    fecha = datetime.date.today().strftime("%d/%m/%Y")
    lines = []
    lines.append(f"# 🎯 VACANTES DETECTADAS - {fecha}")
    lines.append("")
    lines.append(f"Total encontradas: {len(vacantes)} | Coinciden con perfil: {sum(1 for v in puntuadas if v['puntos'] >= 5)}")
    lines.append("")
    lines.append("## 🟢 Mejores coincidencias (puntos >= 5)")
    lines.append("")
    top = [v for v in puntuadas if v["puntos"] >= 5]
    if not top:
        lines.append("(Ninguna vacante nueva con coincidencia alta hoy)")
    for v in top[:8]:
        lines.append(f"### ⭐ {v['puntos']} pts - {v['titulo']}")
        lines.append(f"- **Empresa:** {v.get('empresa', '?')}")
        if v.get("ubicacion"):
            lines.append(f"- **Ubicación:** {v['ubicacion']}")
        if v.get("id") and v["id"] != "elempleo":
            lines.append(f"- **Aplicar:** https://www.linkedin.com/jobs/view/{v['id']}/")
        else:
            lines.append(f"- **Aplicar:** https://www.elempleo.com/co/ofertas-empleo/trabajo-tester-qa-junior")
        if v.get("razones"):
            lines.append(f"- *Coincide:* {', '.join(v['razones'][:5])}")
        lines.append("")
    lines.append("## 🟡 Otras vacantes QA")
    lines.append("")
    for v in [x for x in puntuadas if 0 < x["puntos"] < 5][:6]:
        lines.append(f"- ({v['puntos']} pts) {v['titulo']} - {v.get('empresa', '?')}")
    lines.append("")
    lines.append("## 📌 Recordatorio")
    lines.append("- Postulate a 1-2 de las mejores HOY (las vacantes junior se llenan rápido)")
    lines.append("- Incluye tu portafolio: https://brian-gz-qa.github.io/portafolio-qa/")
    lines.append("- Personaliza el CV por vacante con tus proyectos de TripleTen")

    contenido = "\n".join(lines)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(contenido)
    print("[*] Reporte guardado:", out_path, f"({len(contenido)} chars)")
    return puntuadas

def detectar(page=None, out_path="vacantes_hoy.txt"):
    """Flujo principal de detección. Si no hay page, intenta conectarse."""
    if page is None:
        sys.path.insert(0, ".")
        from li_helpers import conectar, cerrar
        p, browser, page = conectar()
        propio = True
    else:
        propio = False

    try:
        print("=== DETECCIÓN DE VACANTES ===")
        vacantes = []
        # 1. LinkedIn Jobs - QA Junior
        print("[*] Buscando en LinkedIn Jobs (QA Junior)...")
        v1 = buscar_linkedin(page, "QA%20Tester%20Junior")
        vacantes += v1
        print(f"    -> {len(v1)} resultados")
        time.sleep(random.uniform(4, 7))
        # 2. LinkedIn Jobs - Analista de Calidad
        print("[*] Buscando en LinkedIn Jobs (Analista de Calidad)...")
        v2 = buscar_linkedin(page, "Analista%20de%20Calidad%20QA")
        vacantes += v2
        print(f"    -> {len(v2)} resultados")
        time.sleep(random.uniform(4, 7))
        # 3. elempleo
        print("[*] Buscando en elempleo (tester qa junior)...")
        v3 = buscar_elempleo(page)
        vacantes += v3
        print(f"    -> {len(v3)} resultados")

        # dedupe por titulo+empresa
        unicos = []
        vistos = set()
        for v in vacantes:
            clave = (v.get("titulo", "")[:40] + v.get("empresa", "")[:20]).lower()
            if clave not in vistos:
                vistos.add(clave)
                unicos.append(v)

        puntuadas = generar_reporte(unicos, out_path)
        print(f"\n[OK] Detección completada: {len(unicos)} vacantes, {sum(1 for v in puntuadas if v['puntos'] >= 5)} coinciden con tu perfil")
        return puntuadas
    finally:
        if propio:
            try:
                cerrar(p, browser, page)
            except TypeError:
                pass

if __name__ == "__main__":
    detectar()
