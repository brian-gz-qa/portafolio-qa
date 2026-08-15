# -*- coding: utf-8 -*-
"""
RUTINA DIARIA DE LINKEDIN (modo humano)
--------------------------------------
1. Comenta en 1-2 publicaciones del feed con valor
2. Publica 1 post con imagen generada (turno: manana / mediodia / noche)
3. Revisa mensajes y conexiones nuevas

Uso:  python rutina_diaria.py [--solo-revisar] [--turno manana|mediodia|noche]
Seguridad: pausas aleatorias humanas, 3 publicaciones/dia (1 por turno), 1-2 comentarios/dia.
"""
import sys, random, time, os, argparse, datetime
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, ".")
from li_helpers import conectar, cerrar
from gen_imagen_contenido import generar

def pausa(a, b):
    time.sleep(random.uniform(a, b))

TURNOS = {
    "manana":   {"hora": "08:00", "offset": 0},
    "mediodia": {"hora": "13:00", "offset": 1},
    "noche":    {"hora": "20:00", "offset": 2},
}
# Temas en orden de rotacion: cada turno usa un tema distinto por dia
TEMAS_ROTACION = ["errores_casos", "api_basico", "bug_jira", "equivalencia", "pregunta"]

def tema_para_turno(turno):
    """Elige el tema del turno segun el dia (sin repetir entre turnos del mismo dia)."""
    dia = datetime.date.today().toordinal()
    base = TURNOS[turno]["offset"]
    return TEMAS_ROTACION[(dia + base) % len(TEMAS_ROTACION)]

COMENTARIOS = [
    "Muy buen contenido. Como QA Tester en formación, estos temas me sirven muchísimo para entender mejor el ecosistema. Gracias por compartir 🙌",
    "Interesante punto. En QA siempre buscamos este tipo de análisis para mejorar la cobertura de pruebas. ¡Buen aporte!",
    "Excelente publicación. Me recuerda la importancia de la atención al detalle en testing — a veces el bug más crítico está en el detalle que nadie revisó. 👌",
    "Gracias por compartir. Aprender de experiencias así es clave para quienes estamos empezando en QA. 🙏",
]

TEXTOS_PUBLICACION = {
    "errores_casos": "🚀 Errores comunes al escribir casos de prueba\n\nEn mi bootcamp de QA en TripleTen aprendí que escribir buenos casos de prueba es un arte. Estos son los 5 errores que más vi (y cómo evitarlos):\n\n1️⃣ Ser vago: \"Verificar que funciona\" → especificar pasos, datos y resultado esperado.\n2️⃣ No definir el resultado esperado → sin él, no sabes si el test pasó o falló.\n3️⃣ Probar todo a la vez → casos pequeños y enfocados son más fáciles de diagnosticar.\n4️⃣ Olvidar casos negativos → probar lo que NO debe pasar es igual de importante.\n5️⃣ No usar datos variados → valores límite y datos inválidos destapan bugs ocultos.\n\n💡 Dato extra: con clases de equivalencia cubres más escenarios con menos casos.\n\n¿Cuál es el error #1 que cometes o has visto? Cuéntamelo en los comentarios 👇\n\n#QA #SoftwareTesting #ManualTesting #TestCases #TripleTen #QAEngineer",
    "api_basico": "🧪 Primeros pasos probando APIs con Postman\n\nEn el Sprint 4 de TripleTen validé APIs REST y esto es lo que todo QA debe dominar al inicio:\n\n✅ Métodos HTTP: GET (leer), POST (crear), PUT (actualizar), DELETE (borrar).\n✅ Status codes: 200 OK, 201 Creado, 400 Bad Request, 401 No autorizado, 404 No encontrado, 500 Error interno.\n✅ Probá siempre: valores límite, IDs inexistentes y datos inválidos.\n✅ Documentá cada caso: request, response y resultado esperado.\n\n📌 Escribí 60+ casos de prueba de API en mi portafolio: https://brian-gz-qa.github.io/portafolio-qa/\n\n¿Ya probaste APIs como QA? Cuéntame tu experiencia 👇\n\n#QA #APITesting #Postman #SoftwareTesting #TripleTen",
    "bug_jira": "🐛 ¿Cómo reportar un bug que los devs entiendan?\n\nDurante el bootcamp de TripleTen documenté 10+ bugs en Jira. La estructura que funciona:\n\n📋 Título claro: qué pasa, dónde, en qué condición (ej: \"Validación rota en campo de tarjeta\").\n📌 Pasos para reproducir: 1, 2, 3... exactos.\n✅ Resultado esperado vs. ❌ Real: la comparación es lo que hace el bug evidente.\n🎬 Evidencia: captura de pantalla o video siempre.\n🔢 Severidad y prioridad: crítico ≠ cosmético.\n\n💡 Un buen reporte de bug es la mitad del arreglo.\n\n¿Qué le pones a tus reportes de bugs? 👇\n\n#QA #BugReport #Jira #SoftwareTesting #TripleTen",
    "equivalencia": "🧠 Clases de equivalencia: prueba menos, cubre más\n\nUna de las primeras técnicas que aprendí en TripleTen y que cambió mi forma de testear:\n\n➡️ En vez de probar cada dato posible (imposible), agrupá las entradas en CLASES con el mismo comportamiento.\n\n💡 Ejemplo: un campo que acepta edades 18-65 → una clase válida (ej: 25) y dos inválidas (ej: 17 y 66). Con 3 datos cubrís miles de posibilidades.\n\n✅ Menos casos, mejor cobertura, bugs encontrados más rápido.\n\n¿Usás esta técnica en tus pruebas? 👇\n\n#QA #TestDesign #ISTQB #SoftwareTesting #TripleTen",
    "pregunta": "🤔 ¿Sabías que el 40% de los bugs se encuentran probando valores LÍMITE?\n\nEn mi bootcamp de TripleTen descubrí que los errores de software se esconden casi siempre en los bordes: el primer valor válido, el último, y justo el que no debería pasar.\n\n💡 Ejemplo rápido: si un campo acepta 1-100 caracteres, probá con:\n✅ 1 carácter (mínimo válido)\n✅ 100 caracteres (máximo válido)\n❌ 0 caracteres (inválido)\n❌ 101 caracteres (fuera de rango)\n\nCon 4 casos encontrás bugs que 100 pruebas 'normales' no verían.\n\n¿Ya aplicás las pruebas de límites en tus test cases? 👇\n\n#QA #SoftwareTesting #TestCases #ISTQB #TripleTen",
}

