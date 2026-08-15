# 🚀 Guía para publicar tu portafolio en GitHub Pages

Tu portafolio **ya está listo y organizado** en esta carpeta (Documentos/Portafolio_QA_Brian), con commit inicial hecho. Solo falta publicarlo online. Sigue estos pasos:

---

## Paso 1 — Crea tu cuenta de GitHub (~5 min)

1. Entra a **https://github.com/signup**
2. Usa tu correo: **gz.sotto@gmail.com**
3. Elige un nombre de usuario (ej: `brian-gz-qa`)
4. Verifica tu correo con el código que te llega
5. Listo, ya tienes cuenta

## Paso 2 — Crea el repositorio

1. Entra a **https://github.com/new**
2. **Nombre del repositorio:** `portafolio-qa` (en minúsculas)
3. **Visibilidad:** selecciona **Público** (necesario para GitHub Pages gratis)
4. **NO marques** "Add a README file" (ya tenemos todo listo)
5. Clic en **Create repository**

## Paso 3 — Sube tu portafolio (1 clic)

1. Abre la carpeta **Documentos\Portafolio_QA_Brian**
2. Haz **doble clic en `SUBIR_A_GITHUB.bat`**
3. La primera vez edita el archivo con el Bloc de notas y escribe tu usuario de GitHub en la línea `set USUARIO=...`
4. Vuelve a ejecutar el `.bat`
5. Si pide contraseña: usa un **Personal Access Token** (ver Paso 4)

## Paso 4 — Si pide contraseña (token)

1. Entra a **https://github.com/settings/tokens** → **Generate new token (classic)**
2. Marca la casilla **repo**
3. Crea el token y **cópialo** (solo se ve una vez)
4. Pégalo como contraseña cuando el script lo pida

## Paso 5 — Activa GitHub Pages

1. Entra a **https://github.com/TU_USUARIO/portafolio-qa/settings/pages**
2. En **Branch** selecciona: `main` y carpeta `/ (root)`
3. Clic en **Save**
4. Espera 1-2 minutos
5. Tu portafolio estará en: **https://TU_USUARIO.github.io/portafolio-qa**

---

## 🎉 Después de publicar

- **Añade el enlace a LinkedIn**: ve a tu perfil → sección "Destacado" → "+" → "Añadir un enlace" → pega la URL de tu portafolio
- **Añádelo a tu CV**: junto a tu email y LinkedIn
- **Añádelo a tu firma de correo**
- **Comparte una publicación** en LinkedIn anunciando tu portafolio (estructura: qué problema resolviste → qué herramientas usaste → qué resultados obtuviste)

## 📁 Estructura de esta carpeta

```
Portafolio_QA_Brian/
├── index.html                  ← Portada del portafolio (se ve en GitHub Pages)
├── README.md                   ← Descripción completa (se ve en el repo)
├── Sprint_1_Introduccion/      ← Requisitos + casos de prueba iniciales
├── Sprint_2_Tecnicas_Pruebas/  ← Clases de equivalencia, pairwise, mapas mentales
├── Sprint_3_Pruebas_Web/       ← Pruebas funcionales Urban Routes + bugs Jira
├── Sprint_4_Pruebas_API/       ← 60+ casos de prueba API + reportes de bugs
├── Sprint_5_CPC/               ← CV, carta de presentación, portada LinkedIn
├── Proyectos_Extra/            ← Proyectos personales adicionales
├── SUBIR_A_GITHUB.bat          ← Script de subida automática
└── GUIA_GITHUB_PASO_A_PASO.md  ← Esta guía
```

¡Éxitos! 🚀
