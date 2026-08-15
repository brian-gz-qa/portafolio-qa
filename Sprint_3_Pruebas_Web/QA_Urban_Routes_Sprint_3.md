# QA Urban Routes - Sprint 3

## Resumen del Proyecto
Sesión de pruebas de Aseguramiento de Calidad (QA) para la aplicación web **Urban Routes**, enfocada en las funcionalidades de "Compartir un automóvil", "Método de pago" y el proceso de "Reserva".

Se realizaron pruebas exploratorias y de validación de UI/UX tanto en Google Chrome como en Mozilla Firefox, detectando múltiples errores críticos y visuales que fueron documentados en Jira.

## Errores Reportados (Jira)

* **[[SDD-1]] - Íconos de autos faltantes en el mapa**
  * **Problema:** En el mapa de navegación no aparece el ícono del automóvil más cercano ni ningún otro automóvil disponible al cargar la interfaz.
* **[[SDD-2]] - Opciones faltantes en tarifa "De Lujo"**
  * **Problema:** Al seleccionar la tarifa "De lujo", el panel de "Requisitos del pedido" no muestra las opciones de "Luz de discoteca" (casilla de verificación) ni el apartado "Relajante" (botones de radio para bebidas y fruta), las cuales sí están contempladas en el diseño.
* **[[SDD-4]] - Marca y placa faltantes en la reserva (Chrome)**
  * **Problema:** La ventana de "Automóvil reservado" muestra la tarifa (ej. "De lujo") en lugar de la marca del auto (ej. "Porsche 911"), y no muestra la placa del vehículo.
* **[[SDD-5]] - Falta de confirmación al cancelar viaje**
  * **Problema:** Al dar clic en el botón de cancelar (X), no aparece la ventana secundaria pidiendo confirmación ("¿Seguro que quieres cancelar el viaje?") y cancela/omite el proceso sin preguntar.
* **[[SDD-6]] - BUG CRÍTICO: Validación rota en campos de tarjeta**
  * **Problema:** Los campos "Número de tarjeta" y "Código" carecen de validación. Permiten ingresar caracteres alfabéticos, especiales y kanjis sin límite de longitud. Lo más grave es que el sistema valida estos datos y permite agregar una tarjeta falsa.
* **[[SDD-7]] - Interfaz de pago no muestra últimos 4 dígitos**
  * **Problema:** Tras agregar una tarjeta exitosamente, la interfaz solo dice "Tarjeta" en lugar de mostrar los últimos 4 dígitos (ej. "Tarjeta **** 1111").
* **[[SDD-8]] - BUG CRÍTICO: Reserva sin método de pago**
  * **Problema:** El sistema permite finalizar una reserva haciendo clic en "Agregar método de pago y reservar" usando solo una licencia de conducir, omitiendo por completo el requisito del método de pago.
* **[[SDD-9]] - Botón "Agregar licencia" no responde**
  * **Problema:** Al faltar la licencia de conducir, el botón muestra el texto correcto, pero no responde al hacer clic, impidiendo al usuario abrir el formulario para agregarla.
* **[[SDD-10]] - Panel desaparece al borrar direcciones**
  * **Problema:** Al borrar las direcciones de "Desde" y "Hasta", el panel inferior completo (con tarifas y botón) desaparece en lugar de mostrar un botón inactivo, reiniciando la aplicación y perdiendo el progreso.

## Aprendizajes Clave de QA
* **Pruebas exploratorias:** Probar los errores en múltiples escenarios (ej. probando diferentes tarifas o escribiendo Kanjis) ayuda a identificar si un bug es específico o global.
* **Aislar variables:** Para verificar si un campo específico activa/desactiva un botón, los demás campos obligatorios deben estar correctos. Si el botón se activa ignorando una regla, la regla está rota.
* **Bugs bloqueantes:** Cuando un error impide visualizar la pantalla (como la ventana que se cierra en Firefox), los casos de prueba posteriores se marcan como fallidos (No Aprobado/Bloqueado) y se enlazan al ticket del bug principal.
* **Reutilización de Bugs:** Al hacer pruebas de flujo final (como el alquiler), muchos casos de prueba fallan debido a errores ya descubiertos en componentes individuales. Identificar la causa raíz permite enlazar el mismo ticket de Jira en lugar de duplicar el trabajo.

## Estado del Proyecto
* **COMPLETADO AL 100%:** Sprint 3 de Aseguramiento de Calidad para Urban Routes finalizado con éxito. Todas las pestañas del documento de Google Sheets fueron ejecutadas y evaluadas correctamente.

## Evaluación del Revisor (Melissa Becerra)
✅ **Proyecto aprobado**
✅ Autorizado para avanzar al siguiente sprint (Sprint 4).

**Comentarios destacados:**
* Los bugs documentados están excelentemente relacionados con las validaciones y casos de prueba correspondientes.
* La estructura de los reportes es adecuada, detallada y profesional para su revisión.
* Se cumplieron con creces los criterios esperados tras implementar las correcciones (valores límite como el "00", bugs de localización y traductor automático, etc).