def comentar_en_feed(page, veces=1):
    """Comenta con valor en publicaciones del feed (ritmo humano, con reintentos)."""
    hechos = 0
    for _ in range(veces):
        # Scroll suave para cargar feed
        for _ in range(3):
            page.mouse.wheel(0, 600)
            pausa(2, 3)
        # Intentar en varias publicaciones hasta encontrar una que abra el editor
        intentos = 0
        while intentos < 3:
            intentos += 1
            pos = page.evaluate('''() => {
              const els = Array.from(document.querySelectorAll('button'));
              for (const b of els) {
                if ((b.getAttribute('aria-label')||'').trim() === 'Comentar' && b.offsetParent !== null) {
                  const r = b.getBoundingClientRect();
                  return {x: r.x + r.width/2, y: r.y + r.height/2};
                }
              }
              return null;
            }''')
            if not pos:
                print("[!] No hay boton Comentar")
                break
            page.mouse.click(pos["x"], pos["y"])
            pausa(5, 7)
            try:
                ed = page.locator(".ProseMirror").first
                ed.wait_for(state="visible", timeout=4000)
                ed.click(timeout=4000)
                pausa(1, 2)
                texto = random.choice(COMENTARIOS)
                for parte in texto.split(" "):
                    ed.type(parte + " ", delay=random.randint(35, 85))
                pausa(2, 3)
                btn = page.evaluate('''() => {
                  const edEl = document.querySelector('.ProseMirror');
                  const edr = edEl ? edEl.getBoundingClientRect() : null;
                  const els = Array.from(document.querySelectorAll('button')).filter(b => b.offsetParent !== null);
                  let best = null, bestD = 99999;
                  for (const b of els) {
                    const t = (b.innerText||'').trim();
                    if (t === 'Comentar') {
                      const r = b.getBoundingClientRect();
                      const d = edr ? Math.abs(r.y - edr.y) : 0;
                      if (d < bestD) { bestD = d; best = {x: r.x + r.width/2, y: r.y + r.height/2, d: d}; }
                    }
                  }
                  return best && best.d < 200 ? best : null;
                }''')
                if btn:
                    page.mouse.click(btn["x"], btn["y"])
                    print("[OK] Comentario publicado")
                    hechos += 1
                    pausa(7, 10)
                    break  # exito, salir del while
                else:
                    print("[!] No boton publicar (intento", intentos, ")")
            except Exception as e:
                print("[!] Error comentario intento", intentos, ":", str(e)[:60])
                # Cerrar si abrio algo y reintentar con otra publicacion
                page.keyboard.press("Escape")
                pausa(3, 4)
            # Scroll para buscar otra publicacion
            page.mouse.wheel(0, 500)
            pausa(2, 3)
        pausa(15, 25)
    return hechos

