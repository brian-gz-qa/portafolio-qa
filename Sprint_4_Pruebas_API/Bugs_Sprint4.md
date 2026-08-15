# Registro de Bugs - Sprint 4 (QA Urban Routes)

Este documento contiene el registro de todos los bugs encontrados durante las pruebas de la API en el Sprint 4, para que NOE y la memoria del sistema tengan acceso al progreso.

## Bug 1: Límite de productos exacto
* **Casos:** 2
* **Descripción:** El servidor devuelve 400 Bad Request al enviar exactamente 30 productos (que es el límite permitido). El límite se configuró como `< 30` en lugar de `<= 30`.
* **Severidad:** Alta
* **Prioridad:** Media

## Bug 2: Falta de validación de tipo en ID de URL
* **Casos:** 6, 7, 8
* **Descripción:** El servidor arroja 500 Internal Server Error cuando se envían caracteres no numéricos (romanos, letras) o decimales en el parámetro ID de la URL (`/api/v1/kits/VI/products`).
* **Severidad:** Alta
* **Prioridad:** Alta

## Bug 3: Falta de validación de estructura Array en Body
* **Casos:** 10, 11
* **Descripción:** El servidor devuelve 404 Not Found y un error interno de base de datos (`container not found`) cuando el parámetro `productsList` se envía como String o Null en lugar de un Array.
* **Severidad:** Alta
* **Prioridad:** Media

## Bug 4: Aceptación de Payload vacío
* **Casos:** 12, 13
* **Descripción:** El servidor devuelve 200 OK y no realiza validación cuando se envía un arreglo vacío `[]` o un body completamente vacío `{}`.
* **Severidad:** Media
* **Prioridad:** Baja

## Bug 5: Error interno por tipo de dato inválido en quantity
* **Casos:** 24, 25, 26, 27
* **Descripción:** El servidor devuelve 500 Internal Server Error por error de sintaxis `NaN` o tipo incorrecto en la base de datos cuando se omite el parámetro `quantity` o se envían decimales/letras.
* **Severidad:** Alta
* **Prioridad:** Alta

## Bug 6: Fallo silencioso con IDs de producto inexistentes
* **Casos:** 14, 15, 16
* **Descripción:** El servidor devuelve 200 OK cuando se intenta agregar un ID numérico que no existe en la base de datos (como 9999, 0, o -1), en lugar de devolver un 400 Bad Request por producto no encontrado. La petición simplemente es ignorada.
* **Severidad:** Media
* **Prioridad:** Media

## Bug 7: Crash (Error 500) por tipo de dato inválido en ID de producto
* **Casos:** 17, 18, 19, 20
* **Descripción:** El servidor colapsa (500 Internal Server Error) cuando se omite el parámetro `id` en el body, o cuando se envía con un tipo de dato no entero (decimal, palabra, letra).
* **Severidad:** Alta
* **Prioridad:** Alta

## Bug 8: Fallo silencioso con cantidades nulas o negativas
* **Casos:** 22, 23
* **Descripción:** El servidor devuelve 200 OK cuando se envían cantidades inválidas lógicamente (0 o -1) en lugar de devolver un 400 Bad Request. La petición es ignorada silenciosamente.
* **Severidad:** Media
* **Prioridad:** Media

## Bug 9: Ausencia de límites de horario en deliveryTime
* **Casos:** 30, 33 (y similares fuera de horario)
* **Descripción:** El servidor devuelve 200 OK y `isItPossibleToDeliver: true` al ingresar horas de entrega fuera del horario laboral válido (ej. 7, 23, 24). Debería devolver 400 Bad Request o `isItPossibleToDeliver: false`.
* **Severidad:** Alta
* **Prioridad:** Alta

## Bug 10: Ausencia total de validación de tipos en deliveryTime
* **Casos:** 34, 35, 36, 37, 38
* **Descripción:** El servidor devuelve 200 OK y procesa el pedido exitosamente al enviar tipos de datos inválidos en el `deliveryTime` (negativos, decimales, letras, números romanos) e incluso si se omite por completo el parámetro.
* **Severidad:** Alta
* **Prioridad:** Alta

## Bug 11: Aceptación de pesos nulos y negativos en productsWeight
* **Casos:** 40, 43
* **Descripción:** El servidor devuelve 200 OK al enviar un peso de `0` o `-2.5` en el parámetro `productsWeight`. Falla la validación lógica de negocio ya que un peso no puede ser nulo o negativo.
* **Severidad:** Media
* **Prioridad:** Media

## Bug 12: Ausencia total de validación de tipos en productsWeight
* **Casos:** 44, 45, 46
* **Descripción:** El servidor devuelve 200 OK al enviar cadenas de texto ("II", "two") o al omitir por completo el parámetro `productsWeight`. No hay validación de tipo ni obligatoriedad.
* **Severidad:** Alta
* **Prioridad:** Alta

## Bug 13: Ausencia total de validaciones en productsCount
* **Casos:** 48, 50, 51, 52, 53, 54
* **Descripción:** El servidor devuelve 200 OK al enviar cantidades de productos irreales (0, negativos como -1), de tipo incorrecto (decimales como 1.5, texto como "X") e incluso si se omite el parámetro. Carece de cualquier tipo de validación.
* **Severidad:** Alta
* **Prioridad:** Alta

## Bug 14: Aceptación de Payload vacío en Order and Go
* **Casos:** 55
* **Descripción:** El servidor devuelve 200 OK y realiza cálculos de entrega al enviar un body completamente vacío `{}`, sin exigir ningún parámetro obligatorio.
* **Severidad:** Alta
* **Prioridad:** Alta

## Bug 15: Aceptación de valores booleanos y campos extraños
* **Casos:** 58, 59
* **Descripción:** El servidor devuelve 200 OK al enviar valores de tipo booleano (`true`, `false`) en lugar de números, y acepta parámetros inventados (`campoInvento`) sin realizar ninguna sanitización del payload.
* **Severidad:** Media
* **Prioridad:** Media

## Bug 16: Error 404 de base de datos por arreglos en parámetros
* **Casos:** 60
* **Descripción:** El servidor devuelve 404 Not Found (con un mensaje interno de "container not found" en formato HTML) cuando se envían Arreglos (`[9]`) en lugar de números en los parámetros del body, provocando un error en el backend.
* **Severidad:** Alta
* **Prioridad:** Alta