def publicar_post(page, tema, con_imagen=True):
    """Publica 1 post con imagen generada."""
    from gen_imagen_contenido import TITULOS
    if tema not in TEXTOS_PUBLICACION:
        print("[!] Tema no existe:", tema)
        return False
    ruta_img = None
    if con_imagen:
        ruta_img = os.path.abspath(f"post_{tema}_{datetime.date.today()}.png")
        try:
            generar(tema, ruta_img)
        except Exception as e:
            print("[!] No se genero imagen:", str(e)[:70])
            ruta_img = None
    page.goto("https://www.linkedin.com/feed/", wait_until="domcontentloaded", timeout=60000)
    pausa(8, 11)
    el = page.get_by_text("Crear publicación").first
    try:
        el.wait_for(state="visible", timeout=6000)
        el.click(timeout=5000)
    except Exception:
        print("[!] No boton Crear publicacion")
        return False
    pausa(6, 8)
    btn_pub = None
    for _ in range(4):
        try:
            btn_pub = page.get_by_text("Publicar", exact=True).first
            btn_pub.wait_for(state="visible", timeout=3000)
            break
        except Exception:
            try:
                el.click(timeout=3000)
            except Exception:
                pass
            pausa(3, 4)
    if not btn_pub:
        return False
    # Subir imagen si existe
    if ruta_img and os.path.exists(ruta_img):
        try:
            input_file = page.locator('input[type="file"]').first
            input_file.set_input_files(ruta_img)
            print("[OK] Imagen adjuntada")
            pausa(5, 7)
        except Exception as e:
            print("[!] No se pudo adjuntar imagen:", str(e)[:70])
    # Escribir texto
    escrito = False
    for sel in ['[data-lexical-editor]', '[contenteditable="true"]', '[role="textbox"]']:
        try:
            ed = page.locator(sel).first
            ed.wait_for(state="visible", timeout=3000)
            ed.click(timeout=4000)
            pausa(1, 2)
            for parte in TEXTOS_PUBLICACION[tema].split("\n"):
                ed.type(parte + "\n", delay=random.randint(40, 90))
                pausa(0.5, 1.2)
            print("[OK] Texto escrito")
            escrito = True
            break
        except Exception as e:
            print("[!] no con", sel, str(e)[:50])
    if not escrito:
        return False
    pausa(3, 5)
    try:
        btn_pub.click(timeout=6000)
        print("✅ PUBLICACIÓN ENVIADA")
        pausa(6, 9)
        return True
    except Exception as e:
        print("[!] clic Publicar:", str(e)[:70])
        return False

def revisar_mensajes(page):
    """Revisa la bandeja de mensajes y reporta nuevas conversaciones."""
    page.goto("https://www.linkedin.com/messaging/", wait_until="domcontentloaded", timeout=60000)
    pausa(7, 10)
    txt = page.evaluate("document.body.innerText")
    with open("bandeja_hoy.txt", "w", encoding="utf-8") as f:
        f.write(txt)
    print("[*] Bandeja revisada. Contenido guardado en bandeja_hoy.txt")
    return True

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo-revisar", action="store_true", help="Solo revisar feed y mensajes, sin publicar")
    ap.add_argument("--turno", default=None, choices=list(TURNOS.keys()), help="Turno del dia (manana/mediodia/noche)")
    ap.add_argument("--tema", default=None, help="Tema fijo de la publicacion (opcional)")
    ap.add_argument("--sin-imagen", action="store_true", help="No generar imagen")
    a = ap.parse_args()

    # Determinar tema: fijo, por turno, o por hora actual
    if a.tema:
        tema = a.tema
        turno = a.turno or "manana"
    else:
        if a.turno:
            turno = a.turno
        else:
            hora = datetime.datetime.now().hour
            if hora < 11:
                turno = "manana"
            elif hora < 17:
                turno = "mediodia"
            else:
                turno = "noche"
        tema = tema_para_turno(turno)
    print(f"[*] Turno: {turno} | Tema: {tema}")

    p, browser, page = conectar()
    try:
        # 1. Feed: comentar
        print("=== 1. INTERACCIÓN EN FEED ===")
        hechos = comentar_en_feed(page, veces=1)
        print(f"[*] Comentarios hechos: {hechos}")

        # 2. Publicar (si no es solo-revisar)
        if not a.solo_revisar:
            print("\n=== 2. PUBLICACIÓN DIARIA ===")
            ok = publicar_post(page, tema, con_imagen=not a.sin_imagen)
            print(f"[*] Publicacion: {'OK' if ok else 'FALLÓ'}")

        # 3. Revisar mensajes
        print("\n=== 3. REVISAR MENSAJES ===")
        revisar_mensajes(page)

        # 4. Detectar vacantes que coincidan con el perfil
        print("\n=== 4. DETECCIÓN DE VACANTES ===")
        try:
            from detectar_vacantes import detectar
            puntuadas = detectar(page, out_path="vacantes_hoy.txt")
            top = [v for v in puntuadas if v["puntos"] >= 5]
            print(f"[*] Vacantes con alta coincidencia hoy: {len(top)}")
            for v in top[:5]:
                print(f"    ⭐ {v['puntos']}pts - {v['titulo'][:60]} ({v.get('empresa','?')})")
        except Exception as e:
            print("[!] Error en detección de vacantes:", str(e)[:80])

        print("\n✅ RUTINA DIARIA COMPLETADA")
    finally:
        try:
            cerrar(p, browser, page)
        except TypeError:
            pass

if __name__ == "__main__":
    main()
