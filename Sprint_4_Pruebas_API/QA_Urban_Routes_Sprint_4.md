Sprint 4: Pruebas de API
Capítulo 1/6 · Faltan 4 lecciones
Fundamentos de API: Comunicación con el Backend
25 min
Introducción a las pruebas de API
Imagina esto: estás probando una app para pedir comida a domicilio. Eliges tu comida favorita, haces clic en “Pedir”… y no pasa nada. Todo parece estar bien: el botón se ve bien, no hay nada raro en los textos y la navegación se siente fluida. Entonces, ¿qué está fallando?
  

Como QA engineer, no basta con revisar lo que se ve. También hay que preguntarse: ¿se está comunicando la app correctamente con el servidor? ¿Los datos llegan a su destino debidamente?
Ahí entra en juego la API, la protagonista de este capítulo.
Si no sabes cómo funciona, podrías pasar por alto algunos errores importantes: tal vez el botón responde, pero los datos no llegan; o la interfaz dice que todo salió bien, cuando no es cierto.
¡No te preocupes! En este sprint aprenderás a mirar más allá de lo que se muestra en pantalla y detectar esos errores invisibles que la mayoría no nota.
¿De qué trata este capítulo?
Al final de este capítulo, comprenderás cómo se comunican las distintas partes de una app a través de una API —y por qué eso es importante para tu trabajo como QA engineer—. También descubrirás la diferencia entre lo que pasa en pantalla y lo que ocurre por detrás, y cómo configurar una herramienta que te permita explorar y probar APIs por tu cuenta.
API en la arquitectura de una aplicación web
¿Prefieres leer? Haz clic aquí para ver la transcripción.
  

Pregunta
Subes una nueva foto de perfil a una red social. Después de unos segundos, la imagen actualizada aparece en tu perfil y tus amigos también pueden verla.
¿Qué parte de la app se encarga de procesar y guardar tu nueva foto antes de que se muestre?
La API
El backend
¡Correcto! El backend hace el trabajo real: procesa y guarda el archivo. El frontend solo envía la solicitud y muestra el resultado.
El frontend
¡Bien hecho!
Pregunta
Tocas “Seguir mi pedido” en una app de compras y ves la información de entrega del servicio de mensajería. ¿Qué parte de la app se conecta con ese sistema externo para obtener los datos?
El frontend
El backend
La API
¡Correcto! La API envía la solicitud al sistema del mensajero y trae la información de vuelta. Es el puente que permite esa comunicación.
¡Buen trabajo!
Supongamos que abres tu app de red social favorita y tocas el ícono de notificaciones para ver qué hay de nuevo.
Esto es lo que realmente sucede detrás de cámaras:
* Tú (el cliente) tocas el ícono de la campanita.
* La app envía una solicitud a través de la API al servidor, preguntando: “¿Cuáles son las notificaciones más recientes de este usuario?”
* El servidor revisa su memoria interna, donde guarda temporalmente las notificaciones recientes.
* Extrae los datos relevantes y los envía de vuelta a través de la API.
* La app te muestra tus notificaciones más recientes.
  

Pregunta
¿Qué parte del sistema realiza cada paso cuando la app de Urban.Routes usa Google Maps para mostrar la ruta y el tiempo estimado de viaje al usuario?
Muestra los campos donde el usuario ingresa el punto de inicio y de destino.
Frontend
¡Correcto! El frontend es la parte visible de la app: permite al usuario ingresar su información.
Envía los datos de ubicación a Google Maps y recibe los detalles de la ruta.
API
¡Así es! La API se encarga de conectar la app con Google Maps y gestionar el intercambio de datos.
Calcula la duración estimada del viaje con base en los datos de la ruta.
Backend
¡Muy bien! El backend procesa los datos y realiza los cálculos necesarios para el viaje.
Muestra al usuario el mapa y el tiempo estimado en pantalla.
Frontend
¡Así es! El frontend toma los resultados procesados y los presenta visualmente al usuario.
¡Tu comprensión del material es impresionante!
Ahora que ya sabes qué papel cumple la API en la arquitectura de una aplicación web, vamos a aprender más sobre cómo funciona.
Valoración de la lección
Siguiente






Sprint 4: Pruebas de API
Capítulo 1/6
Fundamentos de API: Comunicación con el Backend
20 min
Tipos de APIs
¿Prefieres leer? Haz clic aquí para ver la transcripción.
Casi todas las aplicaciones web que usamos hoy en día funcionan con APIs. Piensa en tu app de redes sociales favorita: tiene partes para subir fotos, mostrar publicaciones o reproducir videos. Estas partes se comunican a través de APIs. Seguramente hayas notado que no todas responden igual: algunas cargan rápido y otras tardan más.
Quizás recuerdes la metáfora del restaurante de la lección anterior. No todos los restaurantes tienen el mismo tipo de “mesero”: puede ser una persona, una ventanilla para autos o una pantalla de autoservicio. Algunos tienen un servicio rápido, otros son más formales, y algunos te dejan personalizar cada detalle del platillo. El objetivo es el mismo, pero su forma de atender al cliente puede variar.
  

Con las APIs pasa algo similar. Hay distintos tipos, y cada uno conecta los sistemas de forma un poco diferente. Por eso algunas interacciones se sienten más rápidas, mientras otras son más lentas o actúan distinto.
Como QA engineers, no elegimos qué tipo de API se usa —eso lo decide el equipo de desarrollo— pero sí necesitamos entender cómo funciona. El tipo de API cambia la forma en que se realizan las pruebas: qué hay que revisar, cómo detectar errores y qué herramientas usar. Cuanto mejor la entendamos, mejores serán nuestras pruebas.
¿Qué tipos de APIs existen?
Veamos más de cerca los diferentes tipos de APIs.
💡
Los tipos de API siguen distintos estilos de comunicación — algunos usan formatos muy estrictos, mientras que otros permiten formas más flexibles de pedir información.
🔐 SOAP
Muy estricto y estructurado. Se enfoca en la seguridad, el control y la fiabilidad.
Se usa en sistemas que manejan datos sensibles —como bancos, aseguradoras o plataformas corporativas—.
Imagina que haces un pedido en una pantalla táctil en el aeropuerto. Tienes que seguir los pasos exactos, elegir entre un conjunto fijo de opciones y confirmar cada detalle antes de que el sistema acepte tu pedido. Si falta algo o hay un error, no puedes continuar.
Las APIs SOAP funcionan de forma similar. Requieren solicitudes con un formato muy preciso —normalmente en XML— y responden de manera estructurada. Esto las hace más lentas y complejas de usar, pero también más predecibles y seguras.
⚡ GraphQL
GraphQL es un tipo de API que permite a las apps pedir solo la información que realmente necesitan. Nada más.
Se usa mucho en apps donde cada persona ve un contenido diferente —como redes sociales o apps móviles— y donde es importante cargar solo lo necesario y hacerlo rápido. Por ejemplo, puedes solicitar únicamente el nombre de usuario y su foto, sin tener que acceder a todo su perfil.
Pero probar una API GraphQL puede ser algo más complicado. ¿Por qué?
Porque la app no siempre pide lo mismo, cambia según la situación. Para comprobar que todo funciona, hay que saber qué quería obtener la app y verificar si lo recibió correctamente.
Además, si algo dentro del sistema cambia, tus pruebas pueden dejar de funcionar, aunque la app parezca estar bien.
🌐 REST
REST es el tipo de API más común en sitios y aplicaciones web. La encontrarás en tiendas en línea, blogs, mapas y más.
Es simple y clara. Las APIs REST utilizan URLs legibles que muestran con qué datos estás trabajando —a diferencia de otros tipos como GraphQL o SOAP, que dependen de un solo punto de acceso o formatos más complejos—.
Las apps que usan REST siguen reglas predecibles para enviar y recibir información, lo que facilita entender qué ocurre y verificar que todo funcione bien.
Además, REST es fácil de probar: puedes usar herramientas gratuitas para enviar solicitudes paso a paso y ver qué datos se intercambian, sin tener que hacer complejas configuraciones.
Por eso usaremos REST en este curso: es popular, fácil de aprender y excelente para conocer cómo funcionan las APIs reales, sin caer en complicaciones innecesarias.
Solo ten en cuenta que puede ser menos eficiente en sistemas complejos, por ejemplo: si necesitas hacer varias solicitudes para obtener datos relacionados o si devuelve más información de la necesaria.
  

Pregunta
¿Qué tipo de API encaja mejor con la funcionalidad descrita?
Una función en una app de fitness que necesita cargar rápidamente solo el nombre del usuario, el recuento de los pasos diarios y la frecuencia cardíaca para mostrarlos en la pantalla de bloqueo.
GraphQL
¡Correcto! GraphQL es perfecto para obtener rápidamente solo los datos necesarios.
Un sistema interno de RR. HH. donde los empleados suben documentos e información personal confidencial.
SOAP
¡Exacto! Las estrictas normas de SOAP son adecuadas para sistemas sensibles y de alta seguridad.
Una app de pedidos online para restaurantes que permite a los clientes explorar los menús y realizar pedidos con un tiempo de carga mínimo.
REST
¡Exacto! REST gestiona solicitudes rápidas y sencillas de forma eficiente.
¡Buen trabajo!
Valoración de la lección
Siguiente






Sprint 4: Pruebas de API
Capítulo 1/6
Fundamentos de API: Comunicación con el Backend
15 min
Postman: Configurando nuestro espacio de trabajo de APIs
Hemos estado aprendiendo qué son las APIs y para qué sirven. Pero aún nos falta responder una pregunta importante: ¿Cómo podemos comprobar si una API funciona correctamente?
Para eso, permíteme presentarte una de las herramientas más populares y utilizadas en la industria: Postman.
Postman es un programa que te permite “hablar” con una API: puedes enviarle información como si fueras una aplicación, y ver cómo responde, ¡y todo esto sin la necesidad de escribir código!
Puedes pensar en Postman como un simulador del lado del cliente —con ella, no tienes la necesidad de usar la interfaz del sitio o la app real—. Es una herramienta muy útil tanto para QA engineers como para desarrolladores, ya que permite observar qué está pasando exactamente en esa interacción.
Así que no esperemos más, ¡vamos a instalar Postman y a descubrir cómo funciona!
Instalar y abrir Postman por primera vez
¿Prefieres leer? Haz clic aquí para ver la transcripción.
Para empezar, debemos acceder al sitio oficial de Postman: https://www.postman.com/downloads/ y descargar la versión correspondiente a tu sistema operativo. Postman está disponible para Windows, Mac y Linux.
  

Una vez que lo tengas descargado, ejecuta el instalador como administrador y completa el proceso de instalación de acuerdo a tu sistema operativo.
Una vez instalado, abre Postman y lo primero que verás es una pantalla de bienvenida, junto con la opción para crear una cuenta:
  

Vamos a crear una cuenta: haz clic en el botón “Sign up for Free”. Esto abrirá un navegador con el portal para crear la cuenta:
  

Continúa creando la cuenta con tu método de preferencia, te sugerimos hacer clic en la casilla para mantenerte conectado “Stay signed in”. Después, se te pedirá que hagas un proceso de verificación de la cuenta, así que revisa tu correo para completarlo.
  

¡Y listo! Te redirigirá directamente a la aplicación de Postman y con eso tendrás todo lo necesario para empezar a trabajar con APIs.
  

¡No te dejes intimidar por la interfaz! Es bastante sencilla, en cuestión de minutos estarás haciendo tu primera “solicitud”.
Valoración de la lección
Siguiente


Sprint 4: Pruebas de API
Capítulo 1/6
Fundamentos de API: Comunicación con el Backend
25 min
Cómo funcionan las APIs: solicitudes y respuestas
Pruebas de frontend y backend
¡Un día más, otra prueba más! Esta vez con un código de descuento: WELCOME10, 10 % de descuento.
Como QA engineer, entras al sitio, agregas un producto al carrito, le aplicas el código, ves el mensaje “Descuento aplicado” y completas la compra. Todo parece funcionar bien desde el punto de vista de la interfaz.
Pero decides verificar qué ocurrió en el backend… y descubres que el sistema cobró el precio completo. La interfaz decía una cosa, pero el sistema hizo otra.
¡Oh no! ¿Y si un cliente real se hubiera topado con esto?
  

Las pruebas de frontend ayudan a detectar errores visibles: botones rotos, mensajes incorrectos, problemas de diseño, etc. Sin embargo, no confirman si el sistema realmente hizo lo que debía hacer.
Ahí es donde entran las pruebas de backend. En vez de actuar como un usuario, te comunicas directamente con el sistema: le envías las instrucciones y revisas la respuesta que obtienes de él.
📎
En frontend, el éxito significa que todo se ve bien.
En backend, que el sistema actuó correctamente, incluso si no hay ningún cambio visual.
Seguirás usando casos de prueba e informes de errores, pero ahora enfocados en lo que enviaste y lo que el sistema hizo, no solo en lo que se ve.
Esto te permite probar situaciones que la interfaz no muestra, como datos no válidos o errores ocultos.
Pregunta
Estás probando una función para cambiar el correo electrónico en un perfil de usuario. ¿Cómo puedes confirmar que el cambio realmente se realizó?
Verificando que aparezca el mensaje de éxito al hacer clic en “Guardar”
Actualizando la página y comprobando si el nuevo correo sigue ahí
Inspeccionando qué guardó el sistema después de hacer clic en “Guardar”
¡Correcto! Esto te permite confirmar si el backend realmente guardó el nuevo correo, no solo que lo muestre la interfaz.
Asegurándote de que al hacer clic en “Guardar” la página no se bloquee
¡Lo has entendido bien!
¿Cómo funciona una API?
Ya dijimos que la API conecta el frontend con el backend, pero ¿cómo ocurre realmente esa comunicación?
Todo se basa en un ciclo simple: una solicitud y una respuesta.
  

Volvamos al ejemplo del código de descuento.
Escribes WELCOME10 en el sitio y haces clic en “Aplicar”. Ese clic no aplica el descuento por sí solo, lo que hace es enviar una solicitud al servidor a través de la API. Esa solicitud dice algo como:
“Esta persona quiere aplicar WELCOME10 a su pedido.”
El servidor verifica el código y devuelve una respuesta, por ejemplo:
“Descuento aplicado: 10 %”
o “Código expirado”
El frontend simplemente muestra ese mensaje.
  

  

📎
Lo que hace posible este intercambio se llama HTTP: un protocolo que le dice a la API cómo entregar los mensajes entre el cliente y el servidor.
En nuestra metáfora del restaurante, es como el reglamento de servicio: indica al mesero cómo tomar el pedido, cómo llevarlo a la cocina y cómo traer la comida de regreso a la mesa.
Como testers, podemos probar el ciclo de solicitud y respuesta directamente en Postman: puedes cambiar los datos, dejar algo vacío, enviar información incorrecta… y ver cómo responde el sistema.
Y ya que hablamos de Postman… ¿qué tal si enviamos nuestra primera solicitud?
Tu primera tarea de prueba de API
Uno de los proyectos en los que trabaja tu equipo es la app Urban.Grocers, una plataforma interactiva para hacer la compra doméstica.
Acabas de recibir tu primera tarea para probar una API con Postman.
No te preocupes: vamos a recorrerla paso a paso.
Paso 1: Crea una colección en Postman
Como es tu primera vez usando Postman, empieza creando una Colección, es decir, un espacio para organizar tus solicitudes.
Haz lo siguiente:
* Asegúrate de que “Collections” (Colecciones) esté seleccionado en la barra lateral izquierda.
* Haz clic en “Create Collection” (Crear colección).
* Cambia el nombre predeterminado a “Tareas Tripleten.”
¿Todo listo? ¡Perfecto! Sigamos.
Paso 2: Analiza la tarea
El equipo de desarrollo está por lanzar una nueva funcionalidad: los usuarios podrán pedir Kits: paquetes temáticos de productos comestibles (como un set para picnic o una cena de pasta).
Tu tarea es probar la API que devuelve la lista de kits disponibles. Cuando la app le pide esa información al servidor, revisas si los resultados son correctos, es decir, si cuenta con los nombres, precios y listas de productos adecuados.
Empiezas como cualquier buen QA engineer: revisando la documentación.
Para enviar tu primera solicitud, debes explorar qué espera la API: qué datos necesita y cómo debería verse su respuesta.
Esto es lo que encuentras en los requisitos de esta funcionalidad:
  

Paso 3: Crea tu primera solicitud
Ahora que ya revisaste los requisitos, es el momento de crear tu primera solicitud en Postman.
En Postman, crearás tu solicitud en el panel central.
  

Sigue estos pasos:
* Haz clic en “Add Request” (Agregar solicitud) dentro de tu colección “Tareas Tripleten”.
* Nombra la solicitud como “Obtener Kits”.
* En la barra de la solicitud, asegúrate de que el menú desplegable más a la izquierda esté configurado como GET.
* Inicia el servidor de Urban.Grocers.
Servidor
¡Genial, tu servidor ha sido iniciado!
Dirección del servidor: https://cnt-774e32dc-89f3-4262-83b6-d227d5068bb5.containerhub.tripleten-services.com
Reiniciar el servidor
* Copia la URL que aparece al iniciarlo y pégala en el campo de la solicitud en Postman.
* Después de la URL base, añade la siguiente ruta: /api/v1/kits?cardId=1
* Haz clic en Send (Enviar).
Paso 4: Revisa la respuesta
Tu siguiente paso es revisar la respuesta, es decir, lo que el sistema envía de vuelta después de enviar tu solicitud.
En Postman, la respuesta aparece en la sección inferior.
Ahí verás un bloque de texto que muestra varios kits, cada uno con su nombre, ID y lista de productos.
En la esquina inferior derecha, verás un punto verde y la etiqueta “200 OK”: este código de estado indica que la solicitud se gestionó correctamente.
Ahora compáralo con los requisitos: ¡el estado coincide con el resultado esperado!
  

En la sección del cuerpo puedes ver que la solicitud trajo una lista de productos para el kit “Para pícnics”. Por ejemplo, aquí puedes ver uno de los artículos:
  

¡Esto también es correcto!
  

✅ Tu prueba fue exitosa: el servidor devolvió los datos y el estado correctos.
¡Y así de fácil es! Ya probaste tu primera API. ¿No fue tan difícil, verdad?
Por ahora, solo rellenaste los campos.
En el siguiente capítulo, descubrirás qué significa realmente cada parte y aprenderás cómo usarlas para crear pruebas más efectivas por tu cuenta.
Valoración de la lección
Siguiente


Sprint 4: Pruebas de API
Capítulo 2/6 · Faltan 8 lecciones
Ciclo de Solicitud y Respuesta de la API: Enviar, Recibir, Validar
35 min
Métodos: La acción dentro de una solicitud
Tienes una nueva tarea: verificar si los kits funcionan tras una actualización.
El sistema debe poder:
* Buscar kits.
* Crear uno nuevo.
* Editar uno existente.
* Eliminar uno innecesario.
Antes de hacer las pruebas, necesitas entender cómo funciona una solicitud. Vamos a verlo paso a paso:
¿Cómo funciona realmente una solicitud?
En la lección anterior, enviaste tu primera solicitud. Pero, ¿cómo funciona una solicitud?
Para comunicarte con una API, necesitas responder tres preguntas esenciales:
Cómo, Dónde y Qué.
En esta lección, nos centraremos en la primera de esas preguntas: Cómo.
Más específicamente:
"¿Cómo debería manejar el servidor tu solicitud?"
Para eso sirve el método.
  

¿Qué es un método?
📎Un método define la acción que el servidor debe realizar cuando recibe tu solicitud.
Volviendo a nuestra analogía del restaurante, el método es la acción que le estás pidiendo al mesero que realice con tu pedido. Puedes pedirle que te traiga el menú, pero también podrías pedirle que cancele tu pedido.
Cada método representa esta acción específica —como GET, POST, PUT o DELETE— y elegir el adecuado es clave para que tu solicitud funcione como esperas.
  

Como tester, tu responsabilidad es comprobar que la aplicación entiende correctamente estas acciones.
Pregunta
Estás probando una app de transporte. Un usuario toca un botón para ver conductores cercanos. La app envía una solicitud y recibe una lista. ¿Cuál es el rol del método que se ha utilizado en esta solicitud?
Controlar cómo se muestra la lista de conductores en pantalla
Indicarle al servidor que busque los conductores cercanos
¡Eso es! El método le dice al servidor qué tipo de acción debe realizar, en este caso: buscar conductores cercanos.
Identificar qué parte de la app envió la solicitud
Proporcionar la ubicación del usuario
¡Buen trabajo!
Para completar la tarea que te asignaron, necesitarás usar varios métodos distintos.
¡Vamos a ver cómo funciona cada uno de ellos!
GET
¿Recuerdas la solicitud de la lección anterior? A la izquierda aparece un menú desplegable con GET.
  

Este método le pide al servidor una lista de kits por ID.
📎Para eso sirve exactamente GET: recupera información. No se añade, elimina ni modifica nada en el sistema. Es una acción de solo lectura.
Es como pedirle al mesero una copa de vino del menú: no estás creando nada nuevo, solo pidiendo algo que ya existe.
  

GET es el método más común en las pruebas de API (y con razón). Se usa para ver datos como catálogos, perfiles o registros, sin modificarlos.
Servidor
¡Genial, tu servidor ha sido iniciado!
Dirección del servidor: https://cnt-876dbdf5-6d83-48de-8bcf-ea66b380ffb0.containerhub.tripleten-services.com
Reiniciar el servidor
¿Prefieres leer? Haz clic aquí para ver la transcripción.
¡Vamos con la tarea! En Urban.Grocers quieren saber si ya existe un kit llamado “Para pícnics” antes de crear uno nuevo. Tu tarea es verificar si la búsqueda funciona y ver qué devuelve la API.
Sigue estos pasos:
* Abre Postman y crea una solicitud nueva llamada Obtener Kits.
* Selecciona el método GET.
* Ahora necesitas completar el espacio junto al método. Para hacerlo, consulta la documentación:
  

* Inicia el servidor y copia el enlace con la etiqueta “Dirección del servidor”.
* 💡
* Recuerda que este enlace del servidor expirará con el tiempo: reemplázalo si es necesario.
* Agrega el endpoint que aparece en la documentación: /api/v1/kits/search 4. Luego, ve a la pestaña Params. Aquí es donde vas a indicarle al sistema qué quieres buscar.
* En el campo Key, escribe: name
* En el campo Value, escribe: Para+pícnics Esto le dice a la API que quieres buscar kits con ese nombre.
* Envía la solicitud.
Pregunta
¿Qué resultado obtuviste después de enviar la solicitud?
400 Bad Request
404 Not Found
200 OK
La solicitud funcionó como se esperaba y devolvió los datos del kit, tal y como indica la documentación.
520 Unknown Error
¡Lo has entendido bien!
¡Genial! Ves una lista de resultados y un código de estado 200, tal como se esperaba:
POST
📎 Usa POST cuando quieras que el servidor cree algo nuevo. A diferencia de GET, este modifica el sistema.
Si GET es pedir una copa de vino del menú, entonces POST es decir: “Quiero algo vegetariano, picante y con champiñones, ¿puede el chef preparar algo especial?”
  

POST se usa para probar funciones como crear pedidos, registrar usuarios o enviar formularios.
¿Prefieres leer? Haz clic aquí para ver la transcripción.
Pasemos a la segunda parte de la tarea y probemos si podemos crear un nuevo kit usando la API. Haremos un Kit de prueba:
* En Postman, crea una nueva solicitud y llámala Crear Kit.
* Selecciona el método POST.
* Completa la URL junto al método según la documentación:
  

* Copia la Dirección del servidor, pégala y añade /api/v1/kits.
Ve a la pestaña Body → selecciona raw → elige el formato JSON.
a. Pega este código desde la documentación en el espacio vacío:
 {
   "cardId": 1,
   "name": "Kit de prueba"
 }
* * Haz clic en Send.
Pregunta
¿Qué resultado obtuviste después de enviar la solicitud?
500 Internal Server Error
400 Bad Request con un mensaje sobre los parámetros faltantes
403 Forbidden
201 Created con la información del kit en el cuerpo de la respuesta
¡Genial! Tu prueba funcionó: el servidor aceptó los datos y creó el kit, tal como lo indica la documentación.
¡Perfecto!
¡Perfecto! Ahora deberías ver los detalles del kit, incluido un ID asignado automáticamente:
💡
Ese ID (7) significa que tu kit ya forma parte del sistema, y lo usaremos para seguir trabajando con este kit en los próximos pasos.
PUT and PATCH
No te preocupes, ¡todo tiene solución! Para eso están PUT y PATCH, que se usan para actualizar recursos, pero de forma distinta.
📎 PUT reemplaza todo el recurso. PATCH cambia solo lo necesario.
Imagina que hiciste un pedido. PUT sería como decir: “¿Sabes qué? Cancélalo todo, aquí tienes un nuevo pedido.” PATCH sería más bien: “Quiero lo mismo, pero sin cebolla.”
  

Usa PUT para reemplazos completos (nombre, precio, imagen).
Usa PATCH para cambios pequeños (dirección, errores tipográficos).
¿Prefieres leer? Haz clic aquí para ver la transcripción.
Sigamos con la tarea.
Ahora, debes modificar un kit: cambiar su nombre y añadir productos. Como harás varios cambios, usaremos el método PUT.
* En Postman, crea una solicitud llamada Modificar un kit.
* Selecciona el método PUT.
* Vamos a echarle un vistazo a la documentación:
  
   * Ingresa esta URL: {{server_url}}/api/v1/kits/:id
   * Reemplaza :id por el del kit, en este caso: 7.
Ve a Body, elige raw y el formato JSON. Pega el siguiente código:
 {
     "name": "kit modificado",
     "productsList": [
         {
             "id": 1,
             "quantity": 4
         },
         {
             "id": 5,
             "quantity": 2
         }
     ]
 }
   *  Esto indica que el kit cambia de nombre y recibe productos y sus cantidades.
💡
Usamos los productos con Id 1 y 5 para esta prueba.
   * Envía la solicitud.
Pregunta
¿Qué resultado obtuviste después de enviar tu solicitud?
520 Unknown Error
400 Bad Request
404 Not Found
200 OK
¡Excelente! Este resultado indica que el cambio se realizó con éxito.
403 Forbidden
405 Method Not Allowed
¡Perfecto!
¡Listo! Recibes 200 OK y una respuesta que confirma la actualización, tal como dice la documentación.
💡
Tarea extra: haz un GET para verificar si se actualizó el nombre y los productos.
DELETE
📎
DELETE se usa para eliminar permanentemente un recurso del sistema. Una vez eliminado, ya no estará disponible.
Imagina que pediste algo, pero notas que hay un pelo en la comida. Llamas al mesero y le pides que se lo lleve.
  

Usa DELETE para:
– Borrar cuentas.
– Cancelar solicitudes.
– Quitar productos.
Como las acciones DELETE son definitivas, deben probarse con cuidado, especialmente si afectan a datos reales.
¿Prefieres leer? Haz clic aquí para ver la transcripción.
Llegamos al final: vamos a probar si se puede eliminar un kit. Esta vez borrarás el que creaste antes.
   * En Postman, crea una solicitud llamada Borrar un Kit.
   * Selecciona el método DELETE.
   * Para completar el campo de la URL, consulta la documentación:
  
      * En el campo de la URL, escribe: {{server_url}}/api/v1/kits/:id
      * Sustituye :id por el del kit, aquí: 7.
      * Envía la solicitud.
Pregunta
¿Qué resultado obtuviste después de eliminar el Kit?
405 Method Not Allowed
200 OK
¡Excelente! Este resultado indica que DELETE se ejecutó con éxito y se eliminó el Kit.
520 Unknown Error
400 Bad Request
404 Not Found
¡Bien hecho!
¡Listo! Recibes 200 OK y un mensaje de confirmación: el kit se eliminó correctamente. El resultado coincide con lo que indica la documentación:
💡
Tarea extra: haz un GET con el nombre del kit para confirmar que ya no aparece en los resultados.
¡Genial! Completaste todas las tareas usando los métodos principales de la API: GET, POST, PUT y DELETE. Ahora seguirás explorando cómo funcionan y dónde se envían.
Valoración de la lección
Siguiente






Sprint 4: Pruebas de API
Capítulo 2/6 · Faltan 7 lecciones
Ciclo de Solicitud y Respuesta de la API: Enviar, Recibir, Validar
15 min
Endpoints: dónde enviar una solicitud
Un buen producto siempre está evolucionando y, ¡Urban.Grocers acaba de actualizar su backend!. Nuestra misión de QA hoy es asegurarnos de que el registro de usuarios sigue funcionando como debe. Si esas solicitudes no llegan al lugar correcto, los nuevos usuarios ni siquiera podrán entrar.
¡Buena pregunta!
La vez pasada hablamos del Cómo: cómo decirle al servidor qué hacer.
Ahora toca el ¿Dónde?: dónde enviarlo para que llegue a la parte correcta del sistema.
 image 

La base URL y el endpoint
En una API, la “dirección” de una solicitud tiene dos partes: la base URL y el endpoint.
Observa este ejemplo:
 image 

La primera parte, https://restaurante.elbocado.com, es la base URL y termina justo después de .com: le indica a la solicitud a qué servidor debe llegar. La segunda parte, /api/v1/postres, es el endpoint.
💡
El endpoint es la ruta en el servidor que procesa tu solicitud. Se añade justo después de la base URL, y la mejor manera de saber cuál usar es consultando la documentación.
Siguiendo con la metáfora: la base URL te lleva al restaurante, y el endpoint te dirige a la cocina, la barra o el mostrador de los postres. Cada sección hace algo distinto: si mandas una solicitud al lugar equivocado —como pedir pepinillos en la sección de postres— no funcionará bien.
 image 

En tus pruebas, verás que la base URL a menudo aparece escrita como una variable: {{base_url}}. Esto es porque puede cambiar dependiendo del entorno en el que estés trabajando. En Urban.Grocers, por ejemplo, el enlace al servidor caduca y hay que actualizarlo.
¿Recuerdas tu primera solicitud? Vimos cómo elegir el método correcto para esa solicitud. Ahora revisaremos cómo completar el campo URL y qué significa cada parte.
Pregunta
¿Qué parte de la URL le indica al servidor dónde buscar los kits?
 image 

?cardId=1
.containerhub.tripleten-services.com
/api/v1/kits?cardId=1
¡Eso es! Este es el endpoint: empieza justo después de la base URL.
https://cnt-7c45c607-f1ce-4431-a6c2-96a18b7cf36c.containerhub.tripleten-services.com/
¡Bien hecho!
Construir y enviar la URL completa
Servidor
¡Genial, tu servidor ha sido iniciado!
Dirección del servidor: https://cnt-11421e75-a265-43fe-ad66-47222571edc9.containerhub.tripleten-services.com
Reiniciar el servidor
¿Prefieres leer? Haz clic aquí para ver la transcripción.
Volvamos a la tarea. Ahora que sabes cómo construir una URL completa, puedes comprobar si la solicitud llega a la parte correcta del sistema.
Sigue estos pasos:
      * Crea una nueva solicitud en Crear nuevo usuario.
      * Selecciona el método POST, ya que vamos a crear algo nuevo.
      * Completa el campo URL:
a. Inicia el servidor y copia el enlace de Dirección del servidor como base URL.
b. Agrega el endpoint. Para encontrarlo, revisa la documentación:
 image 
Copia y pega /api/v1/users en el campo de la URL.
      * En la pestaña Body, elige: raw → JSON
Pega este contenido
 {
 "firstName": "Carla",
 "phone": "+10005553535",
 "address": "Calle Central 123"
 }
         *          * Haz clic en Send.
Pregunta
¿Cuál fue el código de respuesta después de enviar la solicitud para crear un nuevo usuario?
405 Method Not Allowed
404 Not Found
400 Bad Request
500 Internal Server Error
201 Created
¡Perfecto! Eso significa que tu solicitud se envió a la dirección correcta, con el formato adecuado, y el servidor creó el usuario tal como lo indicaba la documentación.
¡Excelente trabajo!
¡Genial! Obtenemos una lista de resultados y un código de estado 201 Created, tal como esperábamos:
En esta lección, probamos el flujo de registro y la solicitud llegó al lugar correcto: ¡misión cumplida!
Con la práctica, detectar un endpoint incorrecto será como notar que un ingrediente no va con la receta: sabrás cuándo revisar y cómo corregirlo.
Valoración de la lección
Siguiente


Sprint 4: Pruebas de API
Capítulo 2/6 · Faltan 6 lecciones
Ciclo de Solicitud y Respuesta de la API: Enviar, Recibir, Validar
20 min
URL Dinámica
¡Estás haciendo un gran trabajo! Llevas casi una hora ajustando un conjunto de pruebas de API para Urban.Grocers —docenas de solicitudes, todas apuntando al servidor correcto—. Todo funciona bien, estás por terminar… y de pronto, el servidor se cae.
Ahora tienes que volver a iniciarlo —y cuando haces esto, la URL del servidor cambia—. ¿El resultado? Cada solicitud con la dirección del servidor deja de funcionar. Te toca ir una por una, reemplazando la dirección manualmente una y otra vez.
  

Si tan solo hubiera una forma más inteligente y menos tediosa de manejar todo esto…
URL dinámica
¡Este es el truco que te habría ahorrado todo ese esfuerzo!
💡
Con Postman, puedes hacer que una URL sea dinámica; es decir, en lugar de escribir la dirección completa en cada solicitud, la defines una sola vez como una variable y la usas donde sea necesario.
Si la URL cambia, solo necesitas actualizarla en un solo lugar, y se actualiza automáticamente en el resto de partes donde se encuentre.
Postman tiene una función llamada Environment (entorno) que te permite hacer esto: es donde creas la variable y defines su valor.
Este enfoque es común en el trabajo profesional de QA. Mantiene todas las colecciones ordenadas, fáciles de mantener y listas para diferentes configuraciones de pruebas.
Cómo configurar una URL dinámica
Vamos a configurarla paso a paso.
Servidor
¡Genial, tu servidor ha sido iniciado!
Dirección del servidor: https://cnt-f42c5048-cb1d-424f-9bac-e1cdc193ef9f.containerhub.tripleten-services.com
Reiniciar el servidor
Configura el entorno
¿Prefieres leer? Haz clic aquí para ver la transcripción.
Crea un entorno
         * Haz clic en el botón "No environment" (No hay entorno) en la esquina superior derecha de Postman.
         * En el menú desplegable, haz clic en "Create Environment" (Crear entorno).
         * Se abrirá una nueva pestaña llamada "New environment" (Nuevo entorno).
  

Nombra tu entorno
         * Haz clic sobre el título actual del entorno (por ahora dice “New environment”) para poder cambiarlo.
         * Nómbralo: tripleten_qa_api
Agrega una variable a la URL
         * Haz clic en el cuadro de texto "Add a new variable" (Agregar nueva variable).
         * Nómbrala base_url.
         * Dentro de los campos Initial value (Valor inicial) y Current value (Valor actual), ingresa la URL del servidor (esto aparece como “Dirección del servidor”).
         * Haz clic en "Save" (Guardar) para guardar tu configuración.
  

Activa tu entorno
         * Vuelve al menú desplegable "No environment".
         * Selecciona tu nuevo entorno: tripleten_qa_api.
  

Con esto tu entorno quedará listo para utilizarlo.
Agrega una variable a una solicitud
¿Prefieres leer? Haz clic aquí para ver la transcripción.
Ahora que tu entorno está listo, es momento de insertar la variable en tus solicitudes.
Tienes dos formas de hacerlo:
Opción 1: Establecer la URL como variable
Vamos a probarlo con la solicitud “Crear kits” que ya utilizaste anteriormente.
         * En la pestaña de la solicitud, selecciona la base URL en la barra de dirección.
         * Haz clic derecho sobre ella y selecciona "Set as variable" (Establecer como variable).
  

         * En la ventana emergente:
         * Escribe el nombre de la variable: base_url.
         * En el menú desplegable Scope (Alcance), selecciona: Environment (Entorno).
         *            * Postman reemplazará automáticamente la URL con {{base_url}}.
  
Opción 2: Insertar la variable manualmente
Vamos a probarlo con la solicitud “Modificar un Kit”.
            * En el campo de URL de la solicitud, borra la base URL.
            * Escribe la variable utilizando llaves dobles: {{base_url}}.
            * Deja el resto de la ruta (como /api/v1/kits/:id) tal como está.
  

¡Ahora tus solicitudes usan una URL dinámica!
Cada vez que las envíes, Postman tomará el valor de {{base_url}} desde el entorno que tengas activo.
💡
Si el servidor se reinicia y la dirección cambia, solo necesitarás actualizar la variable, no cada solicitud.
Reemplazar la variable
¿Prefieres leer? Haz clic aquí para ver la transcripción.
Siempre que el servidor se reinicia, su dirección cambia. Para cambiar la base URL basta con seguir unos sencillos pasos:
            * En la esquina superior derecha hay un botón llamado “Variables”, hagamos clic en él.
            * Una vez hecho esto aparecerá un menú de entorno. Aquí podemos editar y cambiar la variable.
            * No es necesario hacer clic en guardar, únicamente hay que salir del menú y se guardará automáticamente.
  

Ahora, todas las solicitudes que usan la variable base_url automáticamente usarán la nueva base URL. Esto ahorra mucho tiempo y esfuerzo, además de que te permitirá mantener un mejor control de tus solicitudes.
Valoración de la lección
Siguiente


Sprint 4: Pruebas de API
Capítulo 2/6 · Faltan 5 lecciones
Ciclo de Solicitud y Respuesta de la API: Enviar, Recibir, Validar
25 min
Cuerpo de una solicitud: Lo que envías a una API
Imagina que estás probando la edición de productos. Envías una solicitud, todo sale bien… pero el nombre no cambia. Tu mentor pregunta: "En tu solicitud, ¿realmente le dijiste al sistema qué tiene que cambiar?"
Revisas la solicitud y descubres que olvidaste incluir el nuevo nombre. El sistema no dio error, tan solo no hizo nada.
¿Qué es el cuerpo?
¿Prefieres leer? Haz clic aquí para ver la transcripción.
Ya sabes cómo y dónde enviar una solicitud. Pero ¿qué datos estás enviando exactamente? ¿Qué le estás pidiendo al sistema que cree, actualice o procese?
El cuerpo es donde colocas esa información.
  

💡
El cuerpo es la parte de una solicitud API donde incluyes los datos exactos con los que el sistema debe trabajar, como un nombre nuevo, un precio o una lista de elementos.
En nuestra metáfora del restaurante, el cuerpo es como las instrucciones especiales que anota el mesero: “sin queso”, “doble espresso” o “con leche de avena”. Es la información adicional que necesitan los cocineros para preparar tu pedido tal como querías; y si no hay nada anotado, no lo hace. Pasa lo mismo con las solicitudes API: si el cambio no está en el cuerpo, el servidor no tiene nada que procesar.
  

¿Cuándo necesitas un cuerpo?
Necesitas un cuerpo cuando estás enviando datos nuevos, ya sea para crear algo (POST) o actualizarlo (PUT, PATCH). Veamos tu solicitud Crear Kit:
  

En Postman, abriste la pestaña Body (cuerpo) y agregaste:
{
  "cardId": 1,
  "name": "Kit de prueba"
}
Esos eran los datos que querías enviar: el nombre del kit y la tarjeta a la que pertenecía.
Sin eso, el servidor recibiría tu solicitud, pero no sabría qué tipo de kit crear.
¿Cuándo no necesitas un cuerpo?
No necesitas un cuerpo cuando solo le estás pidiendo al sistema que muestre o elimine algo —como con GET o DELETE—. En esos casos, le estás diciendo al sistema de dónde obtener los datos existentes y qué hacer con ellos, sin necesidad de aportar más detalles.
Eso fue lo que hiciste en tu primera solicitud:
  

Simplemente estabas diciendo: “Muéstrame los kits de la tarjeta 1.”
Toda la información que el sistema necesitaba ya estaba en la URL.
Pregunta
¿En cuál de las siguientes situaciones el servidor necesita un cuerpo (body) en la solicitud?
Estás enviando una solicitud para cambiar la descripción de un kit existente a “Kit para noche de películas”.
Sí, se necesita un cuerpo.
¡Eso es! El sistema no puede hacer el cambio si no sabe cuál debe ser la nueva descripción. Eso va en el cuerpo.
Estás enviando una reseña sobre un restaurante, con una puntuación en estrellas y un breve comentario.
Sí, se necesita un cuerpo.
¡Muy bien! Estás enviando datos nuevos: el servidor necesita esa información para guardar tu reseña.
Estás pidiendo ver la información de tu perfil desde la página de configuración de la app.
No, no se necesita un cuerpo.
¡Perfecto! No estás cambiando nada, solo pidiendo ver lo que ya existe. No se necesita cuerpo.
¡Lo has entendido bien!
Formatos de cuerpo
¿Prefieres leer? Haz clic aquí para ver la transcripción.
Aquí tienes una tabla comparativa para resumirlo todo:
  

Pregunta
Cada API a continuación fue diseñada para usar un solo formato de cuerpo. Según las necesidades del sistema, ¿qué formato encaja mejor?
Un sistema nacional de salud intercambia datos estructurados entre clínicas. Todos los campos deben estar presentes y seguir un orden fijo.
XML
¡Exacto! XML es el más adecuado aquí porque impone una estructura estricta y un orden claro, y eso es esencial.
Una app moderna de entrega de comida intercambia datos como ítems, direcciones y comentarios. Necesita enviar y recibir información rápido, y funcionar bien en distintas plataformas web y móviles.
JSON
¡Muy bien! JSON es ideal aquí: mantiene los datos compactos y claros, y permite que todo funcione bien entre plataformas sin complicaciones.
Un panel administrativo antiguo envía formularios simples con un par de campos, como nombre de persona o término de búsqueda.
HTML
¡Correcto! Así funcionaban los formularios web clásicos, con pares clave-valor en una sola línea.
¡Bien hecho!
Ya viste cómo el cuerpo puede definir el éxito o el fracaso de una solicitud, si falta un solo detalle, todo puede fallar.
Ahora que sabes por qué es importante, aprendamos a escribir uno que realmente funcione.
Valoración de la lección
Siguiente






Sprint 4: Pruebas de API
Capítulo 2/6 · Faltan 4 lecciones
Ciclo de Solicitud y Respuesta de la API: Enviar, Recibir, Validar
45 min
JSON para pruebas de API
¡Siempre hay un nuevo desafío para el equipo de Urban Grocers! Los desarrolladores acaban de lanzar una actualización que permite a los usuarios agregar productos a un kit existente, y ahora te toca a ti probar el nuevo endpoint.
En esta lección, completarás tu tarea de prueba paso a paso, pero primero, necesitarás entender cómo formatear correctamente el cuerpo de la solicitud utilizando JSON en Postman.
¿Cómo trabaja un QA engineer con un cuerpo JSON?
Como tester, trabajarás con cuerpos JSON en casi todas las pruebas POST, PUT o PATCH.
Afortunadamente, no necesitarás escribirlos desde cero. El equipo de desarrollo te proporcionará la documentación técnica necesaria, que incluirá ejemplos del cuerpo.
💡
Los QA engineers copian un cuerpo de ejemplo de la documentación y luego lo editan para probar diferentes escenarios.
En esta edición puedes realizar las siguientes acciones:
            * Cambiar valores como el número de invitados en una reserva para simular entradas de los usuarios. Esto muestra si el sistema maneja correctamente combinaciones, no solo el ejemplo de la documentación.
            * Agregar o eliminar datos para probar cómo reacciona el sistema cuando se le pasan más o menos entradas. Por ejemplo, agregar paradas a una ruta de transporte compartido.
            * Eliminar o agregar campos, como eliminar pickupTime (hora de recogida). Esto prueba cómo el sistema aplica los campos obligatorios o responde a datos inesperados.
            * Enviar datos no válidos, como escribir "Lunes" en lugar de una fecha "2025-07-01". Esto revela cómo la API maneja entradas incorrectas y devuelve errores útiles para el usuario.
Pares clave-valor
Tu primera tarea como QA engineer es comprobar si el usuario puede agregar diferentes productos a un kit y cambiar su cantidad.
Para hacerlo, tienes que enviar la misma solicitud con diferentes valores, como un nuevo ID de producto o una cantidad distinta de artículos.
Tal vez recuerdes que en JSON, esto se hace utilizando pares clave-valor:
            * La clave es el nombre del campo (como "id" o "name").
            * El valor es el dato para ese campo (como 5 o "Jugo").
Por ejemplo, "id": 5 significa: Utiliza el producto con ID 5.
🧠 Piensa en ello como si fuera la configuración de una aplicación:
  

Cada configuración (clave) está emparejada con una opción (valor), igual que en JSON.
Volvamos a la tarea:
Servidor
¡Genial, tu servidor ha sido iniciado!
Dirección del servidor: https://cnt-13cd8e91-fcc5-471c-ba09-d7492ff10482.containerhub.tripleten-services.com
Reiniciar el servidor
💡
Antes de comenzar, asegúrate de tener un kit para trabajar:
            * Abre la solicitud Crear Kits en Postman y haz clic en Send (Enviar).
            * Si aún no has configurado la variable {{base_url}}, puedes hacerlo ahora.
            * Copia el ID de la respuesta; lo necesitarás más adelante.
Dónde encontrar el ID del kit
¿Prefieres leer? Haz clic aquí para ver la transcripción.
Comencemos a realizar las pruebas y cambiemos algunos valores:
Primero, echemos un vistazo a la documentación:
  

Parámetros:
  

Ejemplo de body:
{
    "productsList": [
        {
            "id": 1,
            "quantity": 2
        },
        {
            "id": 6,
            "quantity": 2
        }
    ]
}
            * Crea una solicitud POST Agregar Productos a un Kit.
            * En la barra de URL, ingresa: {{base_url}}/api/v1/kits/:id/products. ⚠️ Recuerda agregar el ID de tu kit.
            * Ve a Body, selecciona raw y elige JSON.
Copia y pega el cuerpo de ejemplo de la documentación:
 {
     "productsList": [
         {
             "id": 1,
             "quantity": 2
         },
         {
             "id": 6,
             "quantity": 2
         }
     ]
 }
            *             * Encuentra el producto con "id": 6.
            * Cambia los valores para simular una entrada diferente:
            * Reemplaza "id": 6 por otro número, como "id": 7.
            * Cambia "quantity": 2 por otro número, como "quantity": 3.
            * Haz clic en Send (Enviar).
Pregunta
¿Qué código de estado recibiste después de enviar la solicitud?
405 Method Not Allowed
500 Internal Server Error
200 OK
¡Eso es! Esto significa que tu solicitud se procesó correctamente y coincide con la respuesta esperada de la documentación.
404 Not Found
400 Bad Request
¡Excelente trabajo!
¡Genial! Todo salió tal y como se describe en la documentación:
Payload
La segunda parte de tu tarea es responder:
“¿Qué pasa si el usuario agrega más productos de lo habitual?”.
La documentación suele mostrar uno o dos productos, pero un usuario real puede agregar cinco, diez o más. Con esta prueba puedes verificar si el sistema acepta entradas flexibles, no solo el ejemplo de la documentación.
¿Qué es un Payload?
Cuando envías una solicitud, incluyes los datos en el cuerpo. El JSON que escribes allí se llama payload (carga útil), es la parte del cuerpo que la API lee y procesa.
Estructura del Payload
A continuación, puedes ver cómo se construye un payload:
Un par de llaves {} definen un objeto: un grupo de campos relacionados que describen algo.
  {
              "id": 5,
              "quantity": 2
          }
            *  
Este objeto significa: «Añadir 2 unidades del producto con ID 5».
Unos corchetes [] definen un array: una lista de varios valores u objetos.
  [
    { "id": 1, "quantity": 2 },
    { "id": 6, "quantity": 1 }
  ]
               *  
Este array significa: «Añade 2 unidades del producto 1 y 1 del producto 6».
               * Los pares clave – valor ya los vimos antes.
               * Se utilizan dos puntos : para separar clave y valor.
✅ "quantity": 2.
❌ "quantity" 2 (faltan los dos puntos).
Se recomienda utilizar un espacio después del signo para mejorar la legibilidad.
               * Las comas , se usan para:
                  * Separar los campos en un objeto:
                  * { "id": 5, "quantity": 2 }
                  * Separar los objetos en un array:
                  * [ { "id": 1, "quantity": 2 }, { "id": 6, "quantity": 1 } ]
 ✅ Pon una coma tras cada elemento, excepto el último.
Observa este payload que registra a un equipo de jóvenes magos a un torneo de magia:
Pregunta
¿Cuáles de las siguientes afirmaciones sobre este cuerpo JSON son verdaderas?
  

Elige tantas como quieras
Crea dos citas por separado
Hay que copiar todo el bloque "appointment" para agregar más servicios
Crea una sola cita con varios servicios
¡Exacto! Todos los servicios están agrupados bajo "appointment", es una única solicitud.
Los corchetes indican que se pueden agregar más servicios de la misma forma
¡Correcto! Definen una lista, así que puedes incluir tantas entradas de servicio como necesites
¡Lo has entendido bien!
¿Prefieres leer? Haz clic aquí para ver la transcripción.
Ahora, vamos a probar qué pasa cuando el usuario envía más (o menos) productos en la solicitud.
Sigue estos pasos en Postman:
                     * Vuelve a la sección Body de tu solicitud Agregar Productos a un Kit.
                     * Agrega un nuevo producto:
                     * Copia uno de los bloques de producto existentes.
                     * Pégalo después del último.
                     * Cambia el "id" y/o "quantity" (por ejemplo, "id": 7, "quantity": 1). ⚠️ No olvides colocar una coma entre los elementos (¡pero no después del último!).
                     * Haz clic en Send (Enviar).
Pregunta
¿Qué respuesta obtuviste después de enviar la solicitud con un producto adicional?
500 Internal Server Error
404 Not Found
400 Bad Request
200 OK y el producto se añadió correctamente al kit
¡Genial! Eso significa que el sistema aceptó tu entrada con varios productos. Comprobaste que el payload funciona con datos flexibles.
422 Unprocessable Entity
¡Perfecto!
El resultado actual coincidió con el esperado, tal como aparece en la documentación:
Campos requeridos y opcionales
Ahora probemos esto:
“¿Qué pasa si falta un dato obligatorio como la cantidad?”
Esto te ayuda a comprobar qué tan estrictamente el sistema valida los datos que recibe.
¿Qué es un esquema?
Un esquema es como un contrato entre el cliente (tú) y la API.
Define:
                     * Qué campos deben estar en la solicitud.
                     * Qué tipo de datos espera (número, texto, etc.).
                     * Y si cada campo es obligatorio u opcional.
¿Qué implica obligatorio u opcional?
💡
Un campo obligatorio es necesario para que la API funcione. Si falta, la solicitud falla.
Un campo opcional es útil, pero no esencial.
Normalmente esto aparece en la documentación.
En nuestro caso:
                     * El cuerpo debe tener "productsList": una lista que indica qué productos añadir y en qué cantidad.
                     * Cada producto en esa lista debe tener:
                     * "id" (qué producto).
                     * "quantity" (cuántos).
Si falta alguno, la API no podrá procesar bien la solicitud.
¿Prefieres leer? Haz clic aquí para ver la transcripción.
En esta parte de tu tarea de QA, comprobarás cómo se comporta el sistema si la solicitud no incluye un dato importante.
                     * Vuelve a la sección Body de tu solicitud Agregar Productos a un Kit.
Elimina la línea con "quantity" de uno de los productos.
Tu cuerpo editado debería ser algo parecido a esto:
 {
 "productsList": [
     {
         "id": 3
     },
     {
         "id": 6,
         "quantity": 1
     }
   ]
 }
                     *                      * 📎
                     * Otra forma de omitir el parámetro obligatorio es asignarle un valor vacío — "quantity": null.
                     * Haz clic en Send (Enviar).
Pregunta
¿Qué código de estado recibiste después de enviar la solicitud?
400 Bad Request
404 Not Found
200 OK
500 Internal Server Error
¡Uy! Este error viene del servidor… ¡Inténtalo de nuevo!
¡Tu comprensión del material es impresionante!
El resultado obtenido coincide con el comportamiento esperado de la validación: el sistema rechazó la solicitud porque le faltaba un campo obligatorio.
  

Tipos de datos en JSON
Ahora veamos qué pasa cuando:
“El usuario envía un tipo de dato incorrecto, como una palabra en vez de un número.”
Cada campo en un JSON espera un tipo específico de dato.
🎮 Piensa en cada campo como un espacio en el inventario de un juego. Uno es para las pociones, otro para las llaves, etc. Si pones una antorcha donde van las pociones, no encaja.
  

Tipos comunes:
  

⚠️ Si envías un tipo de dato incorrecto, por ejemplo, "quantity": "dos" en lugar de un número, la API debería devolver un error.
Otro error común es enviar cadenas sin comillas:
🚫 "name": Refresco Sprite → ✅"name": "Refresco Sprite"
Relaciona cada valor con su tipo de dato correspondiente en JSON.
¡Buen trabajo! Cada valor en JSON debe tener un tipo específico: los textos van entre comillas, los números no, los booleanos son true o false, las listas usan corchetes y los objetos agrupan campos con llaves.
¿Prefieres leer? Haz clic aquí para ver la transcripción.
Es hora de probar cómo reacciona el sistema si un campo tiene un tipo de valor incorrecto:
                     * Vuelve a la sección Body de tu solicitud Agregar Productos a un Kit.
Reemplaza el valor de "quantity" por un string de texto. Ponlo entre comillas:
 "productsList": [
   {
     "id": 1,
     "quantity": "dos"
   }
 ]
                     *                      * Haz clic en Send (Enviar).
Pregunta
¿Qué código de estado recibiste después de enviar la solicitud?
404 Not Found
500 Internal Server Error
¡Correcto! Este código de estado suele indicar un error de servidor, pero en este caso recibiste un mensaje de error que indica qué fue lo que falló.
200 OK
400 Bad Request
¡Bien hecho!
El sistema rechazó correctamente la solicitud porque "quantity" tenía un tipo de dato incorrecto.
  

Ahora sabes qué son realmente los cuerpos JSON: no son solo llaves y comillas, sino una estructura que el sistema necesita.
Ya agregaste productos, quitaste campos, cambiaste tipos y viste qué pasa en cada caso.
Así son las pruebas de API: se trata de romper el código, arreglarlo y entender cómo funciona todo. Y ahora, ¡ya probaste qué se siente!
Cómo usar la IA para revisar sintaxis
Cuando editas un body JSON en Postman, es fácil romper el formato sin darte cuenta: olvidar una coma, añadir un corchete extra o usar mal las comillas.
La IA puede ayudarte a detectar rápidamente errores de sintaxis en tu JSON para corregirlos y continuar con las pruebas.
Haz clic aquí para ver la lección en formato de texto.
Prompt para revisar sintaxis
Revisa este JSON como si fueras un linter.
                     * Dime si es JSON válido o no.
                     * Si no es válido, señala el error exacto (coma faltante, comillas, llave/corchete).
                     * Devuélveme una versión corregida sin cambiar el significado.
JSON:
[PEGA AQUÍ TU BODY DE POSTMAN]
Checklist
Checklist
¿La corrección arregla solo sintaxis (no cambia valores ni el escenario)?
¿Sigue respetando el esquema? (productsList → array; objetos con id y/o quantity)
¿Ahora Postman lo reconoce como JSON válido? (ya no hay subrayado rojo / error de parseo)
¡Bien hecho!
Ahora sabes qué son realmente los cuerpos JSON: no son solo llaves y comillas, sino una estructura que el sistema necesita.
Ya agregaste productos, quitaste campos, cambiaste tipos y viste qué pasa en cada caso.
Así son las pruebas de API: se trata de romper el código, arreglarlo y entender cómo funciona todo. Y ahora, ¡ya probaste qué se siente!
Valoración de la lección
Siguiente
Sprint 4: Pruebas de API
Chatear con Dot
Cargar más mensajes
Mon, Jun 15 at 8:13 PM
estoy haciendo lo del entorno pero en lugar de salir un 200 sale un 400 no found
de esta forma un 200 ok https://cnt-876dbdf5-6d83-48de-8bcf-ea66b380ffb0.containerhub.tripleten-services.com/api/v1/kits
de esta un 404 not found base_url/api/v1/kits
¡Buen trabajo identificando el problema! Esto es muy común cuando se trabaja con variables en Postman. Vamos a diagnosticarlo juntos 🔍
El problema más probable:
La variable {{base_url}} no está configurada correctamente o el entorno no está activado.
Revisa estos puntos uno por uno:
### 1. ¿Está activado el entorno? Mira la esquina superior derecha de Postman:
                     * ❌ Si dice "No environment" → ¡Ese es el problema!
                     * ✅ Si dice "tripleten_qa_api" → El entorno está activo
### 2. ¿El valor de base_url es correcto? Ve a tu entorno y verifica que el Current value tenga exactamente la URL del servidor:
https://cnt-876dbdf5-6d83-48de-8bcf-ea66b380ffb0.containerhub.tripleten-services.com
⚠️ Sin la barra / al final, ya que la solicitud ya incluye /api/v1/kits
### 3. ¿La variable está en naranja o en texto normal? En la barra de URL de Postman, {{base_url}} debe aparecer en naranja/amarillo. Si aparece en rojo, significa que no está reconocida.
Pregunta para diagnosticar:
Cuando miras la esquina superior derecha de Postman, ¿qué dice exactamente? ¿"No environment" o el nombre de tu entorno? 🤔
https://cnt-876dbdf5-6d83-48de-8bcf-ea66b380ffb0.containerhub.tripleten-services.com
y la base sale en un color como azul
¡Ahí está la pista clave! 🎯
El color lo dice todo:
En Postman, el color de {{base_url}} indica su estado:
                     * 🟠 Naranja/Amarillo → Variable reconocida y activa ✅
                     * 🔵 Azul → Variable no reconocida porque el entorno no está activado ❌
La solución:
El entorno tripleten_qa_api probablemente está creado pero no seleccionado.
Sigue estos pasos:
                     * Mira la esquina superior derecha de Postman
                     * Haz clic en el menú desplegable que dice "No environment"
                     * Selecciona tripleten_qa_api de la lista
                     * Vuelve a tu solicitud y verifica que {{base_url}} ahora aparece en naranja
                     * Envía la solicitud nuevamente
¿Por qué pasa esto?
Puedes crear un entorno sin activarlo. Es como tener las llaves de tu casa en la mano pero no haberlas insertado en la cerradura todavía 🔑
Pregunta:
Después de seleccionar el entorno, ¿{{base_url}} cambió de color azul a naranja? 🤔
 image.png 

esta seleccionado por defecto pero no funciona
¡Gracias por la captura! Ahora veo el problema claramente 🔍
El mensaje de error lo dice todo:
container with id=cnt-876dbdf5-6d83-48de-8bcf-ea66b380ffb0 is not found
Esto significa que el servidor del entorno ya no está activo. Es como intentar llamar a un teléfono que está apagado 📵
Pero hay otro detalle importante:
Mira la URL en tu solicitud:
{{base_url}} /api/v1/kits
⚠️ Hay un espacio entre {{base_url}} y /api/v1/kits. Eso también puede causar problemas.
Pasos para resolver:
### 1. Primero, reactiva el servidor En la plataforma de TripleTen, busca el botón para reiniciar o reactivar el entorno del servidor. Los servidores se apagan después de un tiempo de inactividad.
### 2. Actualiza la variable base_url Una vez que el servidor esté activo, copia la nueva URL y actualízala en tu entorno:
                     * Ve a tripleten_qa_api en el panel izquierdo
                     * Actualiza el Current value con la nueva URL
                     * Haz clic en Save
### 3. Elimina el espacio en la URL Asegúrate de que quede así:
{{base_url}}/api/v1/kits
Pregunta:
¿Tienes acceso al panel de TripleTen donde puedes reiniciar el servidor? 🤔
 image.png 

si era el servido ya funciona bien
¡Excelente! 🎉 ¡Me alegra que ya esté funcionando!
Veo que tu request POST Crear Kits devolvió un 201 Created — eso es exactamente lo que se espera cuando se crea un recurso nuevo en una API REST. ¡Muy bien!
Analizando tu respuesta, puedo ver que el kit fue creado con:
                     * "name": "Kit de prueba"
                     * "id": 8
                     * "productsCount": 0
Ahora te hago una pregunta para reflexionar: ¿Por qué crees que este endpoint devuelve 201 y no 200? ¿Cuál es la diferencia entre ambos códigos de estado? 🤔
la verdad no lo se
¡No te preocupes! Es un concepto muy importante en APIs. Te lo explico con una analogía 😊
Piensa en un restaurante 🍽️
                     * 200 OK → Pediste información y el mesero te la trajo. Todo bien, nada nuevo pasó.
                     * 201 Created → Pediste que te hicieran un platillo especial y el chef lo creó desde cero para ti.
En términos de API:
Código
	Significado
	¿Cuándo se usa?
	200
	OK
	Cuando obtienes o modificas algo existente
	201
	Created
	Cuando creas algo nuevo en el servidor
	En tu caso:
Usaste POST para crear un kit nuevo → El servidor respondió 201 porque efectivamente creó un recurso nuevo con id: 8.
Regla fácil de recordar:
Si la acción crea algo nuevo → espera un 201 🆕 Si la acción consulta o modifica algo → espera un 200 ✅
Pregunta para ti:
Mirando tu colección en Postman, tienes un request llamado "Obtener Kits". ¿Qué código de estado esperarías que devuelva ese request y por qué? 🤔
Mon, Jun 15 at 10:01 PM
 image.png 

hice la leccion y me sale mal no me carga como en el video con el 200ok
¡Veo el problema! Según la lección, el 404 Not Found en este caso puede tener dos causas. Vamos a revisarlas 🔍
Posibles causas:
### 1. ¿El servidor expiró de nuevo? Como pasó antes, los servidores se apagan después de un tiempo. Verifica en la plataforma de TripleTen que el servidor esté activo y que {{base_url}} tenga la URL correcta y actualizada.
### 2. ¿El kit "Sabores de París" existe en el servidor? Este es el punto clave 🎯 Si el servidor fue reiniciado, los datos se borran. El kit que estás buscando puede que no exista en la base de datos actual.
¿Cómo verificarlo?
Primero haz una solicitud con tu request "Obtener Kits" (GET) para ver qué kits existen actualmente en el servidor.
Pregunta:
¿Qué kits aparecen cuando usas el request "Obtener Kits"? ¿Aparece "Sabores de París" en la lista? 🤔
 image.png 

sera que es porque estaba mal escrito yo no coloque asi como lo enviaaste
Sabores de París y asi salia el 200 ok
lo hice asi
Sabores de parís
y salia el 404
¡Exactamente! ¡Lo descubriste tú solo! 🎉
¡Eso es un hallazgo muy importante como QA!
La diferencia fue solo una letra mayúscula:
                     * ❌ Sabores de parís → 404 Not Found
                     * ✅ Sabores de París → 200 OK
¿Qué nos dice esto?
La API es case-sensitive (sensible a mayúsculas/minúsculas). Es decir, trata París y parís como palabras completamente diferentes.
¿Por qué es importante esto para un QA?
Acabas de hacer exactamente lo que hace un tester: probar variaciones de los datos para ver cómo responde el sistema. Esto se llama probar casos límite o edge cases 🧪
Un buen QA siempre pregunta: - ¿Qué pasa si escribo en minúsculas? - ¿Qué pasa si agrego un espacio extra? - ¿Qué pasa si uso un acento diferente?
Pregunta:
Ahora que ya tienes el 200 OK con la respuesta correcta, ¿qué información interesante ves en el cuerpo de la respuesta? ¿Qué datos te devolvió el servidor sobre "Sabores de París"? 🤔
Hablar
El compañero de IA puede cometer errores. Deja tu opinión
Capítulo 2/6
Ciclo de Solicitud y Respuesta de la API: Enviar, Recibir, Validar
20 min
Parámetros: filtrando los resultados de la API
Imagina que estás realizando una tarea en tu trabajo: te han pedido que revises el kit “Sabores de París” para verificar qué contiene.
Ya lo intentaste buscar por su nombre antes, pero en aquella ocasión solo seguiste instrucciones, no entendías cómo funcionaba.
Para poder hacerlo por tu cuenta, necesitas entender primero dos conceptos: los parámetros de consulta y cómo usar Params en Postman.
¿Qué son los parámetros?
¿Prefieres leer? Haz clic aquí para ver la transcripción.
En una lección anterior, aprendiste las tres preguntas clave que definen una solicitud API:
Cómo, Dónde y Qué. Juntas forman la base de cualquier solicitud.
Pero a veces, eso no basta.
Para afinar lo que pedimos, podemos hacernos una pregunta adicional:
¿Cuáles? → ¿Qué datos específicos quiero recibir?
  

La respuesta a esta pregunta está en los parámetros de consulta.
Te resultarán de mucha utilidad cuando necesites filtrar, ordenar o hacer un ajuste preciso de los resultados que la API devuelve.
Son fragmentos pequeños de información adicional que puedes incluir —normalmente cuando usas GET o DELETE—.
En un restaurante, el menú suele tener variantes: por ejemplo, no solo hay "vino", hay tinto y blanco.
Entonces dices:
“Por favor, tráeme una copa de vino blanco.”
  

Eso es lo que hacen los parámetros: no cambian el recurso, pero indican qué versión exacta quieres recibir.
Cómo se ve un parámetro en la URL
De hecho, ya has usado parámetros anteriormente, solo que no te has dado cuenta.
Esta es la primera solicitud que enviaste. ¿Ves la parte del final?
  

Ese es un parámetro de consulta. Le dice a la API:
“Muéstrame solo los kits vinculados al cardId 1.”
Los parámetros de consulta van después del signo de interrogación ?.
Si hay más de uno, se unen con el símbolo &.
Por ejemplo, imagina que usas una API de películas:
  

Aquí estás pidiendo comedias que se estrenaron en 2023 —combinando ambos filtros en una sola solicitud—.
Esa es la ventaja de los parámetros: son simples, flexibles y precisos.
Endpoint vs. Parámetros. ¿Cuál es la diferencia?
Puede parecer que los parámetros son solo una parte más de la URL, al igual que el endpoint; pero en realidad tienen funciones distintas.
                     * El endpoint le dice a la API qué tipo de recurso quieres:
→ /api/v1/kits → “Dame los kits.”
                     * El parámetro le dice a la API qué parte específica de ese recurso te interesa:
→ ?cardId=1 → “Solo los que están vinculados a la tarjeta 1.”
El endpoint es el destino.
Los parámetros son las condiciones.
Pregunta
¿Qué parte de esta URL filtra los resultados para mostrar solo los documentos creados por un usuario específico?
{{base_url}}/api/docs?authorId=5&category=user-library
category=user-library
/api/docs
?authorId=5&category=user-library
authorId=5
¡Exacto! Este parámetro le indica a la API que devuelva únicamente los documentos creados por el usuario 5.
¡Buen trabajo!
¿Dónde se configuran en Postman?
Hay dos formas de añadir parámetros a tu solicitud:
                        * Manualmente en la URL: puedes escribirlos directamente al final del endpoint (por ejemplo: ?cardId=1).
                        * Usando la pestaña Params en Postman: si los agregas ahí, Postman actualizará la URL automáticamente. Nos centraremos en esta opción.
💡
Usar la pestaña Params ayuda a reducir errores tipográficos en la URL y permite ver los valores con mayor claridad.
¡Veamos cómo usarla!
Servidor
¡Genial, tu servidor ha sido iniciado!
Dirección del servidor: https://cnt-e24c964f-e2dd-4b31-9697-1c4c6af1251e.containerhub.tripleten-services.com
Reiniciar el servidor
¿Prefieres leer? Haz clic aquí para ver la transcripción.
Entonces, ¿cómo encontramos el kit “Sabores de París”?
                        * Crea una nueva solicitud GET llamada “Buscar un kit por nombre 2”
                        * Revisa la documentación.
  

                        * Copia la URL desde la documentación: {{base_url}}/api/v1/kits/search
                        * Abre la pestaña Params. La documentación indica que debes usar un par clave–valor, donde name es la clave y el nombre exacto del kit es el valor. Escribe:
                        * Clave: name
                        * Valor: Sabores de París
                        * Haz clic en Send (Enviar).
Pregunta
¿Qué resultado obtuviste después de enviar la solicitud?
404 Not Found
400 Bad Request
520 Unknown Error
200 OK
La solicitud funcionó como se esperaba y devolvió los datos del kit, tal y como indica la documentación.
¡Bien hecho!
¡Encontraste el kit! “Sabores de París” ya aparece en la respuesta.
  

¡Tarea completada! ✔️
Ahora que sabes cómo funcionan los parámetros de consulta —y cómo usarlos en Postman— puedes comenzar a hacer solicitudes más precisas por tu cuenta.
Valoración de la lección
Siguiente


Sprint 4: Pruebas de API
Capítulo 2/6
Ciclo de Solicitud y Respuesta de la API: Enviar, Recibir, Validar
30 min
Encabezados: lo que la API necesita saber sobre tu solicitud
Anteriormente probaste cómo obtener kits de una tarjeta con cardId. Todo funcionó bien.
Ahora te toca comprobar otra cosa:
En Urban Grocers, cada usuario puede crear sus propios kits —y deberían ser visibles solo para quien los creó—.
Esto significa que:
                        * Si estás autenticado, puedes ver tus kits.
                        * Si no lo estás, no deberías verlos.
Aquí entra la autorización.
🎯 Tu tarea: asegurarte de que la API solo muestre los kits correctos según el estado de autenticación.
Seguirás utilizando GET /api/v1/kits, pero esta vez la respuesta dependerá de lo que incluyas en tu solicitud.
Para poder probarlo, necesitas aprender a usar los encabezados.
¿Qué son los encabezados?
¿Prefieres leer? Haz clic aquí para ver la transcripción.
En la lección anterior, viste que además de las preguntas básicas (cómo, dónde, qué), a veces el servidor necesita más contexto.
En este caso, veremos: ¿con qué?
¿Con qué token, formato o metadatos debe enviarse la solicitud?
Esa información se envía en los encabezados, o headers.
  

📎
Los encabezados llevan datos técnicos sobre cómo manejar la solicitud, no sobre el contenido.
Imagina un restaurante donde formas parte de un programa de fidelidad: escaneas tu tarjeta o das tu número —y de inmediato saben tu nombre, idioma o alergias,
incluso antes de que hagas tu pedido—.
  

Eso es lo que hacen los encabezados: le dan al servidor el contexto antes de procesar la solicitud.
Encabezados vs. Parámetros
A primera vista, los encabezados y los parámetros pueden parecer similares —ambos llevan información adicional en una solicitud— pero cumplen funciones muy diferentes:
                        * Los parámetros indican qué quieres: por ejemplo, kits para la tarjeta 2.
                        * Los encabezados indican cómo procesarla: por ejemplo, quién la envía y en qué formato.
Pregunta
¿Cuál es la forma correcta de enviar esta información al servidor?
Estás probando una app de música. Quieres verificar que el endpoint /playlists/my solo muestre listas creadas por la persona que ha iniciado sesión.
En el encabezado
¡Exacto! Esta información no trata sobre qué se pide, sino quién lo pide. Y eso se transmite con un encabezado.
Estás probando una app de vuelos, /flights/search. Quieres ver qué vuelos hay disponibles de Cancún a Buenos Aires el 15 de agosto.
En los parámetros
¡Muy bien! Estás especificando qué datos quieres —como origen, destino y fecha— y eso se hace con los parámetros.
¡Bien hecho!
Encabezados comunes
¿Prefieres leer? Haz clic aquí para ver la transcripción.
Estos son algunos encabezados clave que verás al probar APIs:
                        * Authorization: indica quién hace la solicitud.
Úsalo para verificar que solo los usuarios correctos accedan a los datos.
→ Authorization: Bearer jknnFApafP4awfAIFfafam2fma
 📎 "Bearer" le dice al servidor que estás iniciando sesión, y el código largo es tu identificación personal.
                        * Content-Type: especifica el formato de los datos enviados.
Necesario si envías un body en JSON. Postman suele agregarlo automáticamente.
→ Content-Type: application/json
 📎 Le estás diciendo al servidor: “El contenido de mi solicitud está en formato JSON”.
                        * Accept: indica el formato que esperas recibir.
Útil al probar cómo responde el servidor en diferentes formatos, como JSON, XML o HTML.
→ Accept: application/json
 📎 Le pides al servidor: “Por favor, responde en formato JSON”.
                        * Cookie: envía datos de sesión en sistemas antiguos.
Común en APIs heredadas. Suele venir especificado por el equipo técnico.
→ Cookie: sessionid=abc123
 📎 Esta línea le recuerda al servidor que ya habías iniciado sesión antes, usando tu ID de sesión.
¿Cómo trabajan los QA engineers con los encabezados?
Los QA engineers usan los encabezados para probar aspectos de la solicitud que no forman parte del contenido principal, pero que igual afectan la respuesta del servidor.
¿Cómo saber si se necesitan encabezados?
Empieza con la documentación. Si no se menciona ningún encabezado, los comportamientos inesperados —como errores o respuestas vacías— pueden ser una pista.
Por ejemplo:
→ Con el encabezado Authorization, GET /api/kits devuelve tus kits personales.
→ Sin él, el servidor devuelve un error.
En general:
Agrega encabezados manualmente cuando dependen de quién hace la solicitud.
Los relacionados con el formato suelen añadirse automáticamente —pero revísalos si estás probando cómo el servidor los maneja—.
Pregunta
Vas a enviar una reseña en JSON al endpoint POST /reviews. ¿Qué encabezado le dice al servidor cómo leer el cuerpo?
Cookie
Accept
Content-Type
¡Exacto! Este encabezado indica que estás enviando datos en JSON. Postman suele añadirlo automáticamente, pero es clave al depurar errores.
Authorization
¡Lo has entendido bien!
Pregunta
Vas a hacer una solicitud a GET /courses y quieres la respuesta en XML. ¿Qué encabezado deberías usar?
Content-Type
Cookie
Authorization
Accept
¡Muy bien! Este encabezado le dice al servidor que esperas una respuesta en formato XML —útil para probar distintos formatos de respuesta—.
¡Lo has entendido bien!
Pongámoslo en práctica
Tu tarea es verificar si un usuario autorizado ve solo sus propios kits.
Para ello, necesitarás usar el encabezado Authorization, ya que la API responde según quién hace la solicitud.
Lo haremos en dos pasos:
Paso 1. Obtén tu token
Servidor
¡Genial, tu servidor ha sido iniciado!
Dirección del servidor: https://cnt-b8ac9be9-65e8-413f-82f6-8b86b7f180c2.containerhub.tripleten-services.com
Reiniciar el servidor
¿Prefieres leer? Haz clic aquí para ver la transcripción.
Para hacer una solicitud autorizada, necesitas un token, que le dice al servidor quién está haciendo la solicitud.
Puedes obtener uno cuando creas un nuevo usuario: esto forma parte de la respuesta que envía el servidor.
Vamos a encontrarlo juntos:
                           * Abre tu solicitud “Crear nuevo usuario”.
                           * Envíala.
                           * En la sección de respuesta (abajo), busca la clave authToken y copia su valor: ese es tu token.
  

Lo usarás en el siguiente paso, dentro del encabezado Authorization.
Paso 2. Agrega el encabezado Authorization
¿Prefieres leer? Haz clic aquí para ver la transcripción.
Ahora que ya tienes tu token, es momento de usarlo.
📌 Para comprobar si los kits están correctamente vinculados a un usuario específico, necesitas crear un nuevo kit, pero esta vez como usuario autorizado.
¿Y por qué uno nuevo?
Porque es la forma más sencilla de verificar si el servidor lo asocia correctamente a tu perfil.
En una app real, así es como se sabe: este kit te pertenece.
Verás la confirmación directamente en la respuesta: tu información de usuario y token deben aparecer dentro del bloque user. Eso significa que la solicitud tuvo éxito y está autorizada.
Primero échale un vistazo a la documentación:
  

                           * Abre Postman y carga la solicitud POST /api/v1/kits.
                           * Ve a la pestaña Headers (Encabezados) justo debajo de la URL.
                           * En la primera fila disponible, escribe lo siguiente:
                           * Clave: Authorization
                           * Valor: Bearer {Tu_token}
                           * Asegúrate de que la casilla esté marcada ✅ para que el encabezado se incluya en la solicitud.
Agrega el cuerpo que ya conoces para agregar un kit de prueba:
{
   "cardId": 1,
   "name": "Kit de prueba"
 }
                           *                            * Envía la solicitud.
💡
Para hacer la prueba más interesante: ahora crea un kit de la manera que ya conocías, sin usar el encabezado.
Pregunta
¿Qué resultado obtuviste después de enviar la solicitud?
404 Not Found
400 Bad Request con un mensaje sobre los datos faltantes
201 Created con la información del kit y el usuario en el cuerpo de la respuesta
¡Bien hecho! Eso significa que el servidor aceptó tu solicitud, se creó el kit y se vinculó a tu usuario. Se superó la prueba.
405 Method Not Allowed
401 Unauthorized con un mensaje sobre credenciales faltantes o no válidas
¡Buen trabajo!
Ahora, ¡comparemos el resultado!
Si enviamos el encabezado de autorización y el token, el servidor crea el kit y automáticamente lo asigna al usuario que creamos.
💪
Desafío extra
Ahora que creaste un kit como usuario con la sesión iniciada, comprueba si el sistema restringe el acceso correctamente:
→ Envía una solicitud GET /api/v1/kits con tu token: deberías poder ver tu kit.
→ Luego envía la misma solicitud sin el token: deberías recibir un error.
¿El sistema bloquea el acceso cuando no hay autorización?
Inténtalo y compruébalo.
Ya sabes qué son los encabezados, cómo configurarlos en Postman, y qué efecto tienen en la respuesta que recibes. Son una parte clave para que la API entienda tu solicitud correctamente.
Valoración de la lección
Siguiente




Sprint 4: Pruebas de API
Capítulo 2/6
Ciclo de Solicitud y Respuesta de la API: Enviar, Recibir, Validar
45 min
Respuestas: cómo leer las respuestas de una API
Imagina la siguiente situación, te contacta tu Project Manager para pedirte lo siguiente:
— ¿Puedes revisar la búsqueda de productos? Si alguien busca galletas, solo deberíamos mostrar los kits que realmente las incluyen.
Es una tarea importante, y quieres revisar con atención qué está devolviendo el servidor.
Ya sabes cómo hacer este tipo de solicitudes, pero aún no hemos visto detalladamente cómo leer una respuesta como lo haría un QA engineer profesional.
¡Comencemos!
¿De qué está hecha una respuesta?
En el Capítulo 1 hablamos de cómo funcionan las APIs: tú envías una solicitud y el servidor da una respuesta.
  

Una respuesta es aquello que devuelve un servidor: el resultado de tu solicitud y algunos detalles técnicos.
📎Cada solicitud, exitosa o no, obtiene una respuesta.
Veamos de nuevo nuestra primera respuesta:
En la interfaz de Postman verás cuatro elementos clave:
  

¿Cómo trabaja un QA engineer con todo esto?
Depende del tipo de prueba que haya que realizar —lo veremos más adelante— pero hay un orden que suele tener sentido
                           * Empieza por el código de estado: ¿La solicitud fue exitosa o falló?
                           * Luego revisa el cuerpo: ¿Los datos son correctos y están completos?
                           * Si es necesario, revisa los encabezados: son útiles para la autenticación, en caché.
                           * Por último, verifica el tiempo de respuesta: incluso sin hacer pruebas de rendimiento, una respuesta lenta puede ser señal de problema.
Ser QA engineer consiste en analizar no solo si hubo una respuesta, sino qué dijo el servidor, cómo lo dijo y qué tan rápido.
Códigos de estado: ¿Qué pasó con tu solicitud?
¿Prefieres leer? Haz clic aquí para ver la transcripción.
Cada vez que haces una solicitud, el servidor devuelve un código de estado.
📎Un código de estado es un número corto (como 200, 400, 404) que resume lo que pasó con la solicitud.
En un restaurante, cuando el mesero regresa, lo primero que dice es el estado del pedido:
“Aquí tienes, justo como lo pediste.”
o incluso:
“Lo siento, no puedo servirte, órdenes de la gerencia.”
  

Para un QA engineer, estos es lo primero que debes revisar:
                           * ¿La solicitud funcionó como se esperaba?
                           * ¿Falló por la razón correcta?
                           * ¿El servidor está respondiendo de forma coherente?
                           * ¿Debes seguir probando el cuerpo o arreglar la solicitud primero?
No puedes basarte solo en los códigos de estado, pero pueden ayudarte a detectar problemas rápidamente.
📎En pruebas de API, es común provocar todos los códigos de estado posibles para validar que el servidor responde como debería.
Códigos de estado comunes:
El primer dígito del código de estado indica el tipo de respuesta:
                           * 2xx éxito — la solicitud fue correcta
                           * 3xx redirección — hace falta otra acción
                           * 4xx error del cliente — solicitud mal hecha
                           * 5xx error del servidor — falló al procesar
Los otros dígitos dan más detalle, pero este primer número ya da buen contexto.
  

💡 ¿Quieres ver la lista completa de códigos de estado? Aquí tienes la referencia.
Pongámoslo todo en práctica
Servidor
¡Genial, tu servidor ha sido iniciado!
Dirección del servidor: https://cnt-bab582a4-6a5a-42be-8020-46edb81c1cdb.containerhub.tripleten-services.com
Reiniciar el servidor
Volvamos a nuestra tarea de QA. Primero, vamos a validar los códigos de estado que devuelve el endpoint al buscar los ID de productos válidos y no válidos.
                           * Utiliza la documentación para crear una solicitud “Búsqueda de kits por producto”.
Documentación
  

Parámetros:
  

Ejemplo de cuerpo:
{
"ids": [1, 2, 3]
}
Ejemplo de respuesta:
[
    {
           "id": 1,
           "name": "Para pícnics",
           "productsList": [
               {
                   "id": 1,
                   "quantity": 1
               },
               {
                   "id": 2,
                   "quantity": 1
               },
               {
                   "id": 3,
                   "quantity": 1
               }...
           ],
           "productsCount": 3
       }
                           * Envía una búsqueda con IDs válidos en el cuerpo.
{
  "ids": [1, 2, 3]
}
Pregunta
¿Qué código de estado recibiste cuando la enviaste ID de productos válidos [1, 2, 3]?
500 Internal Server Error
200 OK
¡Correcto! El código 200 OK indica que la API procesó la solicitud exitosamente y devolvió la información solicitada: en este caso, los kits que contienen los productos con IDs válidos.
400 Bad Request
¡Perfecto!
Prueba con IDs no válidos:
Ahora, cambia los ID a un formato no válido, por ejemplo:
 {
   "ids": [A, B, C]
 }
                           * Pregunta
¿Qué código de estado recibiste cuando enviaste los ID no válidos [A, B, C]?
200 OK
404 Not Found
400 Bad Request
¡Correcto! La API no puede procesar la solicitud porque los valores enviados ("A", "B", "C") no son del tipo esperado. Se espera una lista de números, no de texto.
¡Perfecto!
La API devuelve 200 OK con IDs válidos y 400 Bad Request con IDs no válidos, señal de que maneja bien las solicitudes y valida los datos correctamente:
Cuerpo de la respuesta: ¿Es lo que pediste?
¿Prefieres leer? Haz clic aquí para ver la transcripción.
Imagina esto:
Envías una solicitud válida, el servidor responde 200 OK, pero el cuerpo está vacío.
[]
Como QA engineer, esta es una trampa clásica: el estado está bien, pero los datos no.
Imagina que el mesero deja la bandeja y levanta la tapa. Esperabas la famosa pasta con trufa, esa que todos elogian.
¿Y qué hay? Brócoli al vapor y frío.
Sí, es comida, pero no lo que pediste.
Así puede ser el cuerpo de una respuesta 200 OK, pero con los datos equivocados.
  

📎Por eso el cuerpo también importa: es donde están los datos reales que necesitas revisar.
No todas las respuestas tienen cuerpo. Cuando lo tienen, suelen seguir la misma estructura que el de una solicitud: un objeto o lista JSON con datos útiles.
Como QA engineer, debes revisar si el cuerpo tiene sentido:
                           * Estructura: ¿Es una lista o un objeto? ¿Los campos están bien ubicados?
                           * Campos clave: ¿Está id, name, productsList?
                           * Datos correctos: ¿Coinciden con lo que pediste? Si productsCount dice 3, realmente debe haber 3 elementos.
                           * Cosas raras: Listas vacías, cantidades en cero, IDs incorrectos.
Pongámoslo en práctica
Volvamos a nuestra tarea y analicemos el cuerpo de la respuesta.
Parte 1: Revisa una respuesta válida
Abre la solicitud “Buscar kits por producto”, la que busca los productos [1, 2, 3].
Observa el cuerpo de la respuesta y responde al cuestionario.
Pregunta
¿Qué observas en el cuerpo de la respuesta?
Elige tantas como quieras
Todos los campos requeridos están presentes
Puedes ver name, id y productsList, todos son esenciales para confirmar que los datos son útiles.
La cantidad de elementos en productsList coincide con productsCount
Ambos kits muestran un número consistente de productos. Esa es una buena señal.
Solo un kit incluye los productos [1, 2, 3]
¡Excelente trabajo!
Parte 2: Prueba con un producto inexistente
Toma la misma solicitud y reemplaza los IDs 1, 2, 3 por 99.
Usa este cuerpo:
{
  "ids": [99]
}
Pregunta
Hiciste una solicitud con el id [99] al endpoint /api/v1/products/kits. Recibiste un 200 OK y el cuerpo contenía lo siguiente: []
¿Qué significa esto?
La solicitud fue aceptada, y devolvió los datos que esperabas para un id inexistente.
Correcto. Esto no impide que la API funcione, pero como QA deberías analizar si devolver un arreglo vacío ante un id inexistente es el comportamiento esperado o una omisión en las validaciones.
La API no funcionó correctamente: se devolvieron los datos incompletos y posiblemente hay un defecto.
El JSON del cuerpo está mal escrito.
¡Excelente trabajo!
Encabezados de respuesta: ¿Qué más vino con los datos?
Normalmente revisas el código de estado y el cuerpo, pero a veces eso no basta, y los encabezados tienen las pistas.
  

Imagina que estás en una pastelería y quieres comprar algo para llevar a casa. El pastel se ve bien y huele increíble. Das tu primer bocado: perfecto… pero tu lengua empieza a picar. Miras la caja y en ella aparecen dos etiquetas:
“Sin gluten”: genial.
“Contiene almendras”: ¿¡cómo!?
¡Tú lo pediste sin almendras!
Por eso, como QA engineer, debemos revisar los encabezados. A veces, el problema no está en los datos, sino en los metadatos.
  

¿Cuándo revisarlos?
Revisa los encabezados si el estado es OK y el cuerpo tiene buen aspecto, pero algo falla.
Ahí puede estar el problema. Ejemplos comunes:
                           * Autenticación: al iniciar sesión o hacer alguna acción protegida, el servidor devuelve un token (Set-Cookie o Authorization). → Si falta o es incorrecto, las solicitudes siguientes fallarán.
                           * Formato de la respuesta: algunos endpoints, como POST /api/v1/products/kits, deben devolver JSON. → Si el Content-Type dice text/html, puede ser un error del servidor.
📎Los encabezados siempre están presentes. Puedes revisar su utilidad en la documentación o consultarlo con un desarrollador.
Pongámoslo en práctica
Debemos verificar que la respuesta sea JSON, ya que la app necesita este formato para funcionar.
                           * Vuelve a la solicitud “Buscar kits por producto”, la que incluye los IDs de producto [1, 2, 3].
                           * Ve a la pestaña “Headers” en la sección de respuesta (junto a Body).
                           * Verifica si los encabezados coinciden con la documentación.
Documentación
  

Pregunta
¿Qué valor recibiste en el encabezado “Content-Type”?
application/xml
text/html
application/json
Correcto. Este valor indica que el servidor está devolviendo datos en formato JSON, como se espera en este endpoint.
¡Buen trabajo!
El formato coincide con la documentación: el servidor devolvió JSON, tal y como se esperaba. Esto significa que la app puede procesar los datos.
Tiempo de respuesta: ¿Qué tan rápido respondió el servidor?
El tiempo de respuesta es el tiempo que tarda el servidor en contestar. En Postman lo verás abajo a la derecha, en milisegundos o segundos.
En nuestra solicitud “Buscar kits por producto”, el tiempo de respuesta es de 183 milisegundos. ¡Un buen resultado!
  

Este dato importa.
Aunque el estado sea 200 OK y los datos parezca que están bien, una respuesta lenta puede causar retrasos, errores o frustración.
Imagina que pides que te preparen un smoothie rápido. Tienes prisa y la tarea no parece complicada: al fin y al cabo, es solo fruta y hielo. ¿Cuánto puede tardar, dos minutos?
Pero pasan 20 minutos, luego 35… Al final, te lo traen. Está bien, pero ya llegaste tarde.
Pasa lo mismo con las APIs: si la respuesta tarda mucho, algo no está funcionando como debería.
¿Cómo maneja esto un QA engineer?
                           * Mira el tiempo: Postman lo muestra automáticamente.
                           * Compáralo con lo esperado:
                           * Consultas simples: casi instantáneas.
                           * Actualizaciones o subidas: hasta 2 s.
                           * Decide si esto podría ser un problema. Si las respuestas son siempre lentas o repentinamente más lentas, podría haber un problema de rendimiento.
En pruebas regulares, igual vale la pena reportar este tipo de demora.
En pruebas dedicadas de rendimiento, los retrasos son justo lo que se mide, especialmente con carga o con muchos usuarios.
Pregunta
Imagina que envías una solicitud a /api/v1/products/kits. Estado: 200 OK, el cuerpo coincide con la documentación, pero el tiempo de respuesta es de 5 segundos.
¿Cuál es tu siguiente paso?
Todo está bien. El estado y el cuerpo coinciden. El tiempo es óptimo.
El tiempo es alto, pero el estado y el cuerpo están bien, así que no es necesario reportarlo.
Esto sería un retraso. Debería reportarse.
Correcto. 5 segundos es mucho para este tipo de solicitud. Reportarlo permitiría identificar posibles problemas de rendimiento.
Aumenta el tiempo de espera en Postman para evitar retrasos.
El tiempo es demasiado largo. Es posible que fuera la red, pero podemos continuar.
¡Lo has entendido bien!
¡Listo! Ya sabes cómo trabajar con todo el ciclo básico de una API: cómo enviar una solicitud correctamente y cómo leer y analizar la respuesta como un QA engineer profesional.
En los siguientes capítulos, aprenderás a aplicar esto dentro del ciclo completo de pruebas de API para que puedas detectar errores, validar flujos y asegurar que todo funcione correctamente.
Valoración de la lección
Siguiente


Sprint 4: Pruebas de API
Capítulo 3/6 · Faltan 4 lecciones
Documentación de la API: Identificar Qué se va a Probar
10 min
Flujo de trabajo de pruebas de API
La aplicación Urban Grocers está creciendo rápidamente y te han asignado las pruebas de una nueva funcionalidad que está a punto de lanzarse: la gestión de almacenes. Esta actualización cambiará la forma en que el sistema controla el inventario y calcula los tiempos de entrega.
  

¿Suena desafiante? Lo es, pero también es una gran oportunidad para consolidar lo que ya has aprendido.
Para probar una funcionalidad como esta, necesitas algo más que habilidades técnicas: necesitas comprender bien la tarea, encontrar un punto de partida adecuado y avanzar con claridad por cada parte del proceso.
En otras palabras: necesitas un flujo de trabajo.
Ya sabes cómo enviar solicitudes a una API y leer las respuestas que te da. Con ese conocimiento, llegó el momento de convertirlo en una estrategia de pruebas y aplicarlo a una tarea real del backend.
Ahí es donde entra el flujo de trabajo de pruebas de API.
Así es como se ve:
  

Los próximos capítulos siguen estos pasos: a veces abordaremos uno por capítulo y otras veces dos, si tienen sentido juntos.
Este capítulo se enfocará en los dos primeros:
→ Entender exactamente qué se espera que pruebes.
→ Aprender a utilizar documentación de API real.
Hasta este momento, has trabajado con fragmentos: documentación simplificada adaptada a ejercicios concretos. Pero a partir de ahora explorarás conjuntos completos de documentación como los que usan los equipos en proyectos reales.
También conocerás una herramienta profesional donde se crean y publican estas documentaciones.
¡Empecemos!
Valoración de la lección
Siguiente



Sprint 4: Pruebas de API
Capítulo 3/6 · Faltan 4 lecciones
Documentación de la API: Identificar Qué se va a Probar
10 min
Flujo de trabajo de pruebas de API
La aplicación Urban Grocers está creciendo rápidamente y te han asignado las pruebas de una nueva funcionalidad que está a punto de lanzarse: la gestión de almacenes. Esta actualización cambiará la forma en que el sistema controla el inventario y calcula los tiempos de entrega.
  

¿Suena desafiante? Lo es, pero también es una gran oportunidad para consolidar lo que ya has aprendido.
Para probar una funcionalidad como esta, necesitas algo más que habilidades técnicas: necesitas comprender bien la tarea, encontrar un punto de partida adecuado y avanzar con claridad por cada parte del proceso.
En otras palabras: necesitas un flujo de trabajo.
Ya sabes cómo enviar solicitudes a una API y leer las respuestas que te da. Con ese conocimiento, llegó el momento de convertirlo en una estrategia de pruebas y aplicarlo a una tarea real del backend.
Ahí es donde entra el flujo de trabajo de pruebas de API.
Así es como se ve:
  

Los próximos capítulos siguen estos pasos: a veces abordaremos uno por capítulo y otras veces dos, si tienen sentido juntos.
Este capítulo se enfocará en los dos primeros:
→ Entender exactamente qué se espera que pruebes.
→ Aprender a utilizar documentación de API real.
Hasta este momento, has trabajado con fragmentos: documentación simplificada adaptada a ejercicios concretos. Pero a partir de ahora explorarás conjuntos completos de documentación como los que usan los equipos en proyectos reales.
También conocerás una herramienta profesional donde se crean y publican estas documentaciones.
¡Empecemos!
Valoración de la lección
Siguiente




Sprint 4: Pruebas de API
Capítulo 3/6
Documentación de la API: Identificar Qué se va a Probar
25 min
Fundamentos de la documentación de la API
Para comenzar tu misión como QA engineer, necesitas entender cómo funcionan las APIs y cómo se usan.
Para ello, vamos a explorar la documentación técnica del sistema de almacenes.
En el mundo real la documentación de una API no es algo simple, y tampoco es breve. La de Urban Grocers, por ejemplo, tiene más de 65 páginas; y cuando estés probando algo —como crear un almacén— tendrás que encontrar esa información por tu cuenta.
  

Por eso es clave saber navegar documentación extensa con rapidez y seguridad, tanto para las tareas que tendrás que realizar próximamente como para el proyecto final.
Es tan amplia porque está escrita para todos los que trabajan con el sistema: desarrolladores, arquitectos y QA engineers como tú.
En esta lección, hablaremos sobre qué es la documentación de una API y en qué formatos suele presentarse.
Documentación de la API
💡
La documentación de una API es un conjunto de materiales técnicos que explican cómo usar una API: qué puede hacer, qué datos espera recibir y qué respuestas devuelve.
En resumen, la documentación de una API es tu mapa del sistema. Sin ella, trabajar con una API es como intentar reparar una máquina sin el manual de instrucciones: no sabes para qué sirve cada parte ni puedes garantizar que no vayas a romper nada en el proceso.
¿En qué se diferencia la documentación de API de la que usaste antes?
Ya estás familiarizado con la documentación y la has usado antes para probar interfaces. ¿Cuál es la diferencia con esta?
  

Pregunta
Estás probando cómo se guarda una nueva dirección en el sistema.
¿Dónde puedes ver qué datos debes enviar?
En un documento de los requisitos que describe lo que pasa al hacer clic en "Agregar dirección”
En una maqueta o diseño de pantalla del formulario de dirección
En la sección de la documentación de la API que muestra los códigos de estado como 200 o 422
En la parte de la documentación de la API que enumera los campos requeridos para la solicitud "Crear dirección”
¡Exacto! Ahí encontrarás los campos que el sistema necesita, como calle, ciudad o código postal.
¡Perfecto!
Cómo usan la documentación de API los QA engineers
Como QA engineer, tu trabajo con la documentación de API va más allá de solo leerla.
Usarás la documentación para:
                           * Entender el sistema: qué debería suceder y cómo.
                           * Diseñar casos de prueba: en función de los datos de entrada, salidas esperadas y casos límite.
                           * Revisar las estructuras de solicitud/respuesta: para verificar que la API se comporte correctamente.
                           * Detectar vacíos o ambigüedades y reportarlos cuanto antes.
                           * Preparar datos: usando ejemplos de cuerpos de solicitud y campos obligatorios.
En algunos casos, la documentación puede estar incompleta (o equivocada). Como QA engineer, parte de tu trabajo es detectar eso y hacer las preguntas correctas.
Formatos de documentación de API
¿Prefieres leer? Haz clic aquí para ver la transcripción.
La documentación de API viene en distintos formatos. Como QA engineer, no te toca elegir cuál tienes que usar, pero sí necesitas reconocer con qué tipo estás trabajando —y cómo sacarle el máximo provecho—.
Vamos a desglosarlo.
Hay muchas formas de clasificar los formatos comunes de documentación de API. Aquí usaremos dos criterios principales:
                           * Cómo se crea la documentación: manualmente o automáticamente.
                           * Cómo se comporta: estática o interactiva.
Veamos qué significa cada uno.
  

Documentación manual vs Documentación automática
La documentación manual la escribe una persona, como un desarrollador o un redactor técnico. Ofrece control total sobre el contenido pero requiere de actualizaciones manuales, y ese caso no siempre se da.
La documentación automática se genera desde el código a través de herramientas especiales. Suele estar actualizada, si el equipo técnico la mantiene bien.
Estática vs. Interactiva
La documentación que has usado hasta ahora era estática, es decir, solo podías leerla. En sistemas modernos, es común ver documentación interactiva, que permite enviar solicitudes y ver las respuestas sin salir del navegador.
Herramientas comunes de documentación
  

Veamos ahora a través de herramientas reales algunos formatos que encontrarás en muchas documentaciones.
1. PDF o Google Docs
Manual + Estática
  

Estos son los tipos de documentación más tradicionales. Los escribe a mano un miembro del equipo —a menudo para uso interno— y no se actualizan automáticamente.
No puedes interactuar con ellas. Solo las lees, extraes lo que necesitas y creas las solicitudes por tu cuenta.
Aquí tienes un ejemplo del tipo de documentación que ya usaste:
  

✅ Aspectos positivos: puede incluir contexto, diagramas o ejemplos.
❗ Aspectos negativos: puede estar desactualizada o incompleta.
📍 Común en: equipos pequeños, sistemas antiguos, proyectos en una etapa temprana o entornos donde los desarrolladores no configuran documentación automatizada.
🔍 Cuándo usarla:
Si es la única documentación que tienes, úsala, pero con ojo crítico: verifica las respuestas o consulta a los desarrolladores si sospechas que está desactualizada.
2. Apidoc
Automática + Estática
  

Esta documentación se genera a partir del código, normalmente con una herramienta que lee anotaciones especiales o archivos de configuración escritos por los desarrolladores.
Está bien estructurada y es clara, pero no es interactiva. No puedes enviar solicitudes desde la documentación directamente, necesitarás usar Postman u otra herramienta.
  

✅ Aspectos positivos: estructura precisa, refleja siempre la API actual (si se mantiene bien).
❗ Aspectos negativos: no permite hacer pruebas directamente.
📍 Común en: proyectos medianos o grandes con backends bien organizados.
🔍 Cuándo usarla:
Estos formatos son excelentes para revisar cómo están estructurados los endpoints y qué parámetros se esperan.
3. Swagger
Automática + Interactiva
  

Esta es la herramienta más popular y potente para la documentación de APIs en vivo. También se basa en el código del backend, pero a diferencia de Apidoc, es interactiva.
  

Puedes enviar solicitudes, modificar entradas y ver las respuestas al instante. Para un QA engineer, esto es extremadamente útil al probar o aprender cómo se comporta el sistema.
✅ Aspectos positivos:
                           * Se pueden probar los endpoints directamente desde el navegador.
                           * Suele reflejar el código más reciente.
❗ Aspectos negativos: puede carecer de explicaciones o lógica detallada.
📍 Usado en: proyectos modernos, APIs bien mantenidas, entornos con estándares industriales.
🔍 Cuándo usarla:
Empieza por ella siempre que Swagger esté disponible.
Te permite entender, probar y validar rápidamente cómo funcionan los endpoints.
Pregunta
Relaciona el escenario con el formato correcto de documentación:
Estás probando un servicio antiguo que fue creado por un equipo pequeño. Solo tienes un archivo con ejemplos y notas que alguien escribió a mano.
PDF
¡Exacto! Este tipo de documentación es común en proyectos pequeños o en etapas tempranas.
Estás a punto de probar un endpoint y quieres enviar solicitudes y ver las respuestas directamente desde la documentación, sin usar Postman.
Swagger
¡Muy bien! Swagger te permite hacer pruebas desde la misma interfaz de la documentación.
Estás revisando documentación bien estructurada, generada desde el código. Puedes ver los métodos, parámetros y ejemplos, pero no puedes ejecutar nada desde ahí.
Apidoc
¡Correcto! Apidoc muestra la estructura completa pero no es interactiva.
¡Bien hecho!
Cada formato tiene sus ventajas: algunos son más legibles y otros son más útiles para hacer las pruebas.
Como QA engineer, debes reconocer el tipo de formato, navegarlo y encontrar lo que necesitas.
Pronto practicarás con varios tipos.
Valoración de la lección
Siguiente





Sprint 4: Pruebas de API
Capítulo 3/6
Documentación de la API: Identificar Qué se va a Probar
35 min
Apidoc: explora la documentación
Ahora que realizaste tu tarea de pruebas, te toca dar el siguiente paso: explorar la documentación.
¿Cómo se trabaja con la documentación?
Antes de hacer pruebas, necesitas entender cómo debe comportarse la API. Si no, podrías probar cosas irrelevantes, ignorar casos límite o malinterpretar los resultados.
  

Leer la documentación antes de escribir las pruebas es como aprender las reglas de un juego de mesa antes de jugar. Podrías leerlas mientras juegas, pero será más lento y frustrante —y cometerás errores—.
  

La idea clave aquí es:
“Necesito entender este sistema lo suficientemente bien como para cuestionarlo después con confianza y precisión.”
Usarás la documentación para:
                           * Identificar los endpoints relevantes.
                           * Entender qué entradas se requieren (y en qué formato).
                           * Interpretar qué significa cada respuesta y cómo se ve el éxito o el fallo.
                           * Detectar áreas que pueden necesitar validación.
Urban.Grocers usa Apidoc: una herramienta ligera para explorar cómo funcionan las solicitudes y las respuestas, que ya vimos antes.
Al final de esta lección, sabrás cómo se comportan las APIs de los almacenes y estarás listo para probarlas.
Explorar la documentación con Apidoc
Antes de avanzar, vamos a ver lo que conocemos hasta ahora:
  

1. Identifica los endpoints correctos
Según el desglose de tu tarea, necesitas verificar la disponibilidad de productos en los almacenes Everything you Need y Fresh Food. También conoces las entradas necesarias:
  

Tu objetivo ahora es:
🔎 Encontrar los endpoints que manejan esa lógica.
Cómo hacerlo en Apidoc
Abre Apidoc
Servidor
¡Genial, tu servidor ha sido iniciado!
Dirección del servidor: https://cnt-a1f9e287-9698-4f8c-ba6d-831146e194c5.containerhub.tripleten-services.com
Reiniciar el servidor
                           * Primero, necesitas iniciar el servidor. Haz clic en el botón de arriba.
                           * Copia la URL y pégala en tu navegador.
                           * Añade /docs/ al final y presiona Enter.
  

Busca los endpoints
                           * En Apidoc, revisa el menú lateral izquierdo y busca las secciones relacionadas con los almacenes, los productos o la disponibilidad.
                           * En cada sección, abre la descripción completa: no te guíes solo por el nombre del endpoint.
                           * Pregúntate:
                           * ¿Recibe productId y quantity como valores de entrada?
                           * ¿Muestra la disponibilidad por almacén?
Pregunta
¿Cuáles de los siguientes endpoints son relevantes para tu tarea?
Elige tantas como quieras
/api/v1/warehouses
/fresh-food/v2.0.1/ct
¡Muy bien! Este es el endpoint correcto para verificar la disponibilidad de productos en el almacén Fresh Food. Acepta una lista de productos con las cantidades y devuelve la disponibilidad, horarios de trabajo y el precio.
/api/wsdl
/api/v1/orders
/everything-you-need/v1/calculate
¡Correcto! Este endpoint gestiona solicitudes de disponibilidad de productos para el almacén Everything you Need. Procesa múltiples productos y devuelve los datos relevantes de disponibilidad.
¡Buen trabajo!
¡Perfecto! Anotemos esta información en una tabla:
Objetivo de prueba
	Endpoint
	Método HTTP
	¿Requiere body?
	Formato de entrada
	Campos obligatorios
	Campos opcionales
	La respuesta incluye
	Códigos de estado esperados
	Verificar disponibilidad — Fresh Food
	/fresh-food/v2.0.1/ct
	POST
	

	

	

	

	

	

	Verificar disponibilidad — Everything you Need
	/everything-you-need/v1/calculate
	POST
	

	

	

	

	

	

	2. Entiende qué datos necesitas enviar
Ya encontraste los endpoints para Fresh Food y Everything you Need. Ahora te toca descubrir cómo interactuar con ellos.
Para eso, hay una pregunta clave:
¿Cómo debe verse una solicitud válida?
Sabes que necesitas enviar los IDs de producto y sus cantidades. Esto sale en el desglose de tu tarea:
  

Ahora te toca explorar la documentación y confirmar la estructura y el formato exacto de esos datos.
Cómo hacerlo en Apidoc
  

                           * Abre el detalle del endpoint.
                           * Busca la sección "Parámetros" o el ejemplo de solicitud.
                           * Revisa:
                           * ¿Usa JSON?
                           * ¿Qué campos son obligatorios y qué tipo tienen?
                           * ¿Hay estructuras anidadas como arrays?
                           * ¿Hay campos opcionales?
💡
Revisa tanto la lista de campos como el ejemplo: a veces la información solo está en uno de ellos.
Pregunta
¿Qué campos deben incluirse en una solicitud válida para verificar la disponibilidad de productos?
(Según el cuerpo de la solicitud mostrado en Apidoc para ambos endpoints.)
Elige tantas como quieras
products (array de objetos)
¡Exactamente! El cuerpo de la solicitud debe incluir un array de productos: cada uno con productId y quantity.
clientId (string)
deliveryTime (number)
¡Así es! El cuerpo de la solicitud incluye el parámetro deliveryTime que indicará el plazo de entrega del envío.
productId (número)
¡Bien hecho! Este campo es obligatorio: le indica a la API qué producto quieres consultar.
quantity (número)
¡Correcto! Este campo es obligatorio: define cuántas unidades estás solicitando.
¡Lo has entendido bien!
¡Perfecto! Agreguemos estos resultados:
Objetivo de prueba
	Endpoint
	Método HTTP
	¿Requiere body?
	Formato de entrada
	Campos obligatorios
	Campos opcionales
	La respuesta incluye
	Códigos de estado esperados
	Verificar disponibilidad — Fresh Food
	/fresh-food/v2.0.1/ct
	POST
	✅ Sí
	JSON
	productId, quantity, products (required),
	deliveryTime(en array)
	

	

	Verificar disponibilidad — Everything you Need
	/everything-you-need/v1/calculate
	POST
	✅ Sí
	JSON
	productId, quantity, products (required),
	deliveryTime(en array)
	

	

	

	

	

	

	

	

	

	

	

	3. Entiende qué te dice la respuesta
Antes de hacer las pruebas, asegúrate de entender cómo interpretar la respuesta, tanto si funciona bien como si falla.
💡
Piensa como un QA engineer: ¿Qué confirma esta respuesta? ¿Y si algo sale mal? Ten claro qué es un éxito, qué datos debes validar y cómo las entradas afectan los resultados.
En el análisis previo de la tarea también definiste qué tipo de salida esperar: el estado de disponibilidad y las cantidades.
Esta es la línea que lo indicaba:
  

Ahora, veamos la documentación y entendamos cómo aparece exactamente esa información en la respuesta de la API.
En Apidoc:
  

                           * Abre el endpoint y baja hasta la respuesta de ejemplo.
                           * Revisa:
                           * Estructura general: ¿Es un objeto? ¿Un array?
                           * Campos y su significado.
                           * Indicadores de éxito/error (status, available...).
                           * Cómo muestra la disponibilidad.
                           * ¿Se documentan mensajes de error o códigos de estado?
Pregunta
¿Qué campos de la respuesta te ayudan a validar la disponibilidad de productos?
Elige tantas como quieras
isItemsAvailable
¡Muy bien! Este campo puede indicar éxito o problemas con la disponibilidad.
warehouseName
availableProducts
¡Bien! Este campo indica si el producto está en stock y se puede entregar.
Id (product)
¡Correcto! Te ayuda a relacionar la respuesta con tu solicitud original.
requestedQuantity
quantity (in stock)
¡Exactamente! Te permite comparar cuánto hay disponible con la cantidad que solicitaste.
¡Lo has entendido bien!
¡Increíble! Vamos a anotar esto también:
Objetivo de prueba
	Endpoint
	Método HTTP
	¿Requiere body?
	Formato de entrada
	Campos obligatorios
	Campos opcionales
	La respuesta incluye
	Códigos de estado esperados
	Verificar disponibilidad — Fresh Food
	/fresh-food/v2.0.1/ct
	POST
	✅ Sí
	JSON
	productId, quantity, products (required),
	deliveryTime(en array)
	productId, available, quantityInStock, status
	presente
	Verificar disponibilidad — Everything you Need
	/everything-you-need/v1/calculate
	POST
	✅ Sí
	JSON
	productId, quantity, products (required),
	deliveryTime(en array)
	productId, available, quantityInStock, status
	presente
	4. Verifica cómo interpretar los códigos de estado
Antes de hacer las pruebas, asegúrate de entender qué códigos devuelve la API y qué significan en tu caso.
Ya sabes que el objetivo es comprobar si los almacenes pueden satisfacer la lista de productos:
  

Por eso debes saber:
                           * Qué confirma un 200 OK.
                           * Cómo se ve un error.
                           * Qué revisar en el cuerpo además del código.
En Apidoc
  

                           * Abre la documentación del endpoint.
                           * Busca la sección llamada Códigos de estado (o revisa las respuestas de ejemplo).
                           * Para cada código listado, pregúntate:
                           * ¿Qué situación provoca esta respuesta?
                           * ¿Qué significa desde el punto de vista del usuario?
                           * ¿Qué deberías revisar en el cuerpo además del estado?
💡
Algunas APIs devuelven 200 incluso cuando faltan productos: la pista importante está en el cuerpo de la respuesta.
Pregunta
¿Qué códigos de estado podrías esperar al verificar la disponibilidad de productos?
Elige tantas como quieras
404 Not Found
400 Bad Request
¡Exacto! Aparece si envías una solicitud mal formada, por ejemplo, si faltan campos obligatorios.
500 Internal Server Error
200 OK
¡Correcto! Significa que la solicitud fue válida y procesada. Pero aún necesitas revisar el cuerpo para ver la disponibilidad.
¡Bien hecho!
¡Genial! Actualicemos la información:
Objetivo de prueba
	Endpoint
	Método HTTP
	¿Requiere body?
	Formato de entrada
	Campos obligatorios
	Campos opcionales
	La respuesta incluye
	Códigos de estado esperados
	Verificar disponibilidad — Fresh Food
	/fresh-food/v2.0.1/ct
	POST
	✅ Sí
	JSON
	productId, quantity, products (required),
	deliveryTime(en array)
	productId, available, quantityInStock, status
	200 OK, 400 Bad Request
	Verificar disponibilidad — Everything you Need
	/everything-you-need/v1/calculate
	POST
	✅ Sí
	JSON
	productId, quantity, products (required),
	deliveryTime(en array)
	productId, available, quantityInStock, status
	200 OK, 400 Bad Request
	5. Esboza qué vas a probar
Después de explorar la API, puedes definir los escenarios que vas a probar, según lo que permite la documentación y lo que exige el objetivo.
  

Ya que sabes qué espera la API y cómo responde, por lo que puedes definir qué quieres probar: tanto cuando todo funciona bien como cuando algo puede salir mal.
Para ello, considera:
                           * Qué debería pasar si se introducen datos válidos.
                           * Qué pasa si faltan productos o cantidades.
                           * Qué ocurre con las solicitudes mal formadas.
💡
Usa esta fórmula:
→ Dado este input, el sistema debería responder así. Ej.: Si la contraseña es incorrecta, debería recibir 401 Unauthorized.
Pregunta
¿Cuáles de las siguientes son ideas de prueba válidas según la documentación?
Elige tantas como quieras
Enviar una solicitud con cero productos y esperar un 200 OK
Enviar una solicitud válida con productId y quantity, y esperar una respuesta clara sobre la disponibilidad
¡Exacto! Esta es la prueba base: asegúrate de que el flujo esperado funcione.
Omitir el campo quantity y esperar un 400
¡Sí! Esto comprueba directamente cómo maneja la API una entrada mal formada.
Enviar una cantidad muy alta y comprobar cómo responde la API
¡Muy bien pensado! Este es un caso límite válido: te ayuda a explorar cómo el sistema gestiona las restricciones de stock.
Enviar el mismo producto dos veces y esperar que se sumen
Solicitar un producto que no esté en la lista y comprobar si aparece como no disponible
¡Buena idea! Verifica cómo la API maneja productos desconocidos o faltantes.
¡Buen trabajo!
¡Perfecto! Ahora tienes todo listo para pasar al siguiente paso del flujo de pruebas de API.
Objetivo de prueba
	Endpoint
	Método
	Campos requeridos
	La respuesta incluye
	Códigos de estado
	Notas (ideas de prueba)
	Verificar disponibilidad — Fresh Food
	/fresh-food/v2.0.1/ct
	POST
	productId, quantity, products (required)
	available, quantityInStock
	200 OK, 400 Bad Request
	- Probar con un producto y cantidad válidos.
- Usar un ID de producto inexistente.
- Omitir un campo obligatorio.
- Enviar una cantidad muy grande para comprobar los límites.
	Verificar disponibilidad — Everything you Need
	/everything-you-need/v1/calculate
	POST
	productId, quantity, products (required)
	available, quantityInStock
	200 OK, 400 Bad Request
	Y, por último, la documentación de la API confirma el comportamiento esperado para una solicitud válida.
	Valoración de la lección
Siguiente


Sprint 4: Pruebas de API
Capítulo 4/6 · Faltan 6 lecciones
Pruebas de API: Preparación y Ejecución
35 min
Pruebas positivas
En el capítulo anterior, aprendiste a analizar la documentación de una API, y de esta forma también completando el Paso 2 del flujo de pruebas.
El siguiente paso sería configurar el entorno (Paso 3), pero eso ya lo hiciste antes:
                           * Creaste un entorno de Postman con una URL base y variables.
                           * Organizaste los endpoints en una colección.
Entonces, ahora puedes avanzar al Paso 4: Probar los endpoints de la API.
  

¿Qué implica esta etapa de pruebas?
El Paso 4 es donde realmente comienzan las pruebas —y en muchos aspectos, el proceso es similar al que realizamos cuando hacemos las pruebas de frontend—.
Sigue este flujo:
  

Durante este proceso, aplicarás las mismas técnicas que ya usaste en otros tipos de pruebas, incluyendo: pruebas positivas y negativas, clases de equivalencia y valores límite, tablas de decisión y pruebas por pares.
Comencemos por las más fundamentales: las pruebas positivas.
Pruebas positivas para API
Las pruebas positivas son como encender un coche para ver si arranca. Si ni siquiera arranca, no tiene sentido revisar los frenos o los sensores de reversa.
  

Si una solicitud es válida, la API debe devolver una respuesta exitosa: con el código de estado correcto y todos los campos esperados.
Los casos de prueba positivos verifican que la aplicación funcione sin errores en dos situaciones:
                           * Si la usas según lo previsto y no intentas forzar errores.
                           * Si introduces datos válidos de acuerdo con los requisitos.
Vamos a seguir este proceso paso a paso para completar tu tarea de QA.
1. Diseña los casos de prueba
Requisitos y documentación
Para probar una API, necesitas dos fuentes clave:
  

Los requisitos del backend te dicen:
                           * Qué productos verificar.
                           * Qué almacenes están involucrados.
                           * Qué se considera un éxito o un fallo.
Usa ambas fuentes para crear tus casos de prueba.
Diseño paso a paso
Empezaremos diseñando casos de prueba positivos para confirmar que el sistema se comporta correctamente en condiciones ideales. Es decir: entrada válida → respuesta exitosa.
Queremos verificar si el almacén Everything You Need puede responder a una solicitud para los productos 1, 4 y 44 en cantidades específicas.
Paso 1. Define tu escenario positivo
Antes de elegir datos, aclara qué estás probando y cómo se ve el resultado si todo va bien. A esto lo llamamos Happy Path: entradas válidas, sin errores.
En la documentación ya propusiste:
                           * Probar con un producto y cantidad válidos.
También viste el método, endpoint, campos requeridos y código esperado.
Extracto de la documentación
Para confirmar esta idea, acudes a los Requisitos del backend, que dicen:
El usuario solo puede pedir una cantidad completamente disponible de un artículo en al menos uno de los almacenes.
Parece que ahora ya estamos listos para definir el escenario:
Pregunta
¿Cuál de los siguientes es el mejor escenario de Happy Path para esta tarea?
El usuario envía una solicitud para productos disponibles en múltiples almacenes y espera que la API elija la opción más económica.
El usuario envía una solicitud POST correctamente estructurada con los campos obligatorios (productId, quantity, products), además del campo opcional (deliveryTime) al endpoint correcto y los productos están en stock. Se espera una respuesta 200 OK.
¡Exacto! Este es un Happy Path válido. Los datos de entrada son correctos, los productos están disponibles y se espera que la API devuelva una respuesta exitosa.
El usuario envía una solicitud al endpoint /everything-you-need/v1/calculate con los ID de producto válidos, pero omite el campo quantity. El sistema debería devolver los datos de disponibilidad de los productos.
¡Lo has entendido bien!
Paso 2. Elige datos válidos para la prueba
Una vez definido el Happy Path, es momento de seleccionar los valores específicos que usarás para probarlo:
El usuario envía una solicitud POST correctamente estructurada con los campos obligatorios (productId, quantity) al endpoint correcto y los productos están en stock. Se espera una respuesta 200 OK.
Para que esto funcione, los datos deben coincidir con lo que espera el sistema.
Esta información suele venir en la descripción de la tarea o en los requisitos. En este caso:
                           * Producto 1: 2 unidades.
                           * Producto 4: 3 unidades.
                           * Producto 44: 1 unidad.
Empezaremos con el producto 1 (productId: 1, quantity: 2): parece estar disponible, así que es ideal para una prueba positiva.
Vamos a escribir el caso de prueba:
ID
	Nombre del caso de prueba
	Condición previa
	Paso
	Descripción del paso
	Resultado esperado
	TC01
	Solicitud válida devuelve información de disponibilidad de producto existente y su cantidad existente.
	El sistema del almacén está activo y contiene el producto con ID 1 con al menos 2 unidades en stock
	1
	Enviar una solicitud POST a /everything-you-need/v1/calculate con productId: 1, quantity: 2
	La API devuelve 200 OK y confirma la disponibilidad del producto
	2. Ejecuta la prueba: envía la solicitud
Servidor
Iniciar
¿Prefieres leer? Haz clic aquí para ver la transcripción.
3. Verifica e interpreta la respuesta
Una vez enviada la solicitud, tu primera validación es el código de respuesta.
“¿Se procesó la solicitud correctamente?”
Pregunta
¿Qué código de estado confirma que la solicitud se realizó correctamente en este caso?
400 Bad Request
201 Created
200 OK
Correcto. Esto es lo que esperamos en una consulta de disponibilidad.
404 Not Found
¡Buen trabajo!
4. Compara los resultados con las expectativas
Ahora que ya tienes el cuerpo de respuesta, te toca hacer lo más importante: ver si cumple con las expectativas. Compara los datos de salida de la respuesta contra los que obtuviste.
Aquí tienes un ejemplo de respuesta de la documentación:
  

Pregunta
Compara la respuesta que obtuviste en Postman con lo que se espera según la documentación en Apidoc. ¿Qué conclusiones puedes sacar sobre su validez?
Faltan campos importantes como clientId o deliveryEstimate.
Todos los campos principales están presentes y coinciden con lo que se esperaba.
Correcto. Esta respuesta cumple con la documentación y refleja una solicitud exitosa.
La API devolvió un estado 201, por lo tanto no fue una respuesta válida.
availableProducts tiene datos, pero isItemsAvailable debería ser false.
¡Lo has entendido bien!
¡Genial! Vamos a añadirlo al caso de prueba.
ID
	Nombre del caso de prueba
	Condición previa
	Paso
	Descripción del paso
	Resultado esperado
	Resultado actual
	TC01
	Solicitud válida devuelve información de disponibilidad de producto existente y su cantidad existente.
	El sistema del almacén está activo y contiene el producto con ID 1 con al menos 2 unidades en stock.
	1
	Enviar una solicitud POST a /everything-you-need/v1/calculate con productId: 1, quantity: 2
	La API devuelve 200 OK y confirma la disponibilidad del producto.
	La API devolvió 200 OK. La respuesta incluyó los campos esperados: availableProducts, isItemsAvailable, etc.
	5. Registra el resultado
Ya ejecutaste la prueba y confirmaste que la respuesta coincide con el resultado esperado. Ahora te toca documentar lo que ocurrió.
Este paso final completa tu caso de prueba. Ya tienes el escenario, los pasos y el resultado esperado. Solo te falta añadir el estado, para que tu prueba sea reutilizable, revisable y clara para otras personas.
Pregunta
¿Cuál es el estado correcto para este caso de prueba?
¡Buen trabajo! “Aprobado” significa que la prueba se ejecutó correctamente y los resultados actuales coincidieron con los esperados, justo como en este caso.
¡Lo has entendido bien!
Aquí tienes el caso de prueba completo con el resultado incluido:
ID
	Nombre del caso de prueba
	Condición previa
	Paso
	Descripción del paso
	Resultado esperado
	Resultado actual
	Estado
	TC01
	Solicitud válida devuelve información de disponibilidad de producto existente y su cantidad existente.
	El sistema del almacén está activo y contiene el producto con ID 1 con al menos 2 unidades en stock.
	1
	Envía una solicitud POST a /everything-you-need/v1/calculate con productId: 1, quantity: 2.
	La API devuelve 200 OK y confirma la disponibilidad del producto.
	La API devolvió 200 OK. La respuesta incluyó los campos esperados: availableProducts, isItemsAvailable, etc.
	Aprobado
	💡
Tarea adicional: haz pruebas positivas con los demás productos y con el almacén Fresh Food, usando el mismo enfoque.
Crea pruebas positivas para API usando IA
Sigues a cargo de la tarea de probar la disponibilidad de los almacenes de Urban Grocers. Ahora toca probar la disponibilidad del almacén Fresh Food.
Haz clic aquí para ver la lección en formato de texto.
Entrada
Fragmento de la documentación de API
Objetivo de prueba
	Endpoint
	Método HTTP
	¿Requiere body?
	Formato de entrada
	Campos obligatorios
	Campos opcionales
	La respuesta incluye
	Códigos de estado esperados
	Verificar disponibilidad — Fresh Food
	/fresh-food/v2.0.1/ct
	POST
	✅ Sí
	JSON
	productId, quantity, products (required),
	deliveryTime(en array)
	productId, available, quantityInStock, status
	200 OK, 400 Bad Request
	Requisitos
El usuario solo puede pedir una cantidad completamente disponible de un artículo en al menos uno de los almacenes.
Prompt para generar casos positivos para API
Actúa como un QA Engineer con experiencia en pruebas de APIs REST, análisis de documentación técnica y diseño de casos de prueba funcionales. Tu enfoque debe ser generar casos de prueba positivos claros, estructurados y alineados con la documentación proporcionada.
Entrada / Contexto Documentación de la API (endpoints, métodos HTTP, parámetros, headers, body, códigos de respuesta, ejemplos). Texto ó archivo de texto con documentación de backend (reglas de negocio, validaciones, restricciones, descripciones funcionales, flujos esperados).
Ambos describen el comportamiento esperado del sistema.
Reglas y Restricciones -Genera únicamente casos de prueba positivos (escenarios donde el sistema debe funcionar correctamente). -No incluyas casos negativos, validaciones de error ni escenarios de falla. -No inventes endpoints, campos, reglas o comportamientos que no estén explícitamente definidos en la documentación. -No mezcles escenarios positivos con validaciones negativas. -Si algún campo o comportamiento no está claramente definido, omítelo. -Cada caso debe validar que el sistema cumple correctamente con lo especificado. -Usa terminología técnica adecuada para pruebas de API.
Salida Requerida Genera una lista estructurada de casos de prueba en formato tabla con las siguientes columnas: -ID -Nombre -Precondiciones -Número de paso -Descripción del paso -Resultado esperado
Lista de validación de los casos de prueba generados con la IA
Lista de validación de los casos de prueba generados con la IA
El nombre del caso de prueba coincide con lo que se prueba.
Las precondiciones del caso de prueba coinciden con lo que se prueba.
No inventa endpoints ni campos que no estén en la documentación.
Los resultados esperados son positivos.
Los casos de prueba no se repiten.
Los casos de prueba cubren todos los requisitos.
¡Buen trabajo!
Pregunta
Una vez que tengas tus casos de prueba refinados pega el siguiente mensaje de seguimiento en el mismo chat donde generaste los casos de prueba:
Dame en formato de Markdown la tabla del caso de prueba que generaste para probar la disponibilidad total del almacén
📌 Qué debes enviar aquí:
Pega únicamente la tabla devuelta por la IA en el mensaje de seguimiento anterior. Para copiar la tabla da click en el botón de Copiar en la esquina superior derecha de la tabla.
| ID | Nombre | Precondiciones | Número de paso | Descripción del paso | Resultado esperado |
|-----|---------|----------------|-----------------|----------------------|-------------------|
| TC_API_001 | Consultar disponibilidad de un producto con stock disponible | El producto existe y la cantidad solicitada está completamente disponible en al menos uno de los almacenes. | 1 | Enviar una solicitud POST al endpoint `/fresh-food/v2.0.1/ct`. | La solicitud es procesada correctamente. |
| TC_API_001 | Consultar disponibilidad de un producto con stock disponible | El producto existe y la cantidad solicitada está completamente disponible en al menos uno de los almacenes. | 2 | Incluir en el body JSON los campos obligatorios `productId`, `quantity` y `products`. | El servicio acepta la estructura de entrada definida. |
| TC_API_001 | Consultar disponibilidad de un producto con stock disponible | El producto existe y la cantidad solicitada está completamente disponible en al menos uno de los almacenes. | 3 | Ejecutar la petición. | El servicio responde con código de estado 200 OK. |
| TC_API_001 | Consultar disponibilidad de un producto con stock disponible | El producto existe y la cantidad solicitada está completamente disponible en al menos uno de los almacenes. | 4 | Verificar el contenido de la respuesta. | La respuesta incluye los campos `productId`, `available`, `quantityInStock` y `status`. |
Veredicto: Casi correcto
Has identificado correctamente:
                           * La tabla incluye todas las columnas requeridas.
                           * Los resultados esperados son positivos y están relacionados con la disponibilidad total del almacén.
                           * Los pasos y precondiciones están alineados con el caso de prueba descrito.
Esto es lo que se debe ajustar:
                           * El formato de la tabla no sigue estrictamente el formato esperado, ya que incluye líneas adicionales y caracteres de escape innecesarios. Asegúrate de que la tabla esté correctamente estructurada y limpia para facilitar su lectura y comprensión.
Feedback IA
Reenviar
¡Buen trabajo! Ahora ya sabes cómo hacer una prueba positiva para una API sin interfaz visual, solo con solicitudes y respuestas.
A continuación: ¿qué pasa cuando algo falla? ¡Vamos a verlo!
Valoración de la lección
Siguiente



Sprint 4: Pruebas de API
Capítulo 4/6 · Faltan 5 lecciones
Pruebas de API: Preparación y Ejecución
30 min
Pruebas negativas
Ya conoces el propósito de las pruebas negativas: asegurarte de que el sistema no acepte datos no válidos y maneje los errores de forma adecuada.
Ahora vamos a aplicar esa idea a las pruebas de APIs.
¿Cómo es una prueba negativa en APIs?
En el contexto de APIs, una prueba negativa implica:
                           * Enviar datos no válidos o incompletos.
                           * Usar el método o el endpoint incorrecto.
                           * Romper intencionalmente la solicitud.
                           * Esperar a que el sistema rechace la entrada y devuelva el mensaje de error correspondiente.
Así te aseguras de que el backend responde de forma adecuada: sin fallos, sin exponer datos confidenciales y sin fallar en silencio. En proyectos reales, las pruebas negativas ayudan a detectar errores del backend a tiempo, especialmente en la lógica de validación y seguridad.
Pruebas negativas
¡Vamos a probarlo! Mismo flujo, diferentes expectativas.
Seguirás exactamente los mismos pasos del flujo de pruebas de API:
  

Pero esta vez, esperarás que falle, y eso es lo que buscamos.
1. Diseña los casos de prueba negativos
Comencemos con la misma API:
POST /everything-you-need/v1/calculate
La documentación indica que productId y quantity son obligatorios.
Objetivo de prueba
	Endpoint
	Método
	Campos requeridos
	La respuesta incluye
	Códigos de estado
	Notas (ideas de prueba)
	Verificar la disponibilidad — Everything you need
	/everything-you-need/v1/calculate
	POST
	productId, quantity
	available, quantityInStock
	200 OK, 400 Bad Request
	Y, por último, la documentación de la API confirma el comportamiento esperado para una solicitud válida.
	También muestra el formato aceptado:
  

Eso nos da muchas posibilidades para realizar pruebas negativas.
Ya usaste esta documentación para probar entradas válidas. Ahora vamos a darle la vuelta a la situación y a preguntarnos: ¿Qué podría salir mal?
Pregunta
¿Cuál de las siguientes son ideas válidas para hacer pruebas negativas en esta API?
Elige tantas como quieras
Usar un productId no válido (productId: "abc")
¡Exacto! Esto prueba cómo responde el sistema ante datos inexistentes o no admitidos: un escenario clásico de prueba negativa.
Enviar la solicitud mediante el método GET en lugar de POST
Enviar una solicitud POST con productId y quantity válidos
Enviar una solicitud con un tipo de dato incorrecto para quantity
¡Bien pensado! Esto verifica cómo maneja la API los tipos de datos incorrectos. quantity debe ser un número, así que usar un string es una prueba negativa válida.
Enviar una solicitud sin el campo quantity
¡Buena observación! Esta entrada está incompleta: según la documentación, quantity es obligatorio. Si falta se debería generar un error.
¡Excelente trabajo!
Elijamos esta idea de prueba negativa: enviar una solicitud con un tipo de dato incorrecto para quantity.
Pregunta
Quieres comprobar cómo maneja la API una quantity no válida; más en específico, un tipo de dato incorrecto. ¿Cuál de las siguientes solicitudes implementaría correctamente esta prueba?
Enviar una solicitud POST con "quantity": null
Enviar una solicitud POST con "quantity": 0 
Enviar una solicitud POST con "quantity": "two"
¡Excelente! Esto envía un string en lugar de un número, un error clásico de tipo de dato. La API espera un entero, por lo que esto debería devolver 400 Bad Request.
Enviar una solicitud POST con "quantity": -3
¡Perfecto!
¡Genial! Vamos a añadir todos nuestros hallazgos al caso de prueba.
ID
	Nombre del Caso de Prueba
	Condición previa
	Paso
	Descripción del Paso
	Resultado Esperado
	

	TC02
	Ingresar tipo de dato “string” en el campo numérico quantity genera código de error 400.
	El sistema de almacén está activo
	1
	Enviar una solicitud POST a /everything-you-need/v1/calculate con productId: 1, quantity: "two"
	La API devuelve 400 Bad Request y un mensaje de error apropiado
	

	2. Envía la solicitud
Servidor
¡Genial, tu servidor ha sido iniciado!
Dirección del servidor: https://cnt-458ec84b-ce2a-4b2d-a688-276735a2e826.containerhub.tripleten-services.com
Reiniciar el servidor
¿Prefieres leer? Haz clic aquí para ver la transcripción.
¡Ahora toca ejecutar la prueba! Usaremos esta solicitud para comprobar si la API rechaza correctamente los datos con el tipo incorrecto.
Usaremos el mismo extracto de documentación para construir nuestra solicitud, pero siempre puedes revisarlo en Apidoc.
Extracto de la documentación
Elemento clave
	Documentación:
	Endpoint
	/everything-you-need/v1/calculate
	Método
	POST
	Cuerpo esperado
	{
"deliveryTime": 9,
"products": [
{ "id": 1,
"quantity": 1
},
{ "id": 4,
"quantity": 3
}
]
}
	Respuesta esperada
	{
"name": "Everything You Need",
"workingHours": { "start": 8, "end": 23 },
"price": 10,
"availableProducts": [
{ "id": 1, "quantity": 2 }
],
"isWarehouseWorking": true,
"isItemsAvailable": false,
"percentOfAvailableItems": 50
}
	Código de estatus
	200 OK
	Vamos a reutilizar la misma solicitud que creaste antes para Everything You Need.
                           * En Postman, abre tu solicitud anterior al endpoint /everything-you-need/v1/calculate.
                           * Asegúrate de que el método esté configurado como POST.
                           * Mantén la estructura original del body.
                           * Introduce el valor no válido.
Para esta prueba negativa, romperás intencionalmente una regla:
→ En lugar de enviar un quantity numérico, enviarás un string de texto: “two”
                           * Envía la solicitud.
3. Interpreta la respuesta
Esta vez, no queremos un 200 OK, esperamos un error: lo más probable es que obtengamos un 400 Bad Request.
El mensaje exacto puede variar, pero la respuesta debe indicar que algo salió mal debido a una entrada no válida.
Pregunta
¿Qué código de estado obtuviste?
404 Not Found
500 Internal Server Error
400 Bad Request
200 OK
¡Exacto! Esta es la respuesta correcta para una solicitud bien formada que contiene datos válidos. En este caso, se esperaba una respuesta un poco diferente. ¡Haz encontrado un bug!
¡Buen trabajo!
4. Compara los resultados con las expectativas
En esta prueba, enviaste intencionalmente un tipo de dato incorrecto, two, como string en lugar de una quantity numérica.
Aunque la documentación no menciona este caso específico, sí indica claramente que quantity debe ser un número. Así que, cuando el sistema recibe un string, trata la solicitud como no válida.
Por eso esperábamos que la API devolviera un 400 Bad Request.
Y en este caso, obtuviste un 200 OK indicando que la solicitud fue procesada con éxito. Esto quiere decir que encontraste un defecto.
Aquí tienes el caso de prueba actualizado con el resultado actual:
ID
	Nombre del Caso de Prueba
	Condición previa
	Paso
	Descripción del Paso
	Resultado Esperado
	Resultado Actual
	TC02
	Ingresar tipo de dato “string” en el campo numérico quantity genera código de error 400.
	El sistema está activo y espera que quantity sea numérico
	1
	Envía una solicitud POST a /everything-you-need/v1/calculate con quantity: "two" (un string)
	La API devuelve 400 Bad Request
	La API devolvió 200 OK.
	5. Registra el resultado
Ya ejecutaste tu prueba y confirmaste la respuesta. Ahora es el momento de documentar el resultado. Este paso final completa tu caso de prueba; haciéndolo reutilizable, revisable y fácil de entender para otras personas.
Finaliza tu caso de prueba añadiendo el estado:
Pregunta
¿Cuál es el estado correcto para este caso de prueba?
¡Buen trabajo! “Fallado” significa que el resultado esperado y el resultado real de la prueba tuvieron alguna diferencia.
¡Excelente trabajo!
Aquí tienes la versión final de tu caso de prueba, ahora con el estado incluido:
ID
	Nombre del caso de prueba
	Condición previa
	Paso
	Descripción del paso
	Resultado esperado
	Resultado actual
	Estado
	TC02
	Ingresar tipo de dato “string” en el campo numérico quantity genera código de error 400.
	El sistema está activo y espera que quantity sea un número.
	1
	Enviar una solicitud POST a /everything-you-need/v1/calculate con quantity: "two" (un string).
	La API devuelve 400 Bad Request.
	La API devolvió 200 OK .
	Falló
	💡
Tarea adicional:
Escribe y ejecuta al menos una prueba negativa más para esta API.
Prueba eliminando otro campo o ingresando un tipo de dato no válido. También puedes intentar terminar esta tarea para el almacén Fresh Food.
Completaste un caso de prueba negativo completo para una API a través de validaciones reales y la lógica de manejo de errores. Es otra habilidad clave de QA que ya dominas.
En la siguiente lección hablaremos sobre cómo usar las clases de equivalencia en APIs.
Crea pruebas negativas para API usando IA
Veamos cómo la IA puede ayudarnos a diseñar casos de prueba negativos para Fresh Food.
Paso 1. Entiende la tarea
Para esta tarea, utiliza la misma entrada que usaste para generar los casos de prueba positivos. Abre el mismo chat donde trabajaste anteriormente y continúa allí.
Paso 2. Formula una tarea clara para la IA (Prompt)
Prompt para generar casos negativos para API
Actúa como un QA Engineer con experiencia en pruebas de APIs REST, análisis de documentación técnica y diseño de casos de prueba funcionales. Tu enfoque debe ser generar casos de prueba negativos claros, estructurados y alineados estrictamente con la documentación proporcionada.
Entrada / Contexto
                              * Usa la misma entrada/contexto que usaste para generar casos de prueba positivos.
Reglas y Restricciones
                              * Genera únicamente casos de prueba negativos (escenarios donde el sistema debe rechazar la solicitud o devolver un error).
                              * No incluyas casos positivos ni escenarios donde la operación sea exitosa.
                              * No inventes endpoints, campos, reglas, validaciones o comportamientos que no estén explícitamente definidos en la documentación.
                              * Cada caso negativo debe estar basado en una validación, restricción o regla documentada.
                              * No mezcles varios errores en un mismo caso de prueba.
                              * Si un campo, validación o comportamiento no está claramente definido, omítelo.
                              * Usa terminología técnica adecuada para pruebas de API.
Salida Requerida
Genera una lista estructurada de casos de prueba en formato tabla con las siguientes columnas:
                              * ID
                              * Nombre
                              * Precondiciones
                              * Número de paso
                              * Descripción del paso
                              * Resultado esperado (incluyendo el error esperado y código de respuesta si aplica)
Paso 3. Genera los casos de prueba
Paso 4. Refina el resultado
Lista de validación de los casos de prueba generados con la IA
Lista de validación de los casos de prueba generados con la IA
El nombre del caso de prueba coincide con lo que se prueba.
Las precondiciones del caso de prueba coinciden con lo que se prueba.
Los resultados esperados son negativos.
No inventa endpoints ni campos que no estén en la documentación.
Los casos de prueba no se repiten.
Los resultados esperados son códigos de error que aparecen en la documentación de la API.
¡Tu comprensión del material es impresionante!
Pregunta
Una vez que tengas tus casos de prueba refinados pega el siguiente mensaje de seguimiento en el mismo chat donde generaste los casos de prueba:
Dame en formato de Markdown la tabla de uno de los casos de prueba negativos que generaste
📌 Qué debes enviar aquí:
Pega únicamente la tabla devuelta por la IA en el mensaje de seguimiento anterior. Para copiar la tabla da click en el botón de Copiar en la esquina superior derecha de la tabla.
IDNombrePrecondicionesNúmero de pasoDescripción del pasoResultado esperado (incluyendo el error esperado y código de respuesta si aplica)
CPN-001
Solicitud sin campo quantity
El endpoint /everything-you-need/v1/calculate está disponible
1
Enviar una solicitud POST con un elemento de products que incluya id, pero omita el campo quantity.
La solicitud es rechazada y la API devuelve un error 400 Bad Request.
CPN-002
Solicitud sin campo id del producto
El endpoint /everything-you-need/v1/calculate está disponible
1
Enviar una solicitud POST con un elemento de products que incluya quantity, pero omita el campo id.
La solicitud es rechazada y la API devuelve un error 400 Bad Request.
CPN-003
Solicitud sin campo deliveryTime
El endpoint /everything-you-need/v1/calculate está disponible
1
Enviar una solicitud POST omitiendo el campo deliveryTime del cuerpo de la petición.
La solicitud es rechazada y la API devuelve un error 400 Bad Request.
CPN-004
Solicitud sin lista de productos
El endpoint /everything-you-need/v1/calculate está disponible
1
Enviar una solicitud POST omitiendo el campo products del cuerpo de la petición.
La solicitud es rechazada y la API devuelve un error 400 Bad Request.
Veredicto: No es correcto
Has identificado correctamente:
                              * La respuesta incluye casos de prueba negativos.
Esto es lo que se debe ajustar:
                              * La tabla no sigue el formato requerido, ya que no incluye las columnas especificadas en las instrucciones (ID, Nombre, Precondiciones, Número de paso, Descripción de paso, Resultado esperado).
                              * Los endpoints utilizados en los casos de prueba no coinciden con los especificados en la documentación proporcionada (/fresh-food/v2.0.1/ct).
                              * Los resultados esperados deben ser códigos de error que aparecen en la documentación proporcionada.
Feedback IA
Reenviar
Completaste un caso de prueba negativo completo para una API a través de validaciones reales y la lógica de manejo de errores. Es otra habilidad clave de QA que ya dominas.
En la siguiente lección hablaremos sobre cómo usar las clases de equivalencia en APIs.
Valoración de la lección
Siguiente
Sprint 4: Pruebas de API
Capítulo 4/6 · Faltan 4 lecciones
Pruebas de API: Preparación y Ejecución
45 min
Clases de equivalencia
Cuando trabajas con endpoints que aceptan varios parámetros —como quantity, productId o deliveryTime— no necesitas probar todos los valores posibles.
En una lección anterior, sin darte cuenta, ya usaste clases de equivalencia para agrupar los valores en válidos y no válidos.
Ahora vas a aplicar esa misma lógica para diseñar pruebas más eficientes para los endpoints de los almacenes.
¿Cómo funcionan las clases de equivalencia en las APIs?
En las pruebas de API, aplicar clases de equivalencia implica:
                              * Identificar valores de entrada clave, como quantity, productId o deliveryTime.
                              * Agruparlos en clases válidas y no válidas.
                              * Probar un solo valor representativo por clase.
                              * Confirmar que la API responde de forma coherente según el tipo de entrada.
Esto permite cubrir muchos escenarios sin probar todos los valores posibles.
En proyectos reales, esta técnica te ayudará a diseñar pruebas más eficientes, centradas en lo que realmente puede fallar, sin duplicar esfuerzos ni perder cobertura.
Pregunta
¿Cuál de las siguientes opciones describe mejor qué es una clase de equivalencia al probar un campo de entrada como quantity en una API?
Un grupo de valores que representan las preferencias del usuario.
Un grupo de pruebas que usan el mismo valor varias veces.
Un grupo de valores de entrada que deberían generar el mismo comportamiento en la API.
Exacto, así funciona. Si el sistema trata todos esos valores de la misma manera, forman una clase de equivalencia.
Un grupo de valores donde cada uno debe generar un error distinto.
¡Bien hecho!
Clases de equivalencia
Entonces, ¿comenzamos? La idea es la misma que antes, ¡solo tienes que aplicarla de forma un poco diferente!
  

Nuestra primera parada será identificar los campos de entrada clave:
Paso 1. Identifica los valores de entrada clave en la documentación:
Seguirás trabajando con el almacén Everything you Need.
Consulta Apidoc y los requisitos del backend.
Servidor
¡Genial, tu servidor ha sido iniciado!
Dirección del servidor: https://cnt-3dd33f57-4289-48b6-8305-f9d1ad96c8af.containerhub.tripleten-services.com
Reiniciar el servidor
Para aplicar clases de equivalencia, comienza por identificar qué campos de la solicitud pueden agruparse como válidos o no válidos.
Según la documentación, los campos clave son quantity, id , deliveryTime y products .
  

quantity field
La documentación dice:
"El usuario o la usuaria solo puede pedir una cantidad completamente disponible de un artículo en al menos uno de los almacenes.”
Esto convierte al campo quantity en un buen candidato para aplicar clases de equivalencia, ya que el sistema espera ciertos valores válidos y debe rechazar otros que no cumplen las condiciones.
Vamos a dividir el espacio de posibles valores en clases válidas e inválidas:
✅ Clases válidas
                              * Cantidades positivas dentro del stock disponible
❌ Clases inválidas
                              * Cantidades mayores al stock disponible
                              * Cero o números negativos
                              * Números decimales (1.5)
                              * Cadenas de texto ("3")
                              * Números excesivamente grandes (999999999999999)
                              * Valores vacíos o nulos (si aplica)
Probar un valor representativo de cada clase ayuda a cubrir todos los comportamientos posibles sin necesidad de probar cada valor individual.
productId
La API requiere el campo id, y ejemplos como 1, 4 y 44 sugieren que espera IDs reales de productos, probablemente validados con el catálogo.
Sin embargo, este campo no es ideal para aplicar clases de equivalencia basadas en rango, como sí ocurre con quantity o deliveryTime. Esto se debe a que productId no representa un valor dentro de un dominio numérico continuo o acotado, sino que se valida contra un catálogo externo.
Por tanto, aunque podamos enviar muchos valores inválidos, no es útil definir clases como “dentro/fuera de rango” o “en el límite”, que es el enfoque de esta técnica.
deliveryTime
El campo deliveryTime aparece en el cuerpo de la solicitud al verificar la disponibilidad de un producto en un almacén. ¡Veamos si podemos usarlo!
  

  

Pregunta
¿Es deliveryTime un buen candidato para aplicarle clases de equivalencia?
No, el campo solo acepta números enteros, así que no hay suficientes casos para agrupar.
No, enviar valores como deliveryTime: 5 o 24 no rompe el sistema, así que no hay nada que probar.
Sí, tiene valores válidos claramente definidos según el horario laboral del almacén (por ejemplo, de 7 a 23).
¡Correcto! Las clases de equivalencia funcionan mejor cuando un campo tiene reglas claras sobre qué valores se aceptan y cuáles no.
Sí, porque horarios más tempranos, como las 8, son mejores para el cliente que horarios más tardíos, como las 22.
¡Lo has entendido bien!
¡Correcto! Los almacenes tienen horarios definidos. Everything You Need, por ejemplo, opera de 7:00 a 23:00.
Si deliveryTime está fuera de ese rango, la solicitud puede ser rechazada. Por eso, es un buen candidato para aplicarle clases de equivalencia:
                              * Dentro del horario = Válido.
                              * Fuera del horario = No válido.
                              * También conviene probar valores no numéricos.
Vamos a reunirlo todo:
  

Tenemos dos buenos candidatos. Empecemos con deliveryTime y pasemos a la parte 2: agruparlos en clases válidas y no válidas.
Paso 2. Define las clases válidas y no válidas para deliveryTime
Este campo indica la hora de entrega y debe estar dentro del horario de operación del almacén Everything you Need, según los requisitos del backend.
  

Pregunta
¿Cuál de los siguientes grupos representa de forma más adecuada las clases de equivalencia para el campo deliveryTime, según los requisitos del almacén?
Válidos: valores positivos | No válidos: negativos
Válidos: cualquier número entero | No válidos: valores decimales
Válidos: 7–23 | No válidos: 0–6
Válidos: 7–23 | No válidos: <7, >23, tipos no numéricos
Correcto. Esta agrupación cubre todos los rangos no válidos relevantes, incluyendo tipos incorrectos como strings o null.
¡Lo has entendido bien!
Esto nos permite definir las siguientes clases:
  

TC01 representa una clase válida: esperamos una respuesta exitosa.
TC02 representa una clase no válida: la API debería rechazarla.
Esta tabla te ayuda a diseñar las pruebas con un solo valor por clase, cubriendo los casos clave sin repetirlos.
Paso 3. Diseña los casos de prueba a partir de estas clases de equivalencia
Entonces, ya tienes lo más importante para empezar a redactar los casos de prueba:
ID
	Nombre del Caso de Prueba
	Condición previa
	Paso
	Descripción del Paso
	Resultado Esperado
	TC01
	Validación de campo “quantity” con cantidades positivas dentro del stock disponible
	El sistema de almacén está activo.
	1
	Enviar una solicitud POST a /everything-you-need/v1/calculate con productId: 1, quantity: 2, deliveryTime: 9
	La API devuelve 200 OK y confirma la disponibilidad del producto
	TC02
	Validación de campo “deliveryTime” con valores fuera del rango de horario laboral.
	El sistema de almacén está activo
	1
	Enviar una solicitud POST a /everything-you-need/v1/calculate con productId: 1, quantity: 2, deliveryTime: 2
	La API devuelve 400 Bad Request debido a que la hora de entrega está fuera del rango workingHours (7–23)
	Ya tienes lo necesario para empezar. Vamos a usar dos valores representativos: uno debería ser aprobado, el otro fallar. ¿Probamos?
Ejecutar y analizar el TC01: deliveryTime válido
Paso 4: Envía la solicitud
Servidor
¡Genial, tu servidor ha sido iniciado!
Dirección del servidor: https://cnt-6b5d4dd7-ceae-4b86-8bba-8c809b6b53d7.containerhub.tripleten-services.com
Reiniciar el servidor
¿Prefieres leer? Haz clic aquí para ver la transcripción.
Ahora vamos a ejecutar la prueba. Este proceso ya lo conoces, pero esta vez el enfoque será diferente: no solo queremos ver si la respuesta es correcta, queremos validar si el comportamiento de la API se corresponde con la clase de equivalencia que definiste.
Consulta la documentación en Apidoc para crear tu solicitud.
Sigue estos pasos:
                              * Abre Postman y crea una nueva solicitud POST: Everything you need: Delivery time.
                              * Utiliza este endpoint: /everything-you-need/v1/calculate
                              * Ve a la pestaña Body, elige raw y selecciona el formato JSON.
                              * Edita el cuerpo con los valores elegidos (productId: 1, quantity: 2, deliveryTime: 9) de nuestro TC01.
                              * Envía la solicitud.
Paso 5: Interpreta la respuesta
Una vez que envíes la solicitud, tu trabajo como QA engineer no terminará con ver “si funcionó o no”, tienes que analizar la respuesta y compararla con el resultado esperado.
Veamos lo que obtuviste en cada caso:
  

Pregunta
¿Cómo deberías interpretar esta respuesta?
La prueba es inconclusa: el estado es OK, pero los datos parecen incorrectos.
La solicitud fue aceptada: deliveryTime es válido, aunque el producto no esté en stock.
¡Correcto! Estamos probando si la entrada es válida, no si el producto está disponible. Un 200 OK indica que la API aceptó el formato de la solicitud.
La prueba falla: esperábamos que isItemsAvailable fuera true
¡Lo has entendido bien!
Aunque isItemsAvailable es false, tiene sentido: no hay suficiente stock para el producto solicitado.
Podemos confirmar que esta clase se aceptó correctamente, la respuesta es válida y concuerda con lo esperado. Por lo tanto, este caso de prueba estaría aprobado.
Paso 6: Registra el resultado
Aquí tienes tu TC01 final:
ID
	Nombre del caso de prueba
	Condición previa
	Paso
	Descripción del paso
	Resultado esperado
	Resultado actual
	Estado
	TC01
	La solicitud se procesa con valores representativos válidos
	El sistema de almacén está activo.
	1
	Enviar una solicitud POST a /everything-you-need/v1/calculate con productId: 1, quantity: 2, deliveryTime: 9
	La API devuelve 200 OK y confirma la disponibilidad del producto
	La API devuelve 200 OK y confirma la disponibilidad del producto
	Aprobado
	Ejecutar y analizar el TC02: deliveryTime no válido
Paso 4: Envía la solicitud
                              * Abre nuevamente la solicitud: Everything you need: Delivery time
                              * Edita el cuerpo con los valores elegidos (productId: 1, quantity: 2, deliveryTime: 2) de nuestro TC02.
                              * Envía la solicitud.
Paso 5: Interpreta la respuesta
Ahora observa cómo la API maneja una entrada no válida.
  

Pregunta
¿Cuál es la interpretación correcta?
La prueba pasa: el sistema detectó el error, así que todo está bien.
El sistema falló por completo. Esta prueba debe descartarse.
Se rechazó la entrada: eso está bien, pero el manejo del error necesita mejorar.
¡Correcto! La API sí rechazó un valor no válido, pero devolver un 500 en lugar de un 400 indica un problema en cómo se gestiona el error.
¡Bien hecho!
El código 500 suele indicar un error interno, pero el mensaje "Invalid cast of deliveryTime property" sugiere que falló por un dato no válido.
En este contexto, lo interpretamos como un 400: lo importante es que la API rechazó la solicitud, tal como esperábamos para una clase no válida.
Paso 6: Registra el resultado
ID
	Nombre del caso de prueba
	Condición previa
	Paso
	Descripción del paso
	Resultado esperado
	Resultado actual
	Estado
	TC02
	Validación de campo “deliveryTime” con valores fuera del rango de horario laboral.
	El sistema de almacén está activo
	1
	Enviar una solicitud POST a /everything-you-need/v1/calculate con productId: 1, quantity: 2, deliveryTime: 2
	La API devuelve 400 Bad Request debido a que la hora de entrega está fuera del rango workingHours (7–23)
	La API devuelve 500 Internal Server Error el mensaje "Invalid cast of deliveryTime property" sugiere que la solicitud falló por un dato de entrada no válido, no por una falla del servidor
	Fallo
	💡
Tarea adicional:
Aplica clases de equivalencia al campo quantity y prueba también el almacén Fresh Food.
Usaste este enfoque para crear pruebas más estratégicas: identificaste los campos clave y validaste las respuestas según fueran clases válidas o no válidas.
En la próxima lección, verás cómo encontrar errores en los extremos mediante los valores límite.
Uso de IA para generar clases de equivalencia en pruebas de API
Estás validando un parámetro de API como deliveryTime o quantity, definiendo clases de equivalencia válidas e inválidas.
La IA puede ayudarte a sugerir clases y casos comunes en API como null, campos faltantes o tipos incorrectos.
Cómo usar la IA para generar clases de equivalencia
Haz clic aquí para ver la lección en formato de texto.
Input
                              * Campo a analizar (ej. deliveryTime).
                              * Fragmento de regla (copiado tal cual de doc/requisitos).
                              * Contexto mínimo del endpoint: método + endpoint + dónde está el campo (body/query/path) + tipo/formato si aparece en la doc.
Fragmento (Everything you Need)
                              * Endpoint: POST /everything-you-need/v1/calculate
                              * Campos relevantes: productId, quantity, deliveryTime
                              * Regla conocida: almacén opera de 7:00 a 23:00 → deliveryTime debe caer en ese rango.
Prompt
Actúa como QA engineer.
Quiero generar clases de equivalencia para pruebas de API.
Para el campo: deliveryTime
Reglas (solo lo que aparece aquí):
                              * El almacén opera de 7:00 a 23:00.
                              * deliveryTime representa una hora.
Necesito:
                              * Lista de clases válidas y no válidas basadas estrictamente en esas reglas.
                              * Para cada clase, un valor representativo.
                              * Para cada clase, el resultado esperado (acepta/rechaza; si no puedes asegurar el status code, dilo).
Restricciones:
                              * No inventes reglas adicionales.
                              * No mezcles varias diferencias en la misma clase (rango ≠ tipo ≠ null).
                              * Si falta información, crea una sección Preguntas.
Devuélvelo como tabla: Clase | ¿Válida? | Valor | Esperado.
(Puedes repetir el mismo prompt para quantity, pegando sus reglas cuando existan. Si la regla depende de stock real y no hay datos, la IA debe moverlo a “Preguntas”.)
Checklist
Pregunta
Una vez que generaste y refinaste tus clases de equivalencia para deliveryTime, pega este mensaje de seguimiento en el mismo chat de IA:
                              * Mini-prompt:
Actúa como formateador.
NO generes clases nuevas. NO cambies valores.
Toma mis clases de equivalencia ya aprobadas para deliveryTime y preséntalas exactamente como una tabla con estas columnas:
Clase | ¿Válida? | Valor representativo | Resultado esperado (acepta/rechaza)
Reglas (solo para validar consistencia del formato):
                                 * Debe incluir como mínimo estas 3 filas de rango: 7–23 (válida), <7 (no válida), >23 (no válida).
                                 * Si en tu resultado final incluiste clases por tipo/forma (string/null/missing), también deben aparecer como filas separadas (sin mezclar con rango).”
                                 * No mezcles rango y tipo en la misma fila.
                                 * Si no tienes status code, escribe solo “rechaza” (sin código).
                                 * Aquí está mi resultado final ya validado (no lo modifiques):
[PEGA AQUÍ TU LISTA/TABLA FINAL]
Clase¿Válida?Valor representativoResultado esperado (acepta/rechaza)
deliveryTime dentro del rango 7–23
Sí
9
acepta
deliveryTime menor que 7
No
6
rechaza
deliveryTime mayor que 23
No
24
rechaza
Veredicto: Casi correcto
Has identificado correctamente:
                                    * Las clases requeridas por rango están presentes y separadas adecuadamente.
                                    * Los valores representativos son claros y corresponden a sus respectivas clases.
                                    * El resultado esperado está expresado correctamente como 'acepta' o 'rechaza'.
Esto es lo que se debe ajustar:
                                    * El formato de la tabla no es claro debido a la falta de separadores entre columnas y filas. Asegúrate de usar un formato tabular con delimitadores claros como | para que las columnas sean fácilmente identificables.
Feedback IA
Reenviar
Usaste este enfoque para crear pruebas más estratégicas: identificaste los campos clave y validaste las respuestas según fueran clases válidas o no válidas.
En la próxima lección, verás cómo encontrar errores en los extremos mediante los valores límite.
Valoración de la lección
Siguiente



Sprint 4: Pruebas de API
Capítulo 4/6
Pruebas de API: Preparación y Ejecución
30 min
Valores límite
Habrás visto este fenómeno en múltiples ocasiones: un sistema que funciona perfectamente... hasta que le das un número de más.
Tal vez un formulario que acepta la edad 60, pero falla con 61, o un botón que se rompe cuando el precio llega a cero. Estos son unos clásicos ejemplos de errores de límites, y a veces pueden ser difíciles de detectar.
Ya aprendiste a identificarlos en interfaces de frontend, pero ahora es momento de subir de nivel:
Vamos a aplicar ese mismo enfoque a tus pruebas de API.
Por qué los valores límite importan en las APIs
Al igual que en el frontend, los errores suelen aparecer en los límites. Pero, en lugar de rellenar formularios, esta vez enviarás datos sin procesar en el cuerpo de una solicitud y observarás cómo reacciona la API.
Cuando pruebas una API, los valores límite te ayudan a verificar:
                                    * ¿La API acepta el primer valor válido?
                                    * ¿Rechaza el primer valor no válido?
                                    * ¿Maneja esas transiciones de forma consistente?
Esto es especialmente útil en campos con límites claros, como deliveryTime.
Pruebas con valores límite
Como en los otros tipos de pruebas, vamos a seguir el mismo flujo: esta vez centrándonos en los valores límite:
  

Sigamos trabajando con deliveryTime para Everything You Need:
1. Identifica los valores límite para deliveryTime
En la lección anterior, usaste clases de equivalencia para agrupar las entradas en conjuntos válidos e inválidos.
Ahora toca dar un paso más — identificar los límites de esas clases.
💡
Las pruebas de valores límite se enfocan en los extremos de cada clase de equivalencia — los puntos donde es más probable que cambie el comportamiento del sistema.
Esto significa que para cada clase, debes probar los valores:
                                    * Justo en el límite (por ejemplo, la primera y la última hora válida).
                                    * Justo fuera del límite (por ejemplo, una unidad antes o después).
                                    * Un valor dentro de la clase.
Ya sabes que deliveryTime es válido entre 7 y 23.
Así que ahora veamos qué valores nos ayudan a probar esos límites.
Pregunta
¿Cuáles de los siguientes valores representan casos de prueba válidos de valores límite para deliveryTime, según el rango de 7 a 23?
Elige tantas como quieras
6
¡Sí! Este es el límite no válido inferior: un caso ideal para comprobar que la API rechaza correctamente las horas de entrega demasiado tempranas.
15
0
¡Así es! Este es el límite no válido superior: ideal para comprobar que se bloquean correctamente las horas demasiado tardías.
1
23
¡Perfecto! Este es el límite válido superior: la hora válida más tardía que la API aún debería aceptar.
7
¡Exacto! Este es el límite válido inferior: confirma que la API acepta la hora de entrega más temprana permitida.
¡Lo has entendido bien!
Aquí tienes un resumen rápido de lo que hemos identificado:
  

2. Diseña los casos de prueba usando valores límite
¡Perfecto! Ahora que identificaste los valores límite clave, es momento de convertirlos en casos de prueba reales.
Como antes, cada caso de prueba:
                                    * Parte de una clase de equivalencia clara.
                                    * Se centra en un valor específico cerca del límite.
                                    * Te ayuda a verificar si la API acepta o rechaza correctamente ese valor.
Vamos a diseñar dos casos de prueba: uno en un límite válido y otro en un límite no válido.
TC03: Límite inferior válido (deliveryTime = 7)
ID
	Nombre del caso de prueba
	Condición previa
	Paso
	Descripción del paso
	Resultado esperado
	TC03
	La solicitud se acepta con la primera hora de entrega válida
	El sistema del almacén está activo
	1
	Enviar una solicitud POST a /everything-you-need/v1/calculate con: productId: 1, quantity: 2, deliveryTime: 7
	La API devuelve 200 OK, confirmando que el formato de la solicitud es válido y fue procesado
	                                    * Esta es la primera hora de entrega aceptable según el horario de funcionamiento del almacén.
                                    * La API debería responder con 200 OK, incluso si el producto no está en stock, ya que el formato de la solicitud es válido.
TC04: Límite superior no válido (deliveryTime = 24)
ID
	Nombre del caso de prueba
	Condición previa
	Paso
	Descripción del paso
	Resultado esperado
	TC04
	La solicitud se rechaza cuando deliveryTime supera el rango permitido
	El sistema de almacén está activo
	1
	Enviar una solicitud POST a /everything-you-need/v1/calculate con: productId: 1, quantity: 2, deliveryTime: 0
	La API devuelve 200 OK.


El campo isWarehouseWorking=False
	                                    * Este valor está justo por encima de la última hora permitida (23).
                                    * La API debería rechazar esta solicitud. Idealmente, devolvería un 400 Bad Request.
Ejecutar y analizar el TC03: Límite inferior válido (deliveryTime = 7)
Paso 4: Envía la solicitud
Esta vez, no necesitas crear una solicitud nueva desde cero. Puedes reutilizar la anterior y simplemente actualizar el valor de prueba.
Servidor
¡Genial, tu servidor ha sido iniciado!
Dirección del servidor: https://cnt-412b3315-46cf-49e6-b921-c1eeb3f1f322.containerhub.tripleten-services.com
Reiniciar el servidor
Esto es lo que debes hacer:
                                    * Abre la solicitud: Everything you need: Delivery time
                                    * Actualiza el cuerpo con los valores del TC03 (deliveryTime = 7).
                                    * Envía la solicitud.
Paso 5: Interpreta la respuesta
Después de enviar la solicitud, céntrate en si la API acepta correctamente el valor límite.
  

Pregunta
¿Qué te dice esta respuesta?
La prueba falló: el valor es demasiado bajo. La API debería haberlo rechazado.
La prueba no cuenta: el sistema aceptó el valor, pero eso no prueba que el límite esté bien implementado.
La prueba pasó: el valor está en el límite inferior y fue aceptado correctamente.
¡Sí! deliveryTime = 7 es la primera hora válida. Un 200 OK confirma que la API acepta correctamente el límite inferior.
¡Bien hecho!
El sistema acepta correctamente la hora de entrega más temprana posible.
Esto confirma que el límite inferior del rango válido está implementado correctamente: los usuarios pueden programar entregas a partir de la hora 7, tal y como se esperaba.
Paso 6: Registra el resultado
ID
	Nombre del caso de prueba
	Condición previa
	Paso
	Descripción del paso
	Resultado esperado
	Resultado actual
	Estado
	TC03
	La solicitud es aceptada con el deliveryTime válido más bajo (7)
	El sistema del almacén está activo
	1
	Enviar una solicitud POST a /everything-you-need/v1/calculate con productId: 1, quantity: 2, deliveryTime: 7
	La API devuelve 200 OK, confirmando que la solicitud es válida
	La API devolvió 200 OK, solicitud aceptada correctamente
	Aprobado
	Ejecutar y analizar el TC04: Límite superior no válido (deliveryTime = 24)
Paso 4: Envía la solicitud
Al igual que antes, no necesitas crear una solicitud nueva desde cero, puedes reutilizar tu solicitud de “Delivery time” y simplemente actualizar el valor de deliveryTime.
                                    * Abre la solicitud: Everything you need: Delivery time
                                    * Actualiza el cuerpo con los valores para el TC04 (deliveryTime = 24).
                                    * Envía la solicitud.
Paso 5: Interpreta la respuesta
Ahora observa con atención cómo la API maneja una entrada no válida que está justo fuera del rango permitido.
  

Pregunta
¿Cuál es la interpretación correcta de esta respuesta?
Se rechazó la entrada: eso está bien, pero el manejo del error necesita mejorarse.
¡Exactamente! La API sí rechazó un valor fuera del rango permitido, pero devolver un 500 en lugar de un 400 indica que el manejo de errores es deficiente.
El sistema falló por completo: la prueba no sirve.
La prueba pasa: el sistema detectó el error, así que todo está bien.
¡Excelente trabajo!
El sistema rechaza correctamente un horario de entrega que excede el rango permitido, pero responde con un 500 Internal Server Error en lugar de con un 400 Bad Request, que sería más adecuado.
Esto significa que la validación de entradas funciona, pero el manejo de errores no es claro ni amigable. En un escenario real, los clientes recibirían un error de sistema confuso en lugar de una explicación clara, lo cuál complica la depuración y la atención al usuario.
Paso 6: Registra el resultado
ID
	Nombre del caso de prueba
	Condición previa
	Paso
	Descripción del paso
	Resultado esperado
	Resultado actual
	Estado
	TC04
	La solicitud se rechaza si deliveryTime excede el rango permitido (0)
	El sistema de almacén está activo
	1
	Enviar una solicitud POST a /everything-you-need/v1/calculate con productId: 1, quantity: 2, deliveryTime: 0
	La API devuelve 200 OK.


El campo isWarehouseWorking=False
	La API devolvió 500 Internal Server Error con el mensaje "Invalid cast of deliveryTime property"
	Fallido
	💡
Tarea extra: Prueba valores límite para el campoquantity o cambia al almacén Fresh Food. ¿Puedes detectar los casos límite allí también?
Uso de IA para generar valores límite (boundary values) en API testing
Haz clic aquí para ver la lección en formato de texto.
Fragmento
                                    * Endpoint: POST /everything-you-need/v1/calculate
                                    * Campo: deliveryTime
                                    * Tipo: integer
                                    * Rango válido: 7–23 (inclusive)
Prompt
Actúa como QA engineer.
A partir del requisito, genera valores límite (boundary values) para deliveryTime.
Reglas:
                                    * Usa solo lo que aparece en el requisito (tipo y rango).
                                    * Asume intervalo de 1 unidad (por ser integer).
                                    * Devuelve exactamente 6 valores, calculados con intervalo 1: min-1, min, min+1, max-1, max, max+1 (cubre: fuera inferior, límite inferior, dentro inferior, dentro superior, límite superior, fuera superior).
                                    * Entrega el resultado en 6 líneas con formato: Etiqueta → Valor → Válido/Inválido
                                    * Si el rango no es claro (inclusive/exclusive), escríbelo en “Preguntas”.
Requisito:
[PEGA AQUÍ]
Checklist
Checklist
¿El rango quedó exactamente como el requisito (7–23, inclusive)?
¿Incluye ambos límites: 7 y 23?
¿Incluye 1 dentro del rango cerca de cada límite: 8 y 22?
¿Incluye 1 fuera del rango cerca de cada límite: 6 y 24?
¿Marcó correctamente válido/ inválido?
¿No metió valores “lejanos” (0, 999) como si fueran boundary?
¿No inventó reglas adicionales (formatos, UI, otros campos)?
Si el requisito no indica inclusive/exclusive, ¿lo mandó a “Preguntas” en lugar de asumir?
¡Buen trabajo!
💡
Tip: Si la IA se equivoca con los “±1”, pídele solo números. Intenta con un prompt como este:
“Devuélveme únicamente las 6 líneas con etiquetas y valores numéricos. Intervalo 1. Sin explicaciones.”
Pregunta
Una vez que generaste (y refinaste) tu lista final de valores límite para deliveryTime , usa este prompt para formatear tu resultado final en 6 líneas y luego pégalo aquí
Resume mi resultado final como 6 líneas con formato: Etiqueta → Valor → Válido/Inválido. Devuelve solo esas 6 líneas. Sin explicación. Intervalo 1. No inventes reglas.
Fuera inferior → 6
Límite inferior → 7
Dentro inferior → 8
Dentro superior → 22
Límite superior → 23
Fuera superior → 24
Veredicto: ¡Perfecto! Has identificado correctamente los valores límite y su validez, y tu formato cumple con las expectativas de la tarea. Buen trabajo al seguir las instrucciones y presentar los datos de manera clara y precisa.
Feedback IA
Reenviar
¡Acabas de subir de nivel en tus habilidades de tester! Ahora puedes detectar errores en APIs que se esconden justo en los límites.
En la siguiente lección, vamos a asegurarnos de que los datos en la respuesta de la API sean tan sólidos como el código de estado.
Valoración de la lección
Siguiente
Sprint 4: Pruebas de API
Capítulo 4/6
Pruebas de API: Preparación y Ejecución
25 min
Validación de la API
La API de los almacenes está a punto de lanzarse. Antes de que eso ocurra, tu equipo necesita hacer una verificación especial:
Realizar una validación completa de la respuesta del endpoint /everything-you-need/v1/calculate.
Para ello, necesitas entender qué es la validación de una API.
¿Qué es la validación de una API?
Imagina que eres médico y te llega un paciente con dolor de garganta: lógicamente procedes a tomarle la temperatura y revisar su garganta. Esa es una atención puntual, es como revisar algunos campos clave en una API para un caso específico.
Pero ahora imagina que ese mismo paciente va a correr una maratón. De pronto, necesitas hacerle un chequeo completo: análisis de sangre, corazón, pulmones… todo. Eso es una validación completa de una API: realizar un diagnóstico completo para asegurarte de que el sistema esté preparado de forma integral.
  

💡
En esto consiste la validación de una API: una verificación campo por campo, regla por regla, para confirmar que la respuesta de la API es realmente confiable.
Nos ayuda a responder esta pregunta:
¿Podemos confiar en todo lo que devuelve la API?
Estas son las áreas clave que vas a validar:
                                    * El esquema de la respuesta.
                                    * La lógica de negocio.
¿Cuándo hacer una validación completa?
Hazla si la solicitud es válida (200 OK) y necesitas confirmar que los datos son correctos. También antes del lanzamiento, tras hacer cambios en el backend o si otros equipos dependen de la respuesta. Úsala para verificar reglas de negocio como “si hay disponibilidad del 100%, se devuelven todos los productos”.
¿Cuándo no hace falta?
Si solo estás revisando cómo reacciona la API, por ejemplo, en pruebas negativas, validaciones de entrada o respuestas simples como "success": true"; no necesitas validar todos los detalles.
Cómo realizar la validación de una API
Ya probaste una solicitud básica y confirmaste que respondió correctamente, pero ahora es momento de realizar una validación completa de la API. Eso significa verificar cada parte de la respuesta: estructura, tipos, valores y lógica interna.
Vamos a reutilizar la solicitud Everything You Need: Delivery Time del módulo anterior. Así no tienes que volver a configurarla y puedes centrarte en analizar lo que ya tienes.
Vamos paso a paso para validar esta respuesta.
Paso 1: Validación del esquema
¿Qué es?
💡
La validación del esquema verifica si la estructura y el formato de la respuesta coinciden con lo que se espera del sistema.
No se trata solo del contenido, estás comprobando que:
                                    * Estén presentes los campos obligatorios.
                                    * Los campos tengan los tipos de datos correctos.
                                    * La estructura siga el formato acordado.
¿Qué usamos como referencia?
Vamos a abrir la documentación en Apidoc.
Servidor
¡Genial, tu servidor ha sido iniciado!
Dirección del servidor: https://cnt-3163d8a9-34fb-47fa-a389-f196fe8790c8.containerhub.tripleten-services.com
Reiniciar el servidor
En este caso, Apidoc no enumera explícitamente un esquema de respuesta para la solicitud POST /everything-you-need/v1/calculate.
Sin embargo, incluye un ejemplo de respuesta que se usa para hacer pruebas y comparaciones. Esa es la mejor referencia disponible y la usaremos para nuestra validación del esquema.
  

Esta estructura nos indica:
  

Esta tabla es tu referencia principal: tu tarea es comprobar que la respuesta contiene estos campos y que cada uno tiene el tipo correcto.
Comprueba:
                                    * ¿Están presentes todos los campos listados?
                                    * ¿Los campos anidados están estructurados correctamente? (por ejemplo, workingHours debe tener start y end)
                                    * ¿Hay campos inesperados?
                                    * ¿Los tipos son correctos? (por ejemplo, price no debe ser un string).
💡
En el mundo real, las inconsistencias de esquema a menudo causan errores en otros servicios conectados. Validar el esquema ayuda a prevenir estos errores desde el principio.
Pregunta
¿Coincide esta respuesta con el esquema esperado según el ejemplo y la documentación con la que trabajaste? Para cada elemento, elige si coincide o no.
  

  

Todos los campos clave del esquema esperado están presentes.
Sí, coincide con la estructura esperada
Sí. La respuesta incluye todos los campos clave: name, workingHours, price, isWarehouseWorking, isItemsAvailable, percentOfAvailableItems y availableProducts.
Los campos anidados como workingHours están estructurados correctamente.
Sí, coincide con la estructura esperada
Correcto. workingHours es un objeto con start y end, ambos números enteros, tal como se espera.
No hay campos inesperados o no documentados en la respuesta.
Sí, coincide con la estructura esperada
Exactamente. La respuesta no incluye ningún campo adicional.
Todos los tipos de los campos coinciden con los tipos de datos esperados.
Sí, coincide con la estructura esperada
Bien hecho. price es un número, name es un string y availableProducts es un array: todos los tipos son correctos.
¡Buen trabajo!
Confirmaste que la estructura de la respuesta coincide con el formato esperado. Esto significa que cualquier sistema que dependa de esta API —incluyendo el frontend u otros servicios— puede procesar los datos de forma segura y sin errores.
Paso 2. Validación de la lógica de negocio
💡
La validación de la lógica de negocio consiste en comprobar si los valores de la respuesta tienen sentido según las reglas del sistema.
Esto implica analizar cómo interpretó el sistema tu solicitud y si sus cálculos, decisiones e indicadores son coherentes.
Las reglas suelen estar descritas en los Requisitos del Back End.
En la documentación encontramos que:
El usuario o la usuaria solo puede pedir una cantidad completamente disponible de un artículo en al menos uno de los almacenes. […] La lógica de selección del almacén es que los comestibles están en stock, debe estar abierto cuando se realiza el pedido y es la opción más barata.
Esto nos indica que:
                                    * La disponibilidad es binaria: o el producto está completamente disponible en un almacén, o no lo está.
                                    * Los productos deben verificarse uno por uno en el inventario del almacén.
Hay una última conclusión que podemos extraer sobre la lógica de negocio:
Pregunta
¿Cuál de las siguientes afirmaciones es cierta si ninguno de los artículos solicitados está disponible en ningún almacén?
Selecciona todas las que correspondan.
Elige tantas como quieras
availableProducts debe incluir todos los productos solicitados, incluso si su cantidad es cero.
isItemsAvailable es false
Correcto. Si no se puede entregar ninguno de los artículos, este campo debe indicar claramente que no hay disponibilidad.
isItemsAvailable es true si al menos uno de los productos solicitados existe en el almacén, incluso si está fuera de stock
availableProducts es un array vacío
Correcto. Dado que ninguno de los productos solicitados está disponible, no hay nada que incluir en esta lista.
percentOfAvailableItems es 0
Correcto. No había artículos disponibles, por lo que el porcentaje de cumplimiento es cero.
¡Buen trabajo!
Pregunta
¿Coincide la lógica de la respuesta con las reglas de negocio en cuanto a la disponibilidad en el almacén?
  

El campo isItemsAvailable es false.
Sí, coincide con las reglas.
¡Genial! Esto refleja la lógica: ninguno de los elementos solicitados está disponible, por lo que el flag debe ser false.
El array availableProducts está vacío.
Sí, coincide con las reglas.
¡Bien visto! Si no hay productos solicitados disponibles, este campo debería devolver una array vacío.
El percentOfAvailableItems es 0.
Sí, coincide con las reglas.
¡Eso es! Cero significa que ninguno de los artículos solicitados está disponible; esto se alinea con la lógica de negocio.
Los campos name y workingHours siguen estando incluidos.
Sí, coincide con las reglas.
¡Exactamente! Estos campos describen el almacén y siempre se devuelven, independientemente de la disponibilidad del artículo.
¡Perfecto!
¡Excelente! Verificaste que el sistema interpreta correctamente la disponibilidad de productos:
                                    * Devuelve los indicadores correctos (isItemsAvailable = false).
                                    * Muestra el porcentaje correcto de productos disponibles (0).
                                    * Solo incluye productos que realmente se pueden entregar: si no hay ninguno, la lista aparece vacía.
Estos valores confirman que la API entendió tu solicitud, aplicó las reglas del negocio y comunicó su decisión de forma clara y precisa.
No solo comprobaste que la API funcionara, la examinaste a fondo.
Verificaste cada campo, cada regla, cada resultado.
En la próxima lección añadirás una última pieza a tus pruebas: ¡trabajar con bases de datos!
Valoración de la lección
Siguiente
Sprint 4: Pruebas de API
Capítulo 4/6
Pruebas de API: Preparación y Ejecución
30 min
Bases de datos y APIs
Acabas de terminar de probar la disponibilidad de los productos en el almacén Everything You Need y justo te llega un mensaje del equipo de marketing:
  

Revisas de nuevo todo:
ID de producto 44: ✅ solicitado.
Respuesta: ✅ disponible.
Entonces, ¿por qué no aparece en el sitio?
Para llegar al fondo del asunto, tendrás que ir una capa más abajo: a la base de datos, donde vive la información principal del producto. Si tanto el almacén como la API confirman que el producto está, el problema podría estar en cómo el sitio obtiene esos datos.
No hace falta que profundicemos aún, más adelante tendrás un sprint completo sobre bases de datos. Por ahora, solo tendrás una muestra: vamos a interactuar con la base de datos a través de la API para averiguar qué está pasando realmente.
¿Qué es una base de datos?
Una base de datos es el lugar donde vive la información. Piensa en ella como la memoria a largo plazo de la aplicación: detalles de productos, usuarios, pedidos… todo se guarda allí.
  

Vamos a desglosarlo:
                                    * El backend es el cerebro: en él se procesan las solicitudes, se aplica la lógica y se conectan los diferentes sistemas.
                                    * El servidor es la máquina (física o virtual): ejecuta el código del backend y mantiene la aplicación en funcionamiento.
                                    * ¿Y la base de datos? Es la memoria. Almacena los datos reales: productos, usuarios, pedidos… todo.
Volviendo a nuestra metáfora del restaurante: la base de datos es la despensa.
Cuando el mesero (nuestra API) lleva un pedido a la cocina (el backend), los chefs van primero a la despensa a buscar los ingredientes.
  

Solo entonces pueden empezar a cocinar, emplatar y enviar el plato terminado de vuelta al cliente a través del mesero.
Sin ingredientes en la despensa, no hay plato en la mesa.
En el contexto de las pruebas de API, esto es exactamente lo que ocurre entre bastidores. Cuando alguien hace clic en un kit, el sitio envía una solicitud a la API. El backend procesa esa solicitud, extrae la información correcta de la base de datos y la envía de vuelta como respuesta.
Pregunta
Imagina que estás comprando una entrada para un concierto en línea. Para cada acción, elige qué componente de la arquitectura de la aplicación web es responsable:
Verifica si un asiento está disponible y confirma la reserva.
Backend
¡Correcto! El backend aplica la lógica, consulta la base de datos y gestiona la operación.
Almacena información como fechas de conciertos, asientos disponibles y precios.
Base de datos
¡Correcto! La base de datos guarda información estructurada y persistente.
¡Lo has entendido bien!
Por qué los QA engineers trabajan con bases de datos
Como parte del proceso de pruebas de API, no siempre trabajarás con bases de datos, pero puede que necesites confirmar que:
                                    * La API refleje correctamente lo que hay en la base de datos.
                                    * Los nuevos datos (como kits, pedidos o usuarios) se guarden correctamente en la base de datos.
                                    * Los datos eliminados o modificados realmente se actualicen en la base de datos.
                                    * El sitio refleje lo que hay en la base de datos y avise cuando no lo hace.
En otras palabras: después de hacer las pruebas, puede que necesites comprobar si la acción realmente se ha reflejado en la base de datos.
¿Cómo puedes acceder a la base de datos?
En este proyecto, no te conectarás directamente a la base de datos con un cliente SQL.
En su lugar, la API te dará un atajo: te permitirá descargar las tablas de la base de datos como archivos .csv.
Eso significa que podrás:
                                    * Hacer una solicitud a la API.
                                    * Descargar la tabla correspondiente.
                                    * Verificar los resultados en una hoja de cálculo.
¿Cuál es el flujo de trabajo?
Aquí tienes un enfoque básico para probar el comportamiento relacionado con la base de datos a través de la API:
                                    * Realiza una acción con la API: crea, modifica o elimina algo.
                                    * Descarga la tabla correspondiente de la base de datos mediante una URL especial de la API.
                                    * Abre el archivo .csv y comprueba si se reflejan tus cambios.
                                    * Compara el resultado esperado con el actual, e informa sobre cualquier diferencia existente.
Estás a punto de probarlo por tu cuenta.
Práctica 1. Verifica si el producto existe
Servidor
¡Genial, tu servidor ha sido iniciado!
Dirección del servidor: https://cnt-46ae9909-4319-4641-9a87-d01ee1a5c88e.containerhub.tripleten-services.com
Reiniciar el servidor
¿Prefieres leer? Haz clic aquí para ver la transcripción.
Ya confirmaste que el producto con ID 44 está disponible en el almacén; ahora, vamos a asegurarnos de que también exista en la base de datos.
Descarga la tabla de productos:
                                    * Inicia el servidor y copia el enlace.
                                    * Escribe la URL de tu servidor en la barra de direcciones de Google Chrome y añade /api/db/resources/kit_model.csv.
a. Deberás importar este documento a una plataforma como Excel o Google Sheets en formato separado por comas para poder visualizarlo bien.
Debería tener este aspecto:
  
                                    * Presiona Enter.
Esto descargará el contenido de la tabla product_model, que contiene la lista de todos los productos del sistema.
Busca el producto con ID 44
Abre el archivo .csv y busca el producto con ID 44.
Verifica que existe y observa los siguientes campos:
                                       * Nombre
                                       * Peso
                                       * Unidades
                                       * Precio
Pregunta
Vamos a practicar cómo encontrar el producto correcto en la base de datos.
¿Pudiste encontrar el producto con ID 44?
Sí, lo encontré
¡Perfecto! Eso significa que descargaste y abriste el archivo correctamente, y que identificaste el producto. ¡Sigamos!
¡Bien hecho!
Pregunta
Descubriste que el producto 44 existe en la base de datos y coincide con los datos del almacén. ¿Cuál es la conclusión más probable?
Se debería eliminar el producto y volver a agregarlo.
El problema probablemente ocurre después de que se recuperen los datos, tal vez en el frontend.
¡Perfecto! Eso significa que los sistemas del backend funcionan como se espera, y el problema probablemente está en cómo se muestra la información en el sitio.
Hay un error en la base de datos: es necesario agregar el producto.
La API no está conectada correctamente a la base de datos.
¡Bien hecho!
Justo cuando estás atando cabos, tu superior te envía otra idea:
  

Parece un buen plan.
Vamos a crear un producto de prueba, revisar la base de datos y ver si todo se procesa correctamente.
Práctica 2. Verifica un kit nuevo
¿Prefieres leer? Haz clic aquí para ver la transcripción.
Vamos a reutilizar nuestra solicitud Crear kit:
                                       * Busca tu solicitud Crear kit.
                                       * Agrega el producto 44.
                                       * Envía una solicitud POSTa /api/v1/kits/:id/products, donde id es el id de tu nuevo kit.
                                       * Envíala de nuevo.
                                       * Descarga otra vez kit_model.csv desde base_url/api/db/resources/kit_model.csv.
                                       * Busca tu nuevo kit. Asegúrate de que incluya el producto 44.
Pregunta
¿Pudiste encontrar tu kit recién creado en la base de datos?
Encontré el kit, pero incluía el producto incorrecto
No vi mi kit en absoluto
Sí, encontré el kit y contiene el producto 44
¡Perfecto! Eso significa que tu solicitud API funcionó y que los datos llegaron correctamente a la base de datos.
¡Bien hecho!
Práctica 3. Verifica que el nuevo kit se haya eliminado
¿Prefieres leer? Haz clic aquí para ver la transcripción.
                                       * Finalmente, envía una solicitud DELETE a /api/v1/kits/:id, donde :id es el id de tu nuevo kit.
                                       * Descarga de nuevo kit_model.csv desde base_url/api/db/resources/kit_model.csv.
                                       * Verifica si el nuevo kit desapareció de la base de datos.
Pregunta
Después de eliminar tu kit de prueba y revisar nuevamente la base de datos, ¿qué encontraste?
El producto desapareció de la base de datos, pero el kit sigue allí
El kit ya no está en la base de datos
¡Perfecto! Eso confirma que la eliminación vía API funcionó y que el cambio se registró correctamente en el sistema.
El kit todavía está en la base de datos
¡Buen trabajo!
Revisaste el almacén, la base de datos y la API, ¡y todo funcionó!
Tu kit de prueba se creó y se eliminó correctamente, lo que significa que el backend y el flujo de datos están bien.
Entonces, ¿por qué el producto no aparece en el sitio?
Lo más probable es que el problema esté en el frontend: tal vez haya un bug en cómo se muestran o se filtran los kits.
Ya reportaste tus hallazgos al equipo, y ellos se encargarán del resto.
¡Hora de seguir adelante! En el camino te esperan más acertijos de API.
Valoración de la lección
Siguiente


Sprint 4: Pruebas de API
Capítulo 5/6
Errores en la API: Detección y Reporte
30 min
Informes de errores para APIs
Era una tarde tranquila y estabas probando relajadamente la API del almacén cuando, en un momento dado, enviaste un horario de entrega que estaba un poco fuera de rango.
En ese entonces esperabas un 400 Bad Request normal y corriente.
¿Y qué obtuviste? Un 500 Internal Server Error en toda regla.
Como QA engineer, esa es tu señal: es hora de hacer un informe de errores.
Y eso nos lleva al último paso de nuestro flujo de trabajo de pruebas de API: el que convierte resultados confusos en feedback claro y útil:
  

Ya has escrito informes de errores antes, cuando trabajabas con las pruebas de frontend. El formato sigue siendo el mismo: misma plantilla, mismas columnas.
Pero el contenido cambia.
Ahora describirás endpoints, cuerpos de solicitud, encabezados y códigos de estado; no clics ni botones.
Vamos a recorrer este proceso juntos, utilizando como ejemplo el error que acabas de encontrar.
Cómo redactar un informe de errores de la API
1. Pasos de reproducción
Antes de nada —incluso antes de escribir el título— tienes que mostrar cómo reproducir el error: esta es la esencia de cualquier informe de errores.
En las pruebas de interfaz de usuario (UI), esto puede significar varias acciones del usuario, pero en las pruebas de API, normalmente basta con una sola solicitud.
Todo lo demás —preparar Postman, hacer clic en “Send”, etc.— es una condición previa o una acción de la herramienta, no parte del paso en sí. Así que sí: un único paso claro suele ser todo lo que necesites.
Veamos el caso de prueba y encontremos ese paso.
ID
	Nombre del caso de prueba
	Condición previa
	Paso
	Descripción del paso
	Resultado esperado
	Resultado actual
	TC02
	La solicitud falla si deliveryTime está fuera del horario permitido
	El sistema de almacén debe estar activo
	1
	Enviar una solicitud POST a /everything-you-need/v1/calculate con productId: 1, quantity: 2, deliveryTime: 2
	La API devuelve 400 Bad Request debido a que deliveryTime está fuera del rango workingHours (7–23)
	La API devuelve 500 Internal Server Error con el mensaje "Invalid cast of deliveryTime property"
	Pregunta
¿Cuál de las siguientes es la mejor manera de describir los pasos para reproducir este error de API?
Enviar una solicitud POST a /everything-you-need/v1/calculate y comprobar si la API devuelve 400 Bad Request cuando deliveryTime está fuera de rango
Intentar calcular una hora de entrega fuera del horario laboral para comprobar cómo la API maneja entradas no válidas.
Enviar una solicitud POST a /everything-you-need/v1/calculate con el siguiente cuerpo: { "productId": 1, "quantity": 2, "deliveryTime": 2 }
¡Buen trabajo! Es una descripción precisa del paso: método, endpoint y datos. Se enfoca en la solicitud, no en la herramienta ni en la interpretación.
Abrir Postman, abrir la pestaña de solicitud, pegar la URL del endpoint /everything-you-need/v1/calculate, elegir POST, pegar el cuerpo JSON y hacer clic en Enviar.
¡Buen trabajo!
¡Genial! Añadámoslo a nuestro informe:
ID
	Título
	Pasos de reproducción
	Resultado esperado
	Resultado actual
	Severidad
	

	

	Enviar una solicitud POST a /everything-you-need/v1/calculate con el siguiente cuerpo: { "productId": 1, "quantity": 2, "deliveryTime": 2 }
	

	

	

	2. Resultado Esperado
Una vez hayas escrito el paso para reproducir el error, lo siguiente es registrar qué debería haber ocurrido.
En las pruebas de API, eso significa describir la respuesta esperada —el código de estado y el mensaje— de la forma más clara y específica posible.
¿Cuál es la buena noticia? No necesitas inventar nada. Ya lo escribiste en el caso de prueba.
Vamos a tomarlo de ahí y añadirlo a nuestro informe.
ID
	Título
	Pasos de reproducción
	Resultado esperado
	Resultado actual
	Severidad
	

	

	Enviar una solicitud POST a /everything-you-need/v1/calculate con el siguiente cuerpo: { "productId": 1, "quantity": 2, "deliveryTime": 2 }
	La API devuelve 400 Bad Request debido a que deliveryTime está fuera del rango workingHours (7–23)
	

	

	3. Resultado Actual
Ahora que has escrito lo que debería haber ocurrido, es momento de documentar lo que realmente pasó.
Esta parte es sencilla, pero muy importante: simplemente copia la respuesta exacta que devolvió la API, sin reformularla ni interpretarla. No necesitas explicar por qué falló ni adivinar qué pasó en el servidor. Solo muestra lo que respondió.
Ya vimos la respuesta actual en el caso de prueba:
500 Internal Server Error con el mensaje "Invalid cast of deliveryTime property"
Añadámosla a nuestro informe:
ID
	Título
	Pasos de reproducción
	Resultado esperado
	Resultado actual
	Severidad
	

	

	Enviar una solicitud POST a /everything-you-need/v1/calculate con el siguiente cuerpo: { "productId": 1, "quantity": 2, "deliveryTime": 2 }
	La API devuelve 400 Bad Request debido a que deliveryTime está fuera del rango workingHours (7–23)
	La API devuelve 500 Internal Server Error con el mensaje "Invalid cast of deliveryTime property"
	

	4. Título
Un buen título responde tres preguntas simples:
¿Qué pasó? — ¿Dónde pasó? — ¿Cuándo o bajo qué condición?
Eso es lo que llamamos el enfoque de Qué – Dónde – Cuándo.
En errores de interfaz de usuario (UI), podría verse así:
“El botón de login no responde en Safari (macOS)”
En errores de la API, se ve más como:
“Error 400 al enviar un id inválido a /kits”
Intentemos aplicarlo a nuestro caso:
Pregunta
¿Cuál sería el título correcto para nuestro error?
POST /calculate falla con error del servidor
Error 500 en lugar de 400 al enviar un deliveryTime no válido en POST /calculate
¡Bien hecho! Explica claramente qué salió mal, dónde ocurrió y cuándo (bajo qué condición).
La solicitud POST a /everything-you-need/v1/calculate devuelve un error al recibir un deliveryTime fuera de rango; se esperaba validación adecuada y error del lado del cliente, pero se recibió un error interno
Comportamiento inesperado en la lógica de deliveryTime durante la validación de backend de los datos enviados por el cliente
¡Lo has entendido bien!
ID
	Título
	Pasos de reproducción
	Resultado esperado
	Resultado actual
	Severidad
	

	Error 500 en lugar de 400 al enviar un deliveryTime no válido en POST /calculate
	Enviar una solicitud POST a /everything-you-need/v1/calculate con el siguiente cuerpo: { "productId": 1, "quantity": 2, "deliveryTime": 2 }
	La API devuelve 400 Bad Request debido a que deliveryTime está fuera del rango workingHours (7–23)
	La API devuelve 500 Internal Server Error con el mensaje "Invalid cast of deliveryTime property"
	

	5. ID
En la mayoría de las herramientas (como Jira o YouTrack), el ID se genera automáticamente. Pero en esta lección, lo asignarás manualmente para tenerlo todo claro.
Mantén el formato corto y consistente, algo como:
BUG-001
Usa BUG (Error) como prefijo y numera tus informes: BUG-002, BUG-003, etc.
ID
	Título
	Pasos de reproducción
	Resultado esperado
	Resultado actual
	Severidad
	BUG-001
	Error 500 en lugar de 400 al enviar un deliveryTime no válido en POST /calculate
	Enviar una solicitud POST a /everything-you-need/v1/calculate con el siguiente cuerpo: { "productId": 1, "quantity": 2, "deliveryTime": 2 }
	La API devuelve 400 Bad Request debido a que deliveryTime está fuera del rango workingHours (7–23)
	La API devuelve 500 Internal Server Error con el mensaje "Invalid cast of deliveryTime property"
	

	6. Severidad
Ya has visto el campo Severidad en las pruebas de frontend: ayuda al equipo a entender qué tan urgente es un error.
En las pruebas de API, usamos la misma escala —Baja, Media, Alta, Crítica— pero las señales que evaluamos son distintas. En lugar de botones rotos o flujos bloqueados, aquí analizas:
                                       * Códigos de estado incorrectos.
                                       * Respuestas confusas o engañosas.
                                       * Errores del servidor o JSON mal formado.
                                       * Comportamientos del sistema que no coinciden con el manejo de errores esperado.
Pregunta
¿Qué severidad le asignarías a este error?
Baja
Crítica
Alta
Media
¡Correcto! El sistema funciona, pero devuelve un código de estado engañoso. No se cae el sistema, pero tampoco está bien.
¡Perfecto!
¡Exactamente! En nuestro caso:
                                       * La solicitud contenía datos no válidos (error del cliente).
                                       * La API respondió con un 500 Internal Server Error (fallo del lado del servidor).
                                       * No se cayó nada pero envió una señal equivocada.
                                       * Los clientes y desarrolladores podrían malinterpretar lo que ocurrió.
Esto no rompe el sistema pero sí genera confusión, por lo que podemos asignar con confianza una severidad Media.
Perfecto, ya hemos documentado nuestro error:
ID
	Título
	Pasos de reproducción
	Resultado esperado
	Resultado actual
	Severidad
	BUG-001
	Error 500 en lugar de 400 al enviar un deliveryTime no válido en POST /calculate
	Enviar una solicitud POST a /everything-you-need/v1/calculate con el siguiente cuerpo: { "productId": 1, "quantity": 2, "deliveryTime": 2 }
	La API devuelve 400 Bad Request debido a que deliveryTime está fuera del rango workingHours (7–23)
	La API devuelve 500 Internal Server Error con el mensaje "Invalid cast of deliveryTime property"
	Media
	Uso de IA para organizar información en un informe de errores de API
Esperabas 400 por deliveryTime fuera de rango, pero recibiste 500. Tu tarea: armar un bug report con evidencia clara (request + response).
Paso 1. Prepara el input
📎
Input mínimo (lo que le das a la IA):
                                       * Contexto del caso de prueba (1 línea).
                                       * Método + endpoint.
                                       * Request body (y headers si son relevantes).
                                       * Resultado esperado (del requisito o del test case).
                                       * Resultado actual (status code + mensaje/response body).
                                       * (Opcional) Evidencia extra: timestamp, environment, request/response completos.
Ejemplo (Everything you Need)
                                       * Método/endpoint: POST /everything-you-need/v1/calculate
Body:
  {"productId":1,"quantity":2,"deliveryTime":2}
                                       *  
                                       * Esperado: 400 Bad Request porque deliveryTime está fuera de workingHours (7–23)
                                       * Actual: 500 Internal Server Error con "Invalid cast of deliveryTime property"
Paso 2. Prompt para organizar el bug report
Prompt
Actúa como QA engineer, pero en este paso eres formateador.
NO inventes información. NO cambies valores. NO asumas causas.
Con la evidencia que te doy, organízala en un bug report con estas columnas:
ID | Título | Pasos de reproducción | Resultado esperado | Resultado actual | Severidad
Reglas:
                                       * “Pasos” debe ser una sola solicitud (método + endpoint + body). No describas Postman.
                                       * “Título” debe seguir: Qué – Dónde – Cuándo/condición.
                                       * “Resultado esperado/actual” deben ser concretos (status + motivo/mensaje si existe).
                                       * “Severidad” usa: Baja/Media/Alta/Crítica, justificando solo con el impacto observable (ej. código 500 vs 400).
Evidencia:
                                       * Método/endpoint: [PEGA AQUÍ]
                                       * Request body: [PEGA AQUÍ]
                                       * Resultado esperado: [PEGA AQUÍ]
                                       * Resultado actual: [PEGA AQUÍ]
                                       * Contexto (opcional): [PEGA AQUÍ]
Paso 3. Genera el primer borrador
Paso 4. Revisa y refina el resultado
Checklist
¿El paso de reproducción describe solo la solicitud (método + endpoint + body), sin “abrir Postman / click Send”?
¿El resultado esperado viene del requisito/test case (no está inventado)?
¿El resultado actual está copiado tal cual (status + mensaje), sin interpretación?
¿El título responde Qué–Dónde–Cuándo (incluye código y condición)?
¿La severidad es coherente con el impacto (ej. 500 por input inválido suele ser Media si no hay caída/pérdida)?
¿No cambió valores del body ni “arregló” el request?
¿No agregó campos/headers que no existen?
¡Perfecto!
Pregunta
Una vez que generaste y refinaste tu reporte de bug pega aquí solo tu resultado final (ya validado por ti).
Para estandarizar el formato, usa este mini-prompt y pega únicamente la salida final de la IA:
                                       * Mini-prompt
Actúa como formateador.
NO crees un bug nuevo. NO inventes datos. NO cambies valores.
Toma mi información ya aprobada y preséntala como una sola fila en una tabla con estas columnas:
ID | Título | Pasos de reproducción | Resultado esperado | Resultado actual | Severidad
Reglas de formato:
                                          * “Pasos de reproducción” = una sola solicitud: método + endpoint + body JSON.
                                          * “Título” = Qué – Dónde – Cuándo/condición (breve).
                                          * “Resultado esperado/actual” = incluye status code + motivo/mensaje si existe.
                                          * “Severidad” = Baja/Media/Alta/Crítica (sin inventar impacto).
Aquí está mi información final ya validada (no la modifiques):
                                          * ID: [PEGA AQUÍ]
                                          * Método/endpoint: [PEGA AQUÍ]
                                          * Body: [PEGA AQUÍ]
                                          * Resultado esperado: [PEGA AQUÍ]
                                          * Resultado actual: [PEGA AQUÍ]
                                          * Severidad: [PEGA AQUÍ]
IDTítuloPasos de reproducciónResultado esperadoResultado actualSeveridad
BUG-001
Error 500 en lugar de 400 al enviar un deliveryTime no válido en POST /calculate
Enviar una solicitud POST a /everything-you-need/v1/calculate con el siguiente cuerpo: { "productId": 1, "quantity": 2, "deliveryTime": 2 }
La API devuelve 400 Bad Request debido a que deliveryTime está fuera del rango workingHours (7–23).
La API devuelve 500 Internal Server Error con el mensaje "Invalid cast of deliveryTime property".
Media
Veredicto: Casi correcto
Has identificado correctamente:
                                             * Los pasos de reproducción están bien descritos y coinciden con la evidencia proporcionada.
                                             * El resultado esperado y el resultado actual están correctamente especificados, incluyendo los códigos de estado y mensajes relevantes.
                                             * La severidad está correctamente asignada como 'Media'.
Esto es lo que se debe ajustar:
                                             * El formato de la tabla no sigue estrictamente el formato requerido. Asegúrate de que los datos estén organizados en una tabla con columnas separadas por '|' y con una fila de encabezado clara. Esto facilita la lectura y evaluación del reporte.
Feedback IA
Reenviar
¿Hay algo más que necesitemos agregar aquí? ¡Lo descubriremos en la siguiente lección!
Valoración de la lección
Siguiente


Sprint 4: Pruebas de API
Capítulo 5/6
Errores en la API: Detección y Reporte
40 min
Registrar errores de API
Encontraste un error: envías un deliveryTime no válido y obtienes un 500. Pero ¿qué causó exactamente el fallo?
A veces, para averiguarlo, hay que mirar más al fondo: al registro interno de eventos del sistema. Los registros (logs) muestran lo que realmente pasó: qué recibió el servidor, qué intentó hacer y en qué punto falló.
En esta lección aprenderás a leer esos logs y a usarlos para que tus informes de errores sean más completos y más útiles.
¿Qué son los logs en las pruebas de API?
💡
Los logs son el registro interno de eventos del sistema: un registro línea por línea de lo que hizo el backend, cuándo y con qué datos.
Son como la caja negra de un avión o una cámara de seguridad: invisibles para los usuarios, pero increíblemente útiles cuando algo sale mal. Ayudan a los desarrolladores (y testers) a reconstruir la cadena de eventos que llevó a un error.
¿Cómo se crean los logs?
La mayoría de los sistemas backend modernos están configurados para registrar automáticamente acciones clave y problemas.
Cada uno de estos eventos se registra como una línea de texto. Estas líneas se escriben en la consola del servidor, en un archivo o en un endpoint especial que almacena temporalmente los logs (así están registrados en Urban.Grocers).
Como QA engineer, no necesitas configurar el registro: sólo saber cómo leer lo que ya está allí.
¿Qué suele haber en un log?
Estos son algunos de los elementos que normalmente encontrarás en los logs de API:
  

No necesitas entender cada línea, solo lo suficiente para encontrar las pistas que expliquen el error.
Cómo obtener los logs
Generalmente, los logs se almacenan en el servidor, y como QA necesitas acceder a ellos. Según el sistema, eso puede implicar conectarte a un archivo, revisar una consola o, más cómodamente, utilizar un endpoint especial.
En Urban.Grocers, los logs están disponibles a través de una ruta especial de la API. Esto significa que puedes recuperarlos como cualquier otra solicitud: llamando a un endpoint.
Tarea
Servidor
¡Genial, tu servidor ha sido iniciado!
Dirección del servidor: https://cnt-fb9aa6e2-c9af-4c56-827c-c1d26d19bea7.containerhub.tripleten-services.com
Reiniciar el servidor
¿Prefieres leer? Haz clic aquí para ver la transcripción.
Sigue estos pasos para reproducir el error y obtener los logs.
                                             * Inicia el servidor.
                                             * Envía de nuevo la solicitud Everything You Need: Delivery Time.
Recordatorio
                                             * Solicita los logs: Ahora, envía una solicitud GET a /api/logs/secondary. Nombra esta solicitud «Obtener logs» en tu colección. La respuesta incluirá las últimas entradas del log del backend.
                                             * Encuentra tu entrada en el log. Busca un bloque de líneas que coincidan con tu solicitud. Verás una secuencia que incluye:
                                             * La solicitud recibida.
                                             * Un mensaje de error.
                                             * Un stack trace.
                                             * El código de respuesta.
Deberías ver algo así:
  

Aquí están los últimos registros encontrados por el endpoint:
2025-07-22T07:02:07.250Z [DEBUG] [Almacén][everything-you-need]: [Request] - ::ffff:127.0.0.1 POST:/everything-you-need/v1/calculate - HTTP/1.1 - application/json - {"deliveryTime":6,"products":[{"id":1,"quantity":1},{"id":4,"quantity":3}]}
2025-07-22T07:02:07.250Z [ERROR] [Almacén][everything-you-need]: Unexpected error:
2025-07-22T07:02:07.251Z [ERROR] [Almacén][everything-you-need]:      {"stack":"Error: Invalid cast of `deliveryTime` property\n    at h.<anonymous> (/var/www/backend/packages/secondary/build/server.js:685:119829)\n    at Generator.next (<anonymous>)\n    at /var/www/backend/packages/secondary/build/server.js:685:119417\n    at new Promise (<anonymous>)\n    at o (/var/www/backend/packages/secondary/build/server.js:685:119162)\n    at h.calculateOrder (/var/www/backend/packages/secondary/build/server.js:685:119704)\n    at t.ServiceInvoker.<anonymous> (/var/www/backend/packages/secondary/build/server.js:561:2921)\n    at Generator.next (<anonymous>)\n    at /var/www/backend/packages/secondary/build/server.js:561:1371\n    at new Promise (<anonymous>)\n    at r (/var/www/backend/packages/secondary/build/server.js:561:1116)\n    at t.ServiceInvoker.callTargetEndPoint (/var/www/backend/packages/secondary/build/server.js:561:2523)\n    at t.ServiceInvoker.<anonymous> (/var/www/backend/packages/secondary/build/server.js:561:1830)\n    at Generator.next (<anonymous>)\n    at /var/www/backend/packages/secondary/build/server.js:561:1371\n    at new Promise (<anonymous>)","message":"Invalid cast of `deliveryTime` property"}
2025-07-22T07:02:07.251Z [DEBUG] [Almacén][everything-you-need]: [Response Status] - /everything-you-need/v1/calculate - 500 Error interno del servidor
Log 1: La solicitud
Esto es un registro a nivel de solicitud. Aparece cuando el servidor recibe una solicitud de API entrante.
Para interpretarlo, céntrate en qué recibió y aceptó el servidor: el método, el endpoint, el cuerpo de la solicitud y la IP del remitente. Si estos elementos aparecen claramente y no hay ningún error, puedes concluir que la comunicación fue técnicamente exitosa a nivel de transmisión.
Utiliza la presencia de estos detalles para responder:
                                             * ¿La solicitud llegó al servidor?
                                             * ¿El servidor entendió lo enviado?
  

Pregunta
¿Qué confirma esta línea de log sobre el comportamiento del sistema?
2025-07-22T07:02:07.250Z [DEBUG] [Almacén][everything-you-need]: [Request] - ::ffff:127.0.0.1 POST:/everything-you-need/v1/calculate - HTTP/1.1 - application/json - {"deliveryTime":6,"products":[{"id":1,"quantity":1},{"id":4,"quantity":3}]}
El cliente usó el método HTTP incorrecto, por lo que el servidor devolvió un error 405 Method Not Allowed.
La solicitud fue bloqueada debido a un deliveryTime no válido, lo que provocó una respuesta 400 Bad Request.
El servidor recibió y entendió correctamente una solicitud POST a /everything-you-need/v1/calculate. Incluye un cuerpo JSON y no se produjo ningún error en esta etapa
¡Bien! Esto confirma que la solicitud llegó al servidor y fue aceptada para su procesamiento.
Este log confirma que la solicitud fue recibida pero descartada silenciosamente antes de llegar a la lógica del backend.
¡Lo has entendido bien!
Log 2: Error inesperado
Esto es un registro de nivel de error. Aparece cuando el sistema encuentra un problema al procesar la solicitud.
Para interpretarlo, observa dos elementos clave de nuestra tabla:
  

En esta línea vemos un mensaje genérico: "Unexpected error". Normalmente esto significa que el sistema no tiene una forma predefinida de manejar lo sucedido. Intentó procesar la solicitud pero encontró algo no cubierto por las validaciones, la lógica de negocio o las rutas de fallo esperadas.
Como QA, puedes ver distintos tipos de mensajes en los logs:
                                             * ✅ Mensajes esperados, como "Validation failed: missing field", "Invalid ID format", "Token expired": indican que el sistema detectó el problema y respondió en consecuencia. Normalmente conducen a códigos 4xx.
                                             * ⚠️ Mensajes inesperados, como "Unexpected error", "Unhandled exception", "Null pointer" o no obtener ningún mensaje: suelen provocar un 500 y señalan que hay un error de backend o una falta de manejo de errores.
💡
Si ves un error inesperado, a menudo significa que has descubierto una brecha en el sistema, y eso merece ser reportado.
Pregunta
¿Qué indica esta línea de log?
2025-07-22T07:02:07.250Z [ERROR] [Almacén][everything-you-need]: Unexpected error:
Este mensaje significa que el usuario no estaba autorizado para acceder al recurso.
La solicitud fue rechazada porque deliveryTime falló la validación de entrada.
El sistema detectó una violación de una regla de negocio y devolvió el error correspondiente.
El sistema encontró un fallo interno que no estaba cubierto por la lógica de negocio o validaciones planeadas.
¡Bien hecho! La frase "Unexpected error" y el nivel [ERROR] significan que el backend falló de una manera para la que no estaba preparado, por eso devolvió un 500.
¡Bien hecho!
Log 3: Stack Trace y Mensaje
Este es un registro de stack trace. Aparece inmediatamente después de que se produzca un fallo interno grave, y ayuda a explicar exactamente qué salió mal y dónde.
En nuestra tabla, esta línea contiene dos elementos clave:
  

Para interpretarlo, comprueba si el mensaje vincula el error a una entrada específica (como deliveryTime) y si el trace confirma que provino del backend. Si el mensaje menciona un campo de datos y el stack trace muestra archivos del backend, puedes relacionar con confianza el error con el procesamiento de la entrada.
Usa este log para responder:
                                             * ¿El fallo estaba ligado a un campo o tipo de dato específico?
                                             * ¿Ocurrió en la lógica del backend?
Pregunta
¿Qué indica esta parte del log?
"stack":"Error: Invalid cast of `deliveryTime` property\n    at h.<anonymous> (...)",
"message":"Invalid cast of `deliveryTime` property"
Que los datos de la solicitud no coincidían con lo que el sistema esperaba, y el servidor devolvió un error de validación claro.
Que el backend falló al procesar el campo deliveryTime y señala en qué parte del código ocurrió ese fallo. 
¡Exacto! El mensaje vincula el error a un campo específico y el stack trace muestra que sucedió en la lógica del backend.
Que al cuerpo de la solicitud le faltaban campos obligatorios.
¡Lo has entendido bien!
Log 4: Estado de respuesta
Este es un registro de respuesta. Muestra lo que el servidor envió de vuelta después de intentar procesar la solicitud.
En esta línea aparecen dos elementos claros de nuestra tabla:
  

Este estado coincide con lo que ya vimos en la respuesta y confirma que el error provino desde dentro del servidor, no de la solicitud en sí.
💡
Leyendo la secuencia completa de logs, ahora sabes:
                                             * La solicitud llegó al backend y fue aceptada ([Request]).
                                             * El servidor encontró un error no manejado al procesarla ([ERROR]).
                                             * El fallo fue causado por el campo deliveryTime (message y stack).
                                             * El sistema respondió con un 500, lo que significa que el fallo fue del lado del servidor ([Response Status]).
Cómo documentar el log en tu informe de errores
Agrega al informe de errores una columna llamada “Material adicional (log)” y pega allí solo las líneas de log más relevantes. Así los desarrolladores verán directamente la causa del error sin reproducir todo. No incluyas todos los logs, solo los que evidencien claramente el problema. Echa un vistazo al ejemplo final del informe.
ID
	Título
	Pasos de reproducción
	Resultado esperado
	Resultado actual
	Severidad
	Material adicional (log)
	BUG-001
	Error 500 en lugar de 400 al enviar un deliveryTime no válido en POST /calculate
	Enviar una solicitud POST a /everything-you-need/v1/calculate con el siguiente cuerpo: { "productId": 1, "quantity": 2, "deliveryTime": 2 }
	La API devuelve 400 Bad Request debido a que deliveryTime está fuera del rango workingHours (7–23)
	La API devuelve 500 Internal Server Error con el mensaje "Invalid cast of deliveryTime property”
	Media
	2025-07-22T07:02:07.250Z [ERROR] [Almacén][everything-you-need]: {"message":"Invalid cast of deliveryTime property"}2025-07-22T07:02:07.251Z [DEBUG] [Almacén][everything-you-need]: [Response Status] - /everything-you-need/v1/calculate - 500 Error interno del servidor
	Uso de IA para extraer líneas relevantes de un log largo
Haz clic aquí para ver la lección en formato de texto.
Estás adjuntando un extracto del log para el bug que encontraste — un 500 que se devuelve cuando deliveryTime está fuera de rango.
La IA puede ayudarte a localizar el bloque correcto y extraer solo las líneas clave ([Request] → [ERROR] / "message" → [Response Status]).
Sin embargo, puede mezclar líneas de otra solicitud, inventar causas en lugar de citar el log, eliminar el "message" o el código de estado, o incluir demasiado (como un stack trace completo).
Veamos cómo hacerlo correctamente.
Cómo usar la IA para extraer líneas relevantes del log
Paso 1. Prepara el input
Tu input tiene 2 partes:
                                             * Tu firma de búsqueda (para encontrar tu request en el log):
                                             * Método + endpoint
                                             * Indicador en el body (campo/valor)
                                             * Error observado (status + "message" si existe)
                                             * (Opcional) timestamp aproximado
                                             * (Opcional) requestId / correlationId / traceId
                                             * Ejemplo de firma
                                             * POST /everything-you-need/v1/calculate
                                             * "deliveryTime": 6
                                             * observado: [Response Status] ... 500
                                             * "Invalid cast of \deliveryTime property"`
                                             * Log: pega el log completo (o el segmento grande donde aparece).
Paso 2. Prompt para extraer líneas relevantes
Prompt
Actúa como QA engineer y analista de logs.
Voy a pegar un log largo. Tu tarea es extraer solo las líneas necesarias para adjuntarlas a un informe de errores.
Firma de mi request (úsala para encontrar el bloque correcto):
                                             * Endpoint/método: POST /everything-you-need/v1/calculate
                                             * Indicador en el body: "deliveryTime": 6
                                             * Error observado: 500
                                             * "Invalid cast of \deliveryTime property" (si aparece)
                                             * (Opcional) timestamp aproximado: [PEGA AQUÍ]
                                             * (Opcional) requestId / correlationId / traceId: [PEGA AQUÍ]
Reglas:
                                             * Devuélveme entre 3 y 8 líneas máximo.
                                             * Deben cubrir esta secuencia si existe: [Request] → primera [ERROR] relevante → "message" → [Response Status].
                                             * NO inventes explicaciones. NO reescribas: copia las líneas tal cual.
                                             * Si hay stack trace largo, incluye solo la primera línea del stack + la línea con "message".
                                             * Devuelve solo las líneas extraídas (sin explicación).
Log:
[PEGA AQUÍ EL LOG COMPLETO]
Paso 3. Genera el primer borrador
Paso 4. Revisa y refina el resultado
Checklist
Incluye el [Request] correcto (tu endpoint + tu deliveryTime)
Incluye el [ERROR] relevante y el "message" clave
Incluye [Response Status] 500
No hay solicitudes mezcladas ni trazas de pila innecesarias
¡Buen trabajo!
Pregunta
Pega aquí solo tu extracto final del log (entre 3 y 8 líneas), copiado tal cual (sin resumir ni reescribir)
2026-06-22T12:11:00.429Z [DEBUG] [Almacén][everything-you-need]: [Request] - ::ffff:127.0.0.1 POST:/everything-you-need/v1/calculate - HTTP/1.1 - application/json - {"deliveryTime":6,"products":[{"id":1,"quantity":2}]}
2026-06-22T12:11:00.430Z [ERROR] [Almacén][everything-you-need]: Unexpected error:
2026-06-22T12:11:00.430Z [ERROR] [Almacén][everything-you-need]: {"stack":"Error: Invalid cast of deliveryTime property
2026-06-22T12:11:00.430Z [ERROR] [Almacén][everything-you-need]: {"message":"Invalid cast of deliveryTime property"}
2026-06-22T12:11:00.430Z [DEBUG] [Almacén][everything-you-need]: [Response Status] - /everything-you-need/v1/calculate - 500 Error interno del servidor
Veredicto: ¡Perfecto!
Has identificado correctamente:
                                             * El request correcto con el método y endpoint especificados.
                                             * El indicador del body con el valor esperado de "deliveryTime": 6.
                                             * La primera línea relevante de error y la línea clave con el mensaje de error.
                                             * La línea de estado de respuesta con el código 500.
No hay ajustes necesarios. ¡Buen trabajo!
Feedback IA
Reenviar
¡Has completado el flujo de pruebas de API! Cubriste cada paso, desde desglosar tareas y revisar errores hasta hacer informes de errores.
Después de esto, estarás listo para comenzar tu proyecto final. ¡Vamos! 🚀
Valoración de la lección
Siguiente


Sprint 4: Pruebas de API
Capítulo 5/6
Errores en la API: Detección y Reporte
15 min
Cuestionario: Pruebas de API
Ya casi hemos terminado. ¡Estás a un solo paso de tu proyecto final!
Antes de empezar a trabajar en él, repasemos brevemente algunos puntos esenciales que te ayudarán a tener éxito.
Este cuestionario es más que una simple prueba: es una gran oportunidad para comprobar si entendiste todo lo que vimos, para recibir feedback constructivo e incluso para reutilizar algunas de tus respuestas en el proyecto, ya que nos centraremos en el mismo requisito con el que tienes que trabajar.
Tómate tu tiempo, piensa tus respuestas detenidamente y, si no sientes total confianza en algo, siempre puedes volver atrás y revisar los temas que necesites.
¡Mucha suerte! ¡Tú puedes! 💪
Pregunta
Imagina que estás probando la API de Urban Grocers para añadirle productos a un kit existente. ¿Es correcta esta solicitud?
  

  

Sí, todo parece correcto: esta solicitud debería funcionar.
No, a la URL le falta el ID del kit.
No, el método es incorrecto y falta el campo requerido.
¡Excelente! La solicitud utiliza el método incorrecto (PUT en lugar de POST) y al objeto del segundo producto le falta el campo quantity requerido.
Sí, el método correcto es PUT porque estás actualizando algo.
¡Buen trabajo!
Pregunta
¿Cuál de las siguientes entradas de prueba pertenece a una clase de equivalencia no válida?
💡
El usuario debería poder añadir productos existentes a un kit mediante el endpoint POST URL + /api/v1/kits/:id/products. El kit tiene un límite de 30 productos únicos; no es posible tener más de 30 ID de producto únicos en un kit. La aplicación debería mostrar un error si un usuario intenta superar ese límite.
Se ha añadido una productsList con 5 ID de producto diferentes, cada uno con una cantidad de 6, a un nuevo kit.
Se ha añadido una productsList con 30 ID de producto únicos a un nuevo kit.
Se ha añadido una productsList con 15 entradas, todas con el mismo ID de producto, a un nuevo kit.
Se ha añadido una productsList con 35 ID de producto únicos a un nuevo kit.
Correcto, el kit tendría 35 ID de producto únicos, lo que supera el límite de 30.
¡Perfecto!
Pregunta
Para el mismo endpoint, ¿cuáles de las siguientes entradas se consideran valores límite no válidos para esta regla?
💡
El usuario debería poder añadir productos existentes a un kit mediante el endpoint POST URL + /api/v1/kits/:id/products. El kit tiene un límite de 30 productos únicos; no es posible tener más de 30 ID de producto únicos en un kit. La aplicación debería mostrar un error si un usuario intenta superar ese límite.
Elige tantas como quieras
Una lista con 1 ID de producto único.
Una lista con 29 ID de producto únicos.
Una lista con 31 ID de producto únicos.
Sí. 31 es el primer valor no válido por encima del límite superior válido (30).
Una lista con 28 ID de producto únicos.
Una lista con 30 ID de producto únicos.
¡Buen trabajo!
Pregunta
Para el mismo endpoint, ¿cuál de las siguientes entradas sería una lista completa de valores límite para el límite 30?
💡
El usuario debería poder añadir productos existentes a un kit mediante el endpoint POST URL + /api/v1/kits/:id/products. El kit tiene un límite de 30 productos únicos; no es posible tener más de 30 ID de producto únicos en un kit. La aplicación debería mostrar un error si un usuario intenta superar ese límite.
29, 31
29, 30, 31
¡Exactamente! Este es el conjunto completo para el límite de 30: 29 justo por debajo, 30 en el límite, 31 justo por encima. 29 y 30 deberían ser aceptados, 31 debería ser rechazado (contando los ID de producto únicos). Guarda esto para usarlo en el proyecto.
0, 1, 29, 30, 31
30, 31
¡Buen trabajo!
Pregunta
Estás probando el siguiente escenario:
Verifica que al agregar un producto existente a un kit con espacio disponible, se obtenga un estado 200 OK. ¿Cuáles de los siguientes son los pasos correctos para este caso de prueba?
  

  

  

  

¡Perfecto! Estos son los pasos mínimos correctos para verificar que se haya agregado correctamente un producto a un kit.
¡Buen trabajo!
Pregunta
Enviaste una solicitud POST a /api/v1/kits/:id/products con 31 ID de producto únicos. Esta fue la respuesta que recibiste. ¿Qué significa?
  

Esto es un falso negativo: 400 significa que la estructura de la solicitud era incorrecta, no los datos.
¡La prueba falló! El sistema debería aceptar 31 productos siempre que la cantidad sea baja.
El sistema rechazó correctamente una solicitud perteneciente a una clase no válida, justo por encima del límite permitido de 30 ID únicos.
¡Exactamente! Estabas probando un valor de clase no válido y la API respondió con un error 400, como se esperaba.
La prueba falló porque los ID de producto probablemente no existen en la base de datos.
¡Excelente trabajo!
¡Buen trabajo! Ahora aplica todo lo que aprendiste. ¡Este proyecto es tu momento para brillar!
Valoración de la lección
Siguiente


Sprint 4: Pruebas de API
Capítulo 6/6 · Faltan 4 lecciones
Proyecto
10 min
Cómo enviar tu proyecto: interfaz de hoja de cálculo
💡
En esta lección te presentaremos las partes clave de la interfaz de hoja de cálculo de la plataforma utilizada en tu proyecto. No es necesario que lo memorices todo, solo guarda esta página para más adelante.
La hoja de cálculo está totalmente integrada en TripleTen, por lo que no tendrás que descargar, copiar ni compartir nada. Tu trabajo y el feedback del equipo de supervisión permanecerán en el mismo lugar.
A continuación te explicamos brevemente sus características principales.
La interfaz
Cuando abras el proyecto, verás una descripción de la tarea a pantalla completa.
Para empezar, haz clic en Inicio o arrastra el divisor hacia la izquierda para abrir la hoja de cálculo.
Feature
	What it does
	Editable cells
	Click any cell to type — works like Google Sheets or Excel.
	Autosave
	All changes save automatically — look for the checkmark icon to confirm.
	Version history
	View and restore earlier edits at any time.
	Resizable panes
	Drag the divider to adjust the space between spreadsheet and task description.
	

Característica
	Qué hace
	Celdas editables
	Haz clic en cualquier celda para escribir en ella: funciona como en Google Sheets o Excel.
	Autoguardado
	Todos los cambios se guardarán automáticamente: busca el ícono de marca de verificación para confirmarlo.
	Historial de versiones
	Visualiza y restaura versiones anteriores en cualquier momento.
	Paneles redimensionables
	Arrastra el divisor para ajustar el espacio entre la hoja de cálculo y la descripción de la tarea.
	Cómo enviar tu trabajo
💡
Cuando hayas terminado:
                                             * Ve a la pestaña Enviar.
                                             * Haz clic en Enviar proyecto.
Feedback
Tu instructor revisará tu hoja de cálculo en la plataforma.
✉️
Recibirás un correo electrónico cuando la revisión esté lista.
Verás los comentarios junto a tu hoja de cálculo: edítala y vuelve a enviarla.
Para ver los comentarios:
                                             * Ve a la pestaña Enviar.
                                             * Haz clic en Comentarios en la iteración.
💡
Si ves "Has pasado la revisión", tu proyecto queda aceptado y el documento se vuelve de solo lectura.
¿Necesitas obtener una copia? Ve a Archivo → Descargar.
Ahora, ¡comencemos con tu proyecto!
Valoración de la lección
Siguiente


Sprint 4: Pruebas de API
Compartir
Descripción
Envío
Capítulo 6/6
Proyecto
50 min
Proyecto para el 4.º Sprint: Ejercicio
Urban Grocers acaba de enviar nuevas actualizaciones sobre cómo la plataforma maneja los kits y los servicios de entrega. Tu trabajo será analizar los nuevos requisitos y asegurarte de que la API los admita correctamente.
Servidor
Iniciar
Documentos de Urban Grocers con los que trabajarás
Hay dos fuentes de documentos principales que deberás utilizar para este proyecto, las mismas que utilizaste a lo largo del sprint:
Documentación de la API en Apidoc.
💡
Utiliza apiDoc para identificar el endpoint correcto, el método, los encabezados o la autenticación requeridos, los parámetros de solicitud y ver un cuerpo de solicitud como ejemplo.
Para abrir la documentación:
                                             * Inicia el servidor.
                                             * Copia el enlace (URL base) e insértalo en el campo de dirección del navegador Google Chrome.
                                             * Añade /docs/.
                                             * Presiona Enter.
Requisitos del backend
💡
Utiliza los Requisitos del backend para decidir qué probar y qué no: deriva los criterios de aceptación, las reglas de negocio, las validaciones de datos y los comportamientos de error que debes confirmar en tus pruebas.
Flujo de trabajo de la tarea
💻 Ten en cuenta que esta lección solo se puede realizar desde una computadora portátil.
Para esta tarea tendrás que:
                                             * Analizar dos requisitos: "Trabajar con los kits" y "Trabajar con los servicios de entrega".
                                             * Diseñar casos de prueba para probar las características que recibiste.
                                             * Ejecutar tus casos de prueba a través de Postman.
                                             * Crear informes de errores en Jira para cualquier error que encuentres.
Esto sigue los pasos relevantes del flujo de trabajo para las pruebas de API que cubrimos en el sprint. Los hemos adaptado ligeramente para adaptarlos a esta tarea.
Requisito 1: Trabajar con los kits
Paso 1: Analizar el requisito
Echemos un vistazo al extracto de los requisitos del backend: busquemos el requisito exacto en el que tendrás que trabajar.
Requisito 1
💻
El usuario debe poder agregar productos existentes a un kit utilizando el endpoint POST URL + /api/v1/kits/:id/products. El kit tiene un límite de 30 productos únicos; es decir, no es posible tener más de 30 IDs de productos únicos en un kit. La aplicación debe arrojar un error si el usuario intenta superar ese límite.
La cantidad no afecta a este recuento. Por ejemplo:
// La longitud de esta productsList es 2 porque tenemos 2 artículos con ID diferentes
// aunque la cantidad total de artículos sea 4. 
{
    "productsList": [
        {
            "id": 1,
            "quantity": 2
        },
        {
            "id": 6,
            "quantity": 2
        }
    ]
}
Al agregar IDs de productos no existentes, se debe devolver un 400 Bad Request. Al agregar productos a una ID de kit no existente, se debe devolver un 404 Not Found. En los casos en que el cuerpo de la solicitud no contenga la estructura correcta, se debe devolver un 400 Bad Request, por ejemplo: si productsList no es un array.
Cuando un kit supera el límite de 30 productos únicos, este deberá devolver: 400 Bad Request con un mensaje de error: "message": "No más de 30 artículos por conjunto”
Paso 2: Diseñar las pruebas
💡
Los casos de prueba deben agregarse a la hoja de cálculo integrada que verás a la derecha.
Al diseñar las pruebas para el Requisito 1, asegúrate de cubrir:
                                             * Cómo agregar productos a un kit.
                                             * Los casos positivos, los negativos, las clases de equivalencia y los valores límite para:
                                             * El parámetro :id en la URL (ID del kit).
                                             * Los campos id (ID de los productos).
                                             * El campo quantity en el cuerpo.
                                             * La estructura y longitud del array productsList.
                                             * El límite total de productos únicos por kit.
Antes de empezar a probar, deberías haber escrito 14-20 casos de prueba para el Requisito 1.
Paso 3: Ejecutar las pruebas
Ejecuta tus pruebas a través de Postman.
💡
Crea un nuevo kit vacío para probar este requisito.
👆
Recuerda que los errores pueden tener dos partes: el código y el mensaje. Códigos como 400 puede tener muchas causas, por lo que los mensajes pueden variar. Si difiere de los documentos, investiga qué ha podido suceder.
Paso 4: Crear informes de errores
                                             * Crea informes de errores en Jira para cualquier error que encuentres.
Lista de comprobación para los informes de errores
                                             * ¿Son únicos los títulos de los informes de errores?
                                             * ¿Coinciden los títulos de los informes de errores con el resultado actual?
                                             * ¿Incluyen los informes de errores pasos, resultados esperados y actuales, y se ha establecido la prioridad y especificado el entorno?
                                             * ¿Están duplicados los informes de errores?
                                             * ¿Se especifica el método HTTP en los encabezados de los informes de errores?
Cómo trabajar con Jira.
                                             * Sigue el enlace a la pantalla de registro de Atlassian (Jira) y mira los videos a continuación para crear una cuenta y aprender a enviar informes de errores.
Videos: creación de una cuenta y compilación de un informe de errores en Jira
Haz clic para ver la lección en formato de texto.
Jira: Cómo crear un reporte de error
Parte de tu proyecto consiste en generar defectos y otros tipos de incidencias dentro de Jira. Sin embargo, Jira no nos permite crear defectos de manera independiente; todos ellos deben existir dentro de un proyecto.
Seguramente te preguntarás el porqué; ¡Muy sencillo! Los proyectos son la base de Jira. Es aquí donde todas nuestras incidencias, sean defectos, historias de usuario, tareas o funcionalidades, estarán juntas en un espacio de trabajo organizado.
Así que, sin más que decir, ¡comencemos creando tu primer proyecto de Jira!
                                             * Tras completar tu registro, verás una pantalla que te preguntará que tipo de trabajo vas a realizar, aquí seleccionaremos Software development (Desarrollo de Software) y después daremos clic en Continue.
  

                                             * A continuación, habremos llegado a la pantalla de Tu trabajo en Jira. En la parte superior, podemos ver una barra de menú en la cual encontramos la pestaña Proyectos. Si hacemos clic aquí, podremos ver, a nuestra derecha la opción de Crear proyecto. ¡Con esto, podemos comenzar a configurar nuestro primer proyecto!
  

                                             * La opción Crear proyecto nos mostrará opciones de plantillas comunes para diferentes tipos de proyectos. En nuestro caso, debemos seleccionar la opción de Desarrollo de Software, y después, hacer clic en la opción Seguimiento de errores; Una vez seleccionada, damos clic en Usar plantilla.
  

  

                                             * Le damos un nombre apropiado a nuestro proyecto, y damos clic en Crear proyecto. No te preocupes por el cuadro de texto Clave, ya que este se llenará en automático basándose en el nombre de tu proyecto.
  

                                             * ¡Excelente! Con esto habrás creado un proyecto nuevo en Jira. En esta pantalla podrás explorar las incidencias que están afiliadas a este proyecto en particular. Ahora sí, podemos comenzar a crear nuestro primer defecto para este proyecto. Podrás crear cualquier tipo de incidencia desde el botón azul que dice Crear, que se encuentra en la barra de menús superior.
  

                                             * Una vez en la pantalla de creación de incidencias, solo debemos llenar los campos obligatorios, que en este caso son “Proyecto”, “Tipo de incidencia” “Resumen”. El administrador del proyecto puede establecer cuáles serán los campos mandatorios de cada tipo de incidencia, así como crear campos adicionales.
Cada equipo de trabajo suele tener su propia manera de llenar cada campo. A continuación te mencionaré qué es lo que esperamos de cada uno de estos campos:
                                             * Proyecto: En este campo deberás seleccionar el proyecto al cual vas a asignar tu defecto, en este caso, elegiremos el proyecto que recién creamos.
                                             * Tipo de incidencia: Este campo se refiere al tipo de reporte que se está generando. Esto puede ser una historia de usuario, una tarea, entre otros tipos.
                                             * Resumen: Aquí deberás incluir una descripción breve y concisa sobre tu defecto, algo así como un título para poder identificar tu reporte.
  

                                             * Hacemos clic en Crear y habremos terminado. Podrás ver una notificación que te indicará si la creación fue exitosa.
  

Toma en cuenta que podrás modificar tu incidencia aún después de haberla creado, Jira mantendrá un historial de todos los cambios realizados.
  

¡Felicidades! Con esto habrás creado tu primer proyecto y defecto dentro de Jira.
💡 Tendrás que dar al equipo de revisión acceso a tu espacio de trabajo de Jira. Abre las siguientes instrucciones para descubrir cómo hacerlo.
Cómo dar acceso al equipo de supervisión de proyectos
                                             * Ve a admin.atlassian.com.
                                             * Selecciona tu organización de la lista haciendo clic en el botón “Seleccionar”.
  

                                             * Selecciona “Productos” del menú de navegación que se encuentra en la parte superior.
  

                                             * Selecciona “Configuración de acceso de los usuarios” desde el menú de productos del lado izquierdo.
                                             * Da clic en el botón de “Añadir dominio”.
  

                                             * Llena el formulario de acuerdo a la captura de pantalla que se muestra a continuación, escribiendo tripleten-team.com dentro del cuadro de texto del “Dominio”. Asegúrate de no marcar la casilla “Aprobación del administrador”, ya que de esta forma te permitirá compartir tu proyecto sin necesidad de requerir aprobación.
  

                                             * Haz clic en Guardar.
¿Qué pasa si alguien del equipo de supervisión no tiene acceso a tus informes?
                                             * En el panel lateral, haz clic en “Equipos”.
  

                                             * Haz clic en el botón azul de “Añadir personas”.
  

                                             * Si el usuario __ no está en la lista, invítalo: ve a Invitar a un compañero de equipo, introduce su dirección de correo electrónico __ y haz clic en Añadir compañeros de equipo.  
                                                * Comprueba si has compartido el acceso a Jira con el dominio “@tripleten-team.com”. Este paso es importante porque garantiza que los revisores puedan acceder a tu trabajo.
                                                * Vincula los informes de errores de Jira en el campo correspondiente de la hoja de cálculo:
  

Requisito 2: Trabajar con los servicios de entrega
Paso 1: Analizar el requisito
Echemos un vistazo al extracto de los requisitos: busquemos el requisito exacto en el que tendrás que trabajar.
Requisito 2
💻 El servicio “Order and Go” debería estar disponible si se cumplen los requisitos del cálculo del precio del envío. El endpoint es: /order-and-go/v1/delivery.
La solicitud debe incluir tres campos obligatorios en el cuerpo (body), todos de tipo numérico:
                                                * productsCount: cantidad de productos.
                                                * productsWeight: peso total de los productos.
                                                * deliveryTime: hora prevista de entrega.
{
"deliveryTime": 9,
"productsCount": 10,
"productsWeight": 11
}
Si alguno de estos campos falta, tiene un tipo incorrecto o la estructura del body no es válida, el sistema debe responder con 400 Bad Request.
En caso de que los valores proporcionados no permitan calcular la entrega, el campo "isItPossibleToDeliver" en la respuesta será false, pero el código de estado seguirá siendo 200 OK.
Ejemplo de respuesta exitosa:
{
    "name": "Order and Go",   //Nombre del servicio de entrega
    "clientDeliveryCost": 10, //Costo de entrega para el cliente
    "toBeDeliveredTime": {    //Rango de tiempo de entrega, 
    "min": 10, "max": 20 },   //Valores en columna "Fulfillment time"
    "hostDeliveryCost": 23,   //Costo interno de envío
    "isItPossibleToDeliver": true //Indica si el envío se puede hacer
}
Consulta la sección “Servicios de entrega” en apiDoc para ver toda la información sobre la estructura de la solicitud y su respuesta.
Paso 2: Diseñar las pruebas
💡
Los casos de prueba deben agregarse a la hoja de cálculo integrada que verás a la derecha.
Al diseñar pruebas para el Requisito 2, asegúrate de cubrir:
                                                * Los casos positivos, los negativos, las clases de equivalencia y los valores límite para el parámetro deliveryTime. > Nota: el valor de deliveryTime debe validarse con la columna “Horario” en la tabla de Requisitos para el cálculo de precios de envío. >
                                                * Los casos positivos, los negativos, las clases de equivalencia y los valores límite para el parámetro productsWeight.
                                                * Los casos positivos, los negativos, las clases de equivalencia y los valores límite para el parámetro productsCount.
💡
En la parte “Detalles de cálculo de los servicios de entrega” de los Requisitos del backend, encontrarás el requisito para cada parámetro que te ayudará a identificar los valores de entrada para las pruebas positivas y negativas.
Antes de comenzar con las pruebas, debes tener entre 15 y 25 casos de prueba para el Requisito 2.
Paso 3: Ejecutar las pruebas
Ejecuta tus pruebas a través de Postman.
💡
Crea un nuevo kit vacío para probar este requisito.
👆
Recuerda que los errores pueden tener dos partes: el código y el mensaje. Códigos como el 400 pueden tener muchas causas, por lo que los mensajes pueden variar. Si difiere de lo que se muestra en los documentos, investiga qué ha podido suceder.
Paso 4: Crear informes de errores
                                                * Crea informes de errores en Jira para cualquier error que encuentres.
Lista de comprobación para los informes de errores
                                                * ¿Son únicos los títulos de los informes de errores?
                                                * ¿Coinciden los títulos de los informes de errores con el resultado real?
                                                * ¿Incluyen los informes de errores pasos, resultados esperados y reales, y se ha establecido la prioridad y se ha especificado el entorno?
                                                * ¿Están duplicados los informes de errores?
                                                * ¿Se especifica el método HTTP en los encabezados de los informes de errores?
                                                * Comprueba si has reservado el acceso a Jira con el dominio “@tripleten-team.com”.
                                                * Vincula los informes de errores de Jira en el campo correspondiente de la hoja de cálculo:
  

📎
Aquí tienes una lista con todos los instrumentos, documentos y plantillas que necesitarás para este proyecto:
                                                * Servidor: haz clic en el botón Iniciar servidor en la parte superior de la página para obtener un enlace temporal.
                                                * Apidoc: documentación de la API (base_url/docs/).
                                                * Requisitos del backend.
                                                * Postman: enviarás todas las solicitudes a través de él.
                                                * Jira.
Entrega del proyecto
¡Estás a solo unos clics de terminar el sprint! Vamos a asegurarnos de que lo tienes todo listo:
Lista de comprobación final del proyecto 4
Pregunta
Marca las siguientes casillas para confirmar que has completado cada paso.
Elige tantas como quieras
He escrito y ejecutado 14-20 casos de prueba para el Requisito 1, cubriendo escenarios positivos, negativos, clases de equivalencia y valores límite.
He comprobado que aparecen los códigos de error y los mensajes correctos para las ID de kit/producto no válidas, estructuras incorrectas o productsList duplicados.
He escrito y ejecutado entre 15 y 25 casos de prueba que cubren escenarios positivos, negativos, clases de equivalencia y valores límite para los tres campos: deliveryTime, productsWeight y productsCount.
He comprobado que se comporte correctamente cuando falta una entrada, no es válida o se usa edge-case, incluyendo errores 400 con mensajes precisos, y 200 OK con "isItPossibleToDeliver": false cuando la entrega no es posible.
He añadido todas mis pruebas y errores en la hoja de cálculo integrada a la derecha.
En la última columna del documento de la hoja de cálculo, adjunté los enlaces al Informe de errores en Jira.
He compartido el acceso a Jira con el dominio "@tripleten-team.com".
Enviar
💡
Si estás listo para enviar tu proyecto, debes cambiar a la pestaña "Enviar".
Valoración de la lección
Siguiente

REQUISITOS
https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/qa-sprint-4/ESP/V9/Requisitos%20del%20backend_ES.pdf



API DOC 

Filter...
x
                                                * Warehouses
                                                * Almacén: "Big World"
                                                * Almacén: "Everything You Need"
                                                * Almacén: "Food City"
                                                * Comprobar la cantidad de productos en stock
                                                * Comprobar la disponibilidad de productos en los almacenes
                                                * Obtener la lista de almacenes
                                                * Wharehouse: "Fresh Food"
                                                * [SOAP] Comprobar la cantidad de productos en stock
                                                * Couriers
                                                * Comprobar los costes de envío
                                                * Entrega: "Fast Delivery"
                                                * Entrega: "Food Service"
                                                * Entrega: "Order and Go"
                                                * Entrega: "Speedy"
                                                * Obtener la lista de entregas
                                                * Main.User
                                                * Creación de cuenta
                                                * Main.Products
                                                * Búsqueda de kit por producto
                                                * Cambio del precio del producto
                                                * Main.Kits
                                                * Añadir productos a la kit:
                                                * Cambio de la kit
                                                * Crear un kit
                                                * Eliminación del kit
                                                * Recibir todas las kit
                                                * Recibir una kit por el nombre
                                                * Main.Basket
                                                * Añadir productos a la cesta
                                                * Crear una cesta
                                                * Eliminar la cesta
                                                * Hacer el pedido
                                                * Recibir los productos de la cesta
                                                * Main.Orders
                                                * Recepción de pedidos de los usuarios
                                                * Utils
                                                * Logs de mensajeros/almacenes del servidor
                                                * Logs del servidor principal
                                                * Recuperar información de la tabla de base de datos
API Urban Grocers
Warehouses
Warehouses - Almacén: "Big World"
La interacción se realiza a través de SOAP
post
/big-world/wsdl
Parámetro
Campo
	Tipo
	Descripción
	deliveryTime
	number
	Plazo de entrega previsto
	products
	Array
	Lista de productos
	  id
	number
	Identificador del producto de la tabla product_model
	  quantity
	number
	Cantidad de producto
	                                                * Ejemplo de solicitud
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  xmlns:tns="WebServices.WarehouseWsdl">
    <soap:Body>
        <tns:checkSupply>
            <tns:products>
                <tns:products>
                    <id>1</id>
                    <quantity>1</quantity>
                </tns:products>
                <tns:products>
                    <id>4</id>
                    <quantity>1</quantity>
                </tns:products>
                <tns:products>
                    <id>44</id>
                    <quantity>1</quantity>
                </tns:products>
            </tns:products>
            <tns:deliveryTime>10</tns:deliveryTime>
        </tns:checkSupply>
    </soap:Body>
</soap:Envelope>
                                                * Respuesta: Ejemplo de respuesta
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"  xmlns:tns="WebServices.WarehouseWsdl">
    <soap:Body>
        <tns:checkSupplyResponse>
            <tns:name>Big World</tns:name>
            <tns:workingHours>
                <start>5</start>
                <end>20</end>
            </tns:workingHours>
            <tns:price>9.5</tns:price>
            <tns:isWarehouseWorking>true</tns:isWarehouseWorking>
            <tns:isItemsAvailable>false</tns:isItemsAvailable>
            <tns:percentOfAvailableItems>33</tns:percentOfAvailableItems>
            <tns:availableProducts>
                <tns:availableProducts>
                    <id>1</id>
                    <quantity>1</quantity>
                </tns:availableProducts>
            </tns:availableProducts>
        </tns:checkSupplyResponse>
    </soap:Body>
</soap:Envelope>
Warehouses - Almacén: "Everything You Need"
post
/everything-you-need/v1/calculate
                                                * Ejemplos de encabezados
{
    "Content-Type": "application/json"
}
Parámetro
Campo
	Tipo
	Descripción
	deliveryTime
	number
	Plazo de entrega previsto
	products
	Array
	Lista de productos
	  id
	number
	Identificador del producto de la tabla product_model
	  quantity
	number
	Cantidad de producto
	                                                * Ejemplo de solicitud
{
    "deliveryTime": 9,
    "products": [
        {
            "id": 1,
            "quantity": 1
        },
        {
            "id": 4,
            "quantity": 3
        }
    ]
}
                                                * Respuesta: Ejemplo de respuesta
HTTP/1.1 200 OK
{
       "name": "Everything You Need",
       "workingHours": { "start": 8, "end": 23 },
       "price": 10,
       "availableProducts": [
           { "id": 1, "quantity": 2 }
       ],
       "isWarehouseWorking": true,
       "isItemsAvailable": true,
       "percentOfAvailableItems": 80
   }
Warehouses - Almacén: "Food City"
Interacción a través de XML
post
/food-city/calculate.xml
                                                * Ejemplos de encabezados
{
    "Content-Type": "application/xml"
}
Parámetro
Campo
	Tipo
	Descripción
	deliveryTime
	number
	Plazo de entrega previsto
	products
	Array
	Lista de productos
	  id
	number
	Identificador del producto de la tabla product_model
	  quantity
	number
	Cantidad de producto
	                                                * Ejemplo de solicitud
<?xml version="1.0" encoding="UTF-8"?>
<InputModel>
    <deliveryTime>9</deliveryTime>
    <product id="5" quantity="2" />
    <product id="4" quantity="1" />
</InputModel>
                                                * Respuesta: Ejemplo de respuesta
<response name="Food City" price="8" isWarehouseWorking="true" isItemsAvailable="true" percentOfAvailableItems="100">
    <working_hours>
       <start>8</start>
       <end>21</end>
    </working_hours>
    <available_products>
       <product id="5" quantity="6"/>
       <product id="4" quantity="12"/>
    </available_products>
</response>
Warehouses - Comprobar la cantidad de productos en stock
La versión SOAP de este punto final se llama - [SOAP] Comprobar la cantidad de productos en stock
post
/api/v1/warehouses/amount
                                                * [JSON] Ejemplos de encabezados
                                                * [XML] Ejemplos de encabezados
{
    "Content-Type": "application/json"
}
Parámetro
Campo
	Tipo
	Descripción
	ids
	number[]
	Una matriz de identificadores de productos (después de id en la tabla product_model).
	dataType
opcional
	string
	Formato de los datos de entrada. Puede tomar valores:
                                                * "json" - El cuerpo de la solicitud se espera en formato JSON
                                                * "xml" - El cuerpo de la solicitud se espera en formato XML
Valor por defecto: json
	                                                * [JSON] Comprobar la cantidad de productos
                                                * [XML] Comprobar la cantidad de productos
{
    "ids": [
        1,
        4,
        44
    ]
}
                                                * Respuesta: En qué almacén, qué hay disponible y cuánto
HTTP/1.1 200 OK
{
       "Everything You Need": {
           "Refresco Sprite": 9,
           "Gourmet Palomitas Kernels": 6
       },
       "Food City": {
           "Orange Juice - Cold-Pressed, No Added Sugar, Preservative Free": 3,
           "Refresco Sprite": 12
       },
       "Big World": {
           "Orange Juice - Cold-Pressed, No Added Sugar, Preservative Free": 1
       },
       "Fresh food": {
           "Orange Juice - Cold-Pressed, No Added Sugar, Preservative Free": 3,
           "Refresco Sprite": 12
       }
   }
Warehouses - Comprobar la disponibilidad de productos en los almacenes
post
/api/v1/warehouses/check
                                                * Ejemplos de encabezados
{
    "Content-Type": "application/json"
}
Parámetro
Campo
	Tipo
	Descripción
	products
	number[]
	Una matriz de identificadores de productos and their quantities (Campos id en la tabla product_model).
	                                                * Comprobar la disponibilidad de productos
{
    "products": [
        {
            "id": 5,
            "quantity": 1
        },
        {
            "id": 4,
            "quantity": 5
        }
    ]
}
                                                * Respuesta: En qué almacén, qué hay disponible y cuánto
HTTP/1.1 200 OK
{
       "Everything You Need": {
           "Refresco Sprite": true,
           "Gourmet Palomitas Kernels": true,
           "Orange Juice - Cold-Pressed, No Added Sugar, Preservative Free": false
       },
       "Food City": {
           "Orange Juice - Cold-Pressed, No Added Sugar, Preservative Free": true,
           "Refresco Sprite": true,
           "Gourmet Palomitas Kernels": false
       },
       "Big World": {
           "Orange Juice - Cold-Pressed, No Added Sugar, Preservative Free": true,
           "Refresco Sprite": false,
           "Gourmet Palomitas Kernels": false
       },
       "Fresh food": {
           "Orange Juice - Cold-Pressed, No Added Sugar, Preservative Free": true,
           "Refresco Sprite": true,
           "Gourmet Palomitas Kernels": false
       }
   }
Warehouses - Obtener la lista de almacenes
get
/api/v1/warehouses
                                                * Respuesta: Obtener la lista de almacenes con éxito
HTTP/1.1 200 OK
[
    {
           "name": "Everything You Need",
           "workingHours": {
               "start": 7,
               "end": 23
           }
       },
    {
           "name": "Fresh food",
           "workingHours": {
               "start": 8,
               "end": 23
           }
       },
    {
           "name": "Food City",
           "workingHours": {
               "start": 8,
               "end": 21
           }
       },
    {
           "name": "Big World",
           "workingHours": {
               "start": 5,
               "end": 20
           }
       }
    ]
Warehouses - Wharehouse: "Fresh Food"
post
/fresh-food/v2.0.1/ct
                                                * Ejemplos de encabezados
{
    "Content-Type": "application/json"
}
Parámetro
Campo
	Tipo
	Descripción
	deliveryTime
	number
	Plazo de entrega previsto
	products
	Array
	Lista de productos
	  id
	number
	Identificador del producto de la tabla product_model
	  quantity
	number
	Cantidad de producto
	                                                * Ejemplo de solicitud
{
    "deliveryTime": 9,
    "products": [
        {
            "id": 1,
            "quantity": 1
        },
        {
            "id": 4,
            "quantity": 3
        }
    ]
}
                                                * Respuesta: Ejemplo de respuesta
HTTP/1.1 200 OK
{
       "name": "Fresh food",
       "workingHours": { "start": 8, "end": 23 },
       "price": 10,
       "availableProducts": [
           { "id": 1, "quantity": 2 }
       ],
       "isWarehouseWorking": true,
       "isItemsAvailable": true,
       "percentOfAvailableItems": 80
   }
Warehouses - [SOAP] Comprobar la cantidad de productos en stock
post
/api/wsdl
Parámetro
Campo
	Tipo
	Descripción
	ids
	number[]
	Una matriz de identificadores de productos (después de id en la tabla product_model).
	                                                * [XML] Comprobar la cantidad de productos
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  xmlns:tns="WebServices.MainWsdl">
    <soap:Body>
        <Request xmlns="WebServices.MainWsdl">
            <ids>1</ids>
            <ids>4</ids>
            <ids>44</ids>
        </Request>
    </soap:Body>
</soap:Envelope>
                                                * Respuesta: En qué almacén, qué hay disponible y cuánto
   HTTP/1.1 200 OK
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"  xmlns:tns="WebServices.MainWsdl">
    <soap:Body>
        <Response>
            <name>Everything You Need</name>
            <products>
                <name>Refresco Sprite</name>
                <quantity>9</quantity>
            </products>
            <products>
                <name>Gourmet Palomitas Kernels</name>
                <quantity>6</quantity>
            </products>
        </Response>
        <Response>
            <name>Food City</name>
            <products>
                <name>Orange Juice - Cold-Pressed, No Added Sugar, Preservative Free</name>
                <quantity>3</quantity>
            </products>
            <products>
                <name>Refresco Sprite</name>
                <quantity>12</quantity>
            </products>
        </Response>
        <Response>
            <name>Big World</name>
            <products>
                <name>Orange Juice - Cold-Pressed, No Added Sugar, Preservative Free</name>
                <quantity>1</quantity>
            </products>
        </Response>
        <Response>
            <name>Fresh food</name>
            <products>
                <name>Orange Juice - Cold-Pressed, No Added Sugar, Preservative Free</name>
                <quantity>3</quantity>
            </products>
            <products>
                <name>Refresco Sprite</name>
                <quantity>12</quantity>
            </products>
        </Response>
    </soap:Body>
</soap:Envelope>
Couriers
Couriers - Comprobar los costes de envío
post
/api/v1/couriers/check
                                                * Ejemplos de encabezados
{
    "Content-Type": "application/json"
}
Parámetro
Campo
	Tipo
	Descripción
	products
	number[]
	Una matriz de identificadores de productos and their quantities (después de id en la tabla product_model).
	deliveryTime
	number
	Plazo de entrega previsto (from 0 to 23)
	                                                * Comprobar los costes de los diferentes servicios
{
    "products": [
        {
            "id": 1,
            "quantity": 3
        },
        {
            "id": 4,
            "quantity": 1
        },
        {
            "id": 9,
            "quantity": 3
        }
    ],
    "deliveryTime": 7
}
                                                * Respuesta: Cuánto costaría cada uno de los servicios
HTTP/1.1 200 OK
{
       "Fast Delivery": {
           "deliveryPrice": 0
       },
       "Speedy": {
           "deliveryPrice": 99
       },
       "Food Service": {
           "deliveryPrice": 0
       },
       "Order and Go": {
           "deliveryPrice": 99
       }
   }
Couriers - Entrega: "Fast Delivery"
La interacción se realiza mediante XML
post
/fast-delivery/v3.1.1/calculate-delivery.xml
                                                * Ejemplos de encabezados
{
    "Content-Type": "application/xml"
}
Parámetro
Campo
	Tipo
	Descripción
	productsCount
	number
	Número de productos en el pedido
	productsWeight
	number
	Peso de los productos
	deliveryTime
	number
	Plazo de entrega previsto
	                                                * Ejemplo de solicitud
<InputModel>
    <productsCount>2</productsCount>
    <productsWeight>5.115</productsWeight>
    <deliveryTime>20</deliveryTime>
</InputModel>
                                                * Respuesta: Ejemplo de respuesta
HTTP/1.1 200 OK
<response name="Fast Delivery" isItPossibleToDeliver="true" hostDeliveryCost="43" clientDeliveryCost="0">
    <toBeDeliveredTime>
        <min>25</min>
        <max>30</max>
    </toBeDeliveredTime>
</response>
Couriers - Entrega: "Food Service"
Interacción a través de SOAP
post
/food-service/wsdl
Parámetro
Campo
	Tipo
	Descripción
	productsCount
	number
	Número de productos en el pedido
	productsWeight
	number
	Peso de los productos
	deliveryTime
	number
	Plazo de entrega previsto
	                                                * Ejemplo de solicitud
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  xmlns:tns="WebServices.CourierWsdl">
    <soap:Body>
        <Request xmlns="WebServices.CourierWsdl">
            <productsCount>3</productsCount>
            <productsWeight>1.433</productsWeight>
            <deliveryTime>7</deliveryTime>
        </Request>
    </soap:Body>
</soap:Envelope>
                                                * Respuesta: Ejemplo de respuesta
HTTP/1.1 200 OK
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"  xmlns:tns="WebServices.CourierWsdl">
    <soap:Body>
        <Response xmlns="WebServices.CourierWsdl">
        <name>Food Service</name>
        <isItPossibleToDeliver>true</isItPossibleToDeliver>
        <hostDeliveryCost>29</hostDeliveryCost>
        <toBeDeliveredTime>
            <min>25</min>
            <max>30</max>
        </toBeDeliveredTime>
        <clientDeliveryCost>0</clientDeliveryCost>
        </Response>
    </soap:Body>
</soap:Envelope>
Couriers - Entrega: "Order and Go"
post
/order-and-go/v1/delivery
                                                * Ejemplos de encabezados
{
    "Content-Type": "application/json"
}
Parámetro
Campo
	Tipo
	Descripción
	productsCount
	number
	Número de productos en el pedido
	productsWeight
	number
	Peso de los productos
	deliveryTime
	number
	Plazo de entrega previsto
	                                                * Ejemplo de solicitud
{
    "deliveryTime": 9,
    "productsCount": 10,
    "productsWeight": 11
}
                                                * Respuesta: Ejemplo de respuesta
HTTP/1.1 200 OK
   {
       "name": "Order and Go",
       "clientDeliveryCost": 10,
       "toBeDeliveredTime": { "min": 10, "max": 20 },
       "hostDeliveryCost": 23,
       "isItPossibleToDeliver": true
   }
Couriers - Entrega: "Speedy"
post
/speedy/v1/calculate
                                                * Ejemplos de encabezados
{
    "Content-Type": "application/json"
}
Parámetro
Campo
	Tipo
	Descripción
	productsCount
	number
	Número de productos en el pedido
	productsWeight
	number
	Peso de los productos
	deliveryTime
	number
	Plazo de entrega previsto
	                                                * Ejemplo de solicitud
{
    "deliveryTime": 9,
    "productsCount": 10,
    "productsWeight": 11
}
                                                * Respuesta: Ejemplo de respuesta
HTTP/1.1 200 OK
   {
       "name": "Speedy",
       "clientDeliveryCost": 10,
       "toBeDeliveredTime": { "min": 10, "max": 20 },
       "hostDeliveryCost": 23,
       "isItPossibleToDeliver": true
   }
Couriers - Obtener la lista de entregas
get
/api/v1/couriers
                                                * Respuesta: Recibir las entregas con éxito
   HTTP/1.1 200 OK
    [
           {
               "name": "Order and Go",
               "workingHours": {
                   "start": 8,
                   "end": 22
               }
           },
           {
               "name": "Speedy",
               "workingHours": {
                   "start": 8,
                   "end": 22
               }
           },
           {
               "name": "Fast Delivery",
               "workingHours": {
                   "start": 7,
                   "end": 21
               }
           },
           {
               "name": "Food Service",
               "workingHours": {
                   "start": 6,
                   "end": 20
               }
           }
]
Main.User
Main.User - Creación de cuenta
post
/api/v1/users
                                                * Ejemplos de encabezados
{
    "Content-Type": "application/json"
}
Parámetro
Campo
	Tipo
	Descripción
	firstName
	string
	Nombre de usuario/a, escrito en el campo firstName de la tabla Users
	phone
	string
	El número de teléfono del/de la usuario/a se escribe en el campo phone de la tabla Users
	address
	string
	La dirección del/de la usuario/a se escribe en el campo address de la tabla Users
	email
opcional
	string
	Dirección de correo electrónico, escrita en el campo email de la tabla Users
	comment
opcional
	string
	Comentario de usuario/a, escrito en el campo comment de la tabla Users
	                                                * Conjunto mínimo de datos
                                                * Información completa sobre el/la usuario/a
{
    "firstName": "Max",
    "phone": "+10005553535",
    "address": "8042 Lancaster Ave.Hamburg, NY"
}
                                                * La cuenta de usuario se ha creado correctamente
HTTP/1.1 201 Creado
{
    authToken: 'jknnFApafP4awfAIFfafam2fma'
}
                                                * Error en los datos de entrada #1
                                                * Error en los datos de entrada #2
                                                * Error en los datos de entrada #3
                                                * Error en los datos de entrada #4
HTTP/1.1 400 Bad request.
{
    "code": 400,
    "message": "No se han aprobado todos los parámetros requeridos. Parámetros requeridos: nombre, teléfono, dirección"
}
Main.Products
Main.Products - Búsqueda de kit por producto
endpoint para buscar kit que contengan los productos especificados
post
/api/v1/products/kits
                                                * Ejemplos de encabezados
{
    "Content-Type": "application/json"
}
Parámetro
Campo
	Tipo
	Descripción
	ids
	number[]
	Una matriz de identificadores de productos from the table product_model.
	                                                * Buscar kit que contengan el producto 1 o 2 o 3:
{
    "ids": [
        1,
        2,
        3
    ]
}
                                                * Respuesta: Recibir las kit con éxito
HTTP/1.1 200 OK
[
    {
           "id": 1,
           "name": "Para pícnics",
           "productsList": [
               {
                   "id": 1,
                   "quantity": 1
               },
               {
                   "id": 2,
                   "quantity": 1
               },
               {
                   "id": 3,
                   "quantity": 1
               },
               {
                   "id": 4,
                   "quantity": 1
               },
               {
                   "id": 5,
                   "quantity": 1
               },
               {
                   "id": 6,
                   "quantity": 1
               },
               {
                   "id": 7,
                   "quantity": 1
               },
               {
                   "id": 8,
                   "quantity": 1
               },
               {
                   "id": 9,
                   "quantity": 1
               },
               {
                   "id": 10,
                   "quantity": 1
               },
               {
                   "id": 11,
                   "quantity": 1
               },
               {
                   "id": 12,
                   "quantity": 1
               },
               {
                   "id": 13,
                   "quantity": 1
               },
               {
                   "id": 14,
                   "quantity": 1
               },
               {
                   "id": 15,
                   "quantity": 1
               },
               {
                   "id": 16,
                   "quantity": 1
               },
               {
                   "id": 17,
                   "quantity": 1
               },
               {
                   "id": 18,
                   "quantity": 1
               },
               {
                   "id": 19,
                   "quantity": 1
               },
               {
                   "id": 20,
                   "quantity": 1
               },
               {
                   "id": 21,
                   "quantity": 1
               },
               {
                   "id": 22,
                   "quantity": 1
               },
               {
                   "id": 23,
                   "quantity": 1
               },
               {
                   "id": 24,
                   "quantity": 1
               },
               {
                   "id": 25,
                   "quantity": 1
               },
               {
                   "id": 26,
                   "quantity": 1
               },
               {
                   "id": 27,
                   "quantity": 1
               },
               {
                   "id": 28,
                   "quantity": 1
               },
               {
                   "id": 29,
                   "quantity": 1
               },
               {
                   "id": 30,
                   "quantity": 1
               },
               {
                   "id": 31,
                   "quantity": 1
               },
               {
                   "id": 32,
                   "quantity": 1
               },
               {
                   "id": 33,
                   "quantity": 1
               },
               {
                   "id": 34,
                   "quantity": 1
               },
               {
                   "id": 35,
                   "quantity": 1
               },
               {
                   "id": 36,
                   "quantity": 1
               },
               {
                   "id": 37,
                   "quantity": 1
               },
               {
                   "id": 38,
                   "quantity": 1
               },
               {
                   "id": 39,
                   "quantity": 1
               }
           ],
           "productsCount": 39
       },
    {
           "id": 2,
           "name": "Para películas y series",
           "productsList": [
               {
                   "id": 7,
                   "quantity": 1
               },
               {
                   "id": 8,
                   "quantity": 1
               },
               {
                   "id": 9,
                   "quantity": 1
               },
               {
                   "id": 40,
                   "quantity": 1
               },
               {
                   "id": 41,
                   "quantity": 1
               },
               {
                   "id": 42,
                   "quantity": 1
               },
               {
                   "id": 43,
                   "quantity": 1
               },
               {
                   "id": 44,
                   "quantity": 1
               },
               {
                   "id": 45,
                   "quantity": 1
               },
               {
                   "id": 46,
                   "quantity": 1
               },
               {
                   "id": 47,
                   "quantity": 1
               },
               {
                   "id": 2,
                   "quantity": 1
               },
               {
                   "id": 3,
                   "quantity": 1
               },
               {
                   "id": 4,
                   "quantity": 1
               },
               {
                   "id": 48,
                   "quantity": 1
               },
               {
                   "id": 49,
                   "quantity": 1
               },
               {
                   "id": 50,
                   "quantity": 1
               },
               {
                   "id": 51,
                   "quantity": 1
               },
               {
                   "id": 52,
                   "quantity": 1
               },
               {
                   "id": 53,
                   "quantity": 1
               },
               {
                   "id": 54,
                   "quantity": 1
               },
               {
                   "id": 55,
                   "quantity": 1
               },
               {
                   "id": 56,
                   "quantity": 1
               },
               {
                   "id": 57,
                   "quantity": 1
               },
               {
                   "id": 58,
                   "quantity": 1
               },
               {
                   "id": 59,
                   "quantity": 1
               },
               {
                   "id": 60,
                   "quantity": 1
               }
           ],
           "productsCount": 27
       }
    ]
Main.Products - Cambio del precio del producto
put
/api/v1/products/:id
                                                * Ejemplos de encabezados
{
    "Content-Type": "application/json"
}
Parámetro
Campo
	Tipo
	Descripción
	id
	number
	El id de la kit en la tabla product_model. Se pasa en la URL
	price
opcional
	string
	price del producto. Se pasa en el texto de la solicitud.
	                                                * Cambio del producto /api/v1/products/7
{
    "price": 175
}
                                                * Respuesta: El kit ha sido eliminado con éxito.
HTTP/1.1 200 OK
{
       "ok": true
   }
                                                * Error: Producto no encontrado
HTTP/1.1 404 Not found.
{
       "code": 404,
       "message": "Not found"
   }
Main.Kits
Main.Kits - Añadir productos a la kit:
post
/api/v1/kits/:id/products
                                                * Ejemplos de encabezados
{
    "Content-Type": "application/json"
}
Parámetro
Campo
	Tipo
	Descripción
	id
	number
	El id de kit en la tabla kit_model. Se pasa en la URL
	productsList
	Array
	Una lista de productos que se agregarán al kit. La lista contiene los ID de los artículos y sus cantidades. Debe enviarse en el cuerpo de la solicitud.
	                                                * Ejemplo de cuerpo de solicitud para agregar artículos al kit
{
    "productsList": [
        {
            "id": 1,
            "quantity": 2
        },
        {
            "id": 6,
            "quantity": 2
        }
    ]
}
                                                * Respuesta: Completar con éxito la kit de productos
    HTTP/1.1 200 OK
 {
    "id": 2,
    "name": "Mi conjunto del fin de semana",
    "productsList": [
        {
            "id": 1,
            "name": "Caviar rojo",
            "price": 45,
            "weight": 5,
            "units": "kg",
            "quantity": 2
        },
        {
            "id": 5,
            "name": "Baguette",
            "price": 15,
            "weight": 1,
            "units": "kg",
            "quantity": 2
        }
    ],
    "productsCount": 4
}
                                                * Error: No se han encontrado kits coincidentes
                                                * Error: El formato del JSON enviado no es correcto
                                                * Error: El valor en alguno de los parametros es incorrecto
HTTP/1.1 404 Not found.
{
       "code": 404,
       "message": "Not found"
   }
Main.Kits - Cambio de la kit
put
/api/v1/kits/:id
                                                * Ejemplos de encabezados
{
    "Content-Type": "application/json"
}
Parámetro
Campo
	Tipo
	Descripción
	id
	number
	El id de kit en la tabla kit_model. Se pasa en la URL
	name
opcional
	string
	name de la kit. Se pasa en el texto de la solicitud.
	productsList
opcional
	Array
	Una lista de productos que se agregarán al kit. La lista contiene los ID de los artículos y sus cantidades. Debe enviarse en el cuerpo de la solicitud.
	                                                * Cambio de la kit /api/v1/kits/7
{
    "name": "Mi kit modificada",
    "productsList": [
        {
            "id": 1,
            "quantity": 4
        },
        {
            "id": 5,
            "quantity": 2
        },
        {
            "id": 3,
            "quantity": 1
        },
        {
            "id": 4,
            "quantity": 1
        }
    ]
}
                                                * Respuesta: El kit ha sido eliminado con éxito.
HTTP/1.1 200 OK
{
       "ok": true
   }
                                                * Error: No se han encontrado kits coincidentes
HTTP/1.1 404 Not found.
{
       "code": 404,
       "message": "Not found"
   }
Main.Kits - Crear un kit
endpoint para crear una kit de una tarjeta específica O de usuario.
                                                * Es obligatorio pasar el encabezado Authorisation O el parámetro cardId, para crear la kit
                                                * Si se recibe una solicitud con un encabezado Authorisation que contenga el authToken de un/a usuario/a en particular - se creará la kit de este/a usuario/a.
                                                * Si se recibe el parámetro cardId, se creará una kit dentro de la tarjeta correspondiente
                                                * Si no se pasa ninguno de los parámetros, se devolverá un error.
                                                * Cuando se pasan ambos parámetros, Authorization es la prioridad
post
/api/v1/kits
Header
Campo
	Tipo
	Descripción
	Authorization
opcional
	string
	Encabezado de autorización en formato Bearer {authToken}. Cuando se pasa - se devuelven todos las cestas creadas por el/la usuario/a.
	Content-Type
opcional
	string
	Valor por defecto: application/json
	                                                * Ejemplos de encabezados
                                                * Recepción de las cestas creadas por el/la usuario/a
{
    "Content-Type": "application/json"
}
Parámetro
Campo
	Tipo
	Descripción
	cardId
opcional
	number
	El id de la tarjeta en la tabla card_model. Cuando se pasa - se creará un conjunto incluido en esta tarjeta
	name
	string
	El nombre de la kit, que será escrito en el campo correspondiente de la tabla kit_model.
	                                                * Respuesta: El conjunto ha sido creado con éxito
HTTP/1.1 201 Creado
{
       "name": "Mi conjunto",
       "card": {
           "id": 1,
           "name": "Para la situación"
       },
       "productsList": null,
       "id": 7,
       "productsCount": 0
   }
                                                * Error: No se ha transmitido ninguno de los parámetros
                                                * Error: Validación del nombre
HTTP/1.1 400 Bad request.
{
       "code": 400,
       "message": "No se han aprobado todos los parámetros requeridos"
   }
Main.Kits - Eliminación del kit
delete
/api/v1/kits/:id
Parámetro
Campo
	Tipo
	Descripción
	id
	number
	El id de kit en la tabla kit_model. Se pasa en la URL
	                                                * Eliminación de un kit con id=7
/api/v1/kits/7
                                                * Respuesta: El kit ha sido eliminado con éxito.
HTTP/1.1 200 OK
{
       "ok": true
   }
Main.Kits - Recibir todas las kit
endpoint para recuperar todas las kit dentro de una tarjeta específica O las kit creadas por el/la usuario/a.
                                                * Es obligatorio pasar el encabezado Authorisation O el parámetro cardId, para recibir las kit
                                                * Si se recibe una solicitud con un encabezado Authorisation que contenga el authToken de un/a usuario/a en particular - se devolverán las kit creadas por ese/a usuario/a.
                                                * Si se recibe el parámetro de consulta cardId, se devolverán las kit relativas a la tarjeta.
                                                * Si no se pasa ninguno de los parámetros, se devolverá un error.
                                                * Cuando se pasan ambos parámetros, Authorization es la prioridad
get
/api/v1/kits
Header
Campo
	Tipo
	Descripción
	Authorization
opcional
	string
	Encabezado de autorización en formato Bearer {authToken}. Cuando se pasa - se devuelven todos las kit creadas por el/la usuario/a.
	                                                * Recepción de las kit creadas por el/la usuario/a
{
    "Authorization": "Bearer jknnFApafP4awfAIFfafam2fma"
}
Parámetro
Campo
	Tipo
	Descripción
	cardId
opcional
	number
	El id de la tarjeta en la tabla card_model. Cuando se pasa - se devuelven todos las kit incluidas en la tarjeta.
	                                                * Recibir las kit dentro de una tarjeta with id = 1
/api/v1/kits?cardId=1
                                                * Respuesta: Recibir las kit con éxito
HTTP/1.1 200 OK
[
    {
           "id": 1,
           "name": "Para pícnics",
           "productsList": [
               {
                   "id": 1,
                   "name": "Orange Juice - Cold-Pressed, No Added Sugar, Preservative Free",
                   "price": 149,
                   "weight": 473,
                   "units": "ml",
                   "quantity": 1
               },
               {
                   "id": 2,
                   "name": "Refresco Mountain Dew",
                   "price": 89,
                   "weight": 1,
                   "units": "l",
                   "quantity": 1
               },
               {
                   "id": 3,
                   "name": "Refresco Pepsi",
                   "price": 109,
                   "weight": 1,
                   "units": "l",
                   "quantity": 1
               },
               {
                   "id": 4,
                   "name": "Refresco Sprite",
                   "price": 79,
                   "weight": 900,
                   "units": "ml",
                   "quantity": 1
               },
               {
                   "id": 5,
                   "name": "Jugo Fruit Power: Lichi",
                   "price": 349,
                   "weight": 900,
                   "units": "ml",
                   "quantity": 1
               },
               {
                   "id": 6,
                   "name": "Baguette",
                   "price": 69,
                   "weight": 160,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 7,
                   "name": "Papas fritas: Saladas Clásicas",
                   "price": 119,
                   "weight": 150,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 8,
                   "name": "Papas fritas: Paprika",
                   "price": 199,
                   "weight": 150,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 9,
                   "name": "Papas Fritas: Chile",
                   "price": 209,
                   "weight": 100,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 10,
                   "name": "Pita",
                   "price": 99,
                   "weight": 300,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 11,
                   "name": "Pan multigrano",
                   "price": 149,
                   "weight": 400,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 12,
                   "name": "Pan de ajo",
                   "price": 75,
                   "weight": 225,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 13,
                   "name": "Mini chapata",
                   "price": 45,
                   "weight": 107,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 14,
                   "name": "Brioche",
                   "price": 79,
                   "weight": 79,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 15,
                   "name": "Salchichas vienesas",
                   "price": 179,
                   "weight": 350,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 16,
                   "name": "Salchichas de pollo",
                   "price": 173,
                   "weight": 200,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 17,
                   "name": "Chorizo",
                   "price": 269,
                   "weight": 420,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 18,
                   "name": "Salchichón",
                   "price": 175,
                   "weight": 464,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 19,
                   "name": "Salami",
                   "price": 99,
                   "weight": 190,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 20,
                   "name": "Bacon",
                   "price": 269,
                   "weight": 500,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 21,
                   "name": "Pastrami",
                   "price": 143,
                   "weight": 200,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 22,
                   "name": "Pepperoni",
                   "price": 329,
                   "weight": 500,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 23,
                   "name": "Anti-Bacterial Hand Sanitizer",
                   "price": 139,
                   "weight": 50,
                   "units": "ml",
                   "quantity": 1
               },
               {
                   "id": 24,
                   "name": "Paper Napkin - Large",
                   "price": 99,
                   "weight": 60,
                   "units": "pzas",
                   "quantity": 1
               },
               {
                   "id": 25,
                   "name": "Anti Bacterial Disinfectant Sanitising Wipes - Alcohol Free",
                   "price": 199,
                   "weight": 48,
                   "units": "pzas",
                   "quantity": 1
               },
               {
                   "id": 26,
                   "name": "SMART Mosquito Repellent",
                   "price": 349,
                   "weight": 100,
                   "units": "ml",
                   "quantity": 1
               },
               {
                   "id": 27,
                   "name": "Manzana verde",
                   "price": 169,
                   "weight": 500,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 28,
                   "name": "Orange",
                   "price": 146,
                   "weight": 500,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 29,
                   "name": "Cherry",
                   "price": 249,
                   "weight": 500,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 30,
                   "name": "Raspberry",
                   "price": 239,
                   "weight": 250,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 31,
                   "name": "Blackberry",
                   "price": 125,
                   "weight": 200,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 32,
                   "name": "Lima",
                   "price": 59,
                   "weight": 1,
                   "units": "pzas",
                   "quantity": 1
               },
               {
                   "id": 33,
                   "name": "Red Grapes",
                   "price": 269,
                   "weight": 500,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 34,
                   "name": "Green Grapes",
                   "price": 179,
                   "weight": 500,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 35,
                   "name": "Banana",
                   "price": 99,
                   "weight": 1000,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 36,
                   "name": "Pear",
                   "price": 199,
                   "weight": 650,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 37,
                   "name": "Blueberry",
                   "price": 199,
                   "weight": 125,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 38,
                   "name": "Pineapple",
                   "price": 385,
                   "weight": 1,
                   "units": "pzas",
                   "quantity": 1
               },
               {
                   "id": 39,
                   "name": "Pear",
                   "price": 145,
                   "weight": 800,
                   "units": "g",
                   "quantity": 1
               }
           ],
           "productsCount": 39
       },
    {
           "id": 2,
           "name": "Para películas y series",
           "productsList": [
               {
                   "id": 2,
                   "name": "Refresco Mountain Dew",
                   "price": 89,
                   "weight": 1,
                   "units": "l",
                   "quantity": 1
               },
               {
                   "id": 3,
                   "name": "Refresco Pepsi",
                   "price": 109,
                   "weight": 1,
                   "units": "l",
                   "quantity": 1
               },
               {
                   "id": 4,
                   "name": "Refresco Sprite",
                   "price": 79,
                   "weight": 900,
                   "units": "ml",
                   "quantity": 1
               },
               {
                   "id": 7,
                   "name": "Papas fritas: Saladas Clásicas",
                   "price": 119,
                   "weight": 150,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 8,
                   "name": "Papas fritas: Paprika",
                   "price": 199,
                   "weight": 150,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 9,
                   "name": "Papas Fritas: Chile",
                   "price": 209,
                   "weight": 100,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 43,
                   "name": "Classic Hummus Dip & Spread",
                   "price": 99,
                   "weight": 150,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 44,
                   "name": "Gourmet Palomitas Kernels",
                   "price": 109,
                   "weight": 60,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 45,
                   "name": "Caramel Palomitas",
                   "price": 99,
                   "weight": 150,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 46,
                   "name": "Fruit Beer Non-Alcoholic",
                   "price": 249,
                   "weight": 250,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 47,
                   "name": "Stella Artois Beer Non-Alcoholic",
                   "price": 179,
                   "weight": 60,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 48,
                   "name": "100% Belgian Dark Chocolate - with Apricot",
                   "price": 89,
                   "weight": 45,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 49,
                   "name": "100% Belgian Dark Chocolate - Raisins",
                   "price": 69,
                   "weight": 450,
                   "units": "ml",
                   "quantity": 1
               },
               {
                   "id": 50,
                   "name": "100% Belgian Milk Chocolate - Sea Salt",
                   "price": 109,
                   "weight": 450,
                   "units": "ml",
                   "quantity": 1
               },
               {
                   "id": 54,
                   "name": "Dairy Rich Chocolate Bar - Fruit & Nut",
                   "price": 139,
                   "weight": 100,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 55,
                   "name": "Peanut Butter Nutty Cookies",
                   "price": 119,
                   "weight": 97,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 56,
                   "name": "Cookies - Orange Splash",
                   "price": 89,
                   "weight": 85,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 57,
                   "name": "Choco Nut Cookies",
                   "price": 159,
                   "weight": 160,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 58,
                   "name": "Milk Cookies",
                   "price": 239,
                   "weight": 100,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 59,
                   "name": "Sandwich Biscuits",
                   "price": 119,
                   "weight": 100,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 60,
                   "name": "Chocobakes Choc Filled Cookies",
                   "price": 139,
                   "weight": 80,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 61,
                   "name": "Baguette French Recipe",
                   "price": 179,
                   "weight": 171,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 62,
                   "name": "Queso Croissant",
                   "price": 119,
                   "weight": 50,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 63,
                   "name": "French Almond Croissant",
                   "price": 119,
                   "weight": 228,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 64,
                   "name": "Chocolate Croissant",
                   "price": 149,
                   "weight": 168,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 65,
                   "name": "Smoked Salmon Croissant",
                   "price": 59,
                   "weight": 100,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 66,
                   "name": "Belgian Chocolate Cake Mix",
                   "price": 219,
                   "weight": 250,
                   "units": "g",
                   "quantity": 1
               }
           ],
           "productsCount": 27
       },
    {
           "id": 3,
           "name": "Sabores de París",
           "productsList": [
               {
                   "id": 54,
                   "name": "Dairy Rich Chocolate Bar - Fruit & Nut",
                   "price": 139,
                   "weight": 100,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 58,
                   "name": "Milk Cookies",
                   "price": 239,
                   "weight": 100,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 67,
                   "name": "Baguette French Recipe",
                   "price": 89,
                   "weight": 200,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 68,
                   "name": "Queso Croissant",
                   "price": 79,
                   "weight": 75,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 69,
                   "name": "French Almond Croissant",
                   "price": 129,
                   "weight": 120,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 70,
                   "name": "Chocolate Croissant",
                   "price": 104,
                   "weight": 96,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 71,
                   "name": "Smoked Salmon Croissant",
                   "price": 119,
                   "weight": 90,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 72,
                   "name": "Belgian Chocolate Cake Mix",
                   "price": 359,
                   "weight": 125,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 73,
                   "name": "Queso para untar: Queso crema",
                   "price": 79,
                   "weight": 130,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 74,
                   "name": "Queso Slices",
                   "price": 239,
                   "weight": 400,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 75,
                   "name": "Queso Spread - Roasted Garlic",
                   "price": 129,
                   "weight": 200,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 76,
                   "name": "Spicy Queso Straw",
                   "price": 229,
                   "weight": 250,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 77,
                   "name": "Rebanadas de queso procesado",
                   "price": 220,
                   "weight": 250,
                   "units": "",
                   "quantity": 1
               },
               {
                   "id": 78,
                   "name": "Cubos de queso procesado",
                   "price": 399,
                   "weight": 200,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 79,
                   "name": "Soyabean Tempeh Cubes",
                   "price": 209,
                   "weight": 300,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 82,
                   "name": "Center Filled Dark Chocolate Cookies",
                   "price": 129,
                   "weight": 100,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 83,
                   "name": "Enrobed Cinnamon Milk Chocolate Dipped Cookies",
                   "price": 225,
                   "weight": 100,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 84,
                   "name": "Oreo & Crème Frozen Dessert",
                   "price": 339,
                   "weight": 300,
                   "units": "ml",
                   "quantity": 1
               },
               {
                   "id": 85,
                   "name": "Chocorich Eclairs Chocolate - Assorted",
                   "price": 429,
                   "weight": 200,
                   "units": "g",
                   "quantity": 1
               }
           ],
           "productsCount": 19
       }
    ]
                                                * Error: No se ha transmitido ninguno de los parámetros
                                                * Error: No se han encontrado kits coincidentes
HTTP/1.1 400 Bad request.
{
       "code": 400,
       "message": "No se han aprobado todos los parámetros requeridos"
   }
Main.Kits - Recibir una kit por el nombre
get
/api/v1/kits/search
Parámetro
Campo
	Tipo
	Descripción
	name
	string
	name de la kit en la tabla kit_model.
	                                                * Recibir una kit con un nombre "Sabores de París"
/api/v1/kits/search?name=Sabores%20de%20París
                                                * Respuesta: El conjunto ha sido recibido con éxito.
HTTP/1.1 200 OK
{
       "id": 3,
       "name": "Sabores de París",
       "productsList": [
           {
               "id": 54,
               "name": "Dairy Rich Chocolate Bar - Fruit & Nut",
               "price": 139,
               "weight": 100,
               "units": "g",
               "quantity": 6
           },
           {
               "id": 58,
               "name": "Milk Cookies",
               "price": 239,
               "weight": 100,
               "units": "g"
               "quantity": 8
           },
           {
               "id": 67,
               "name": "Baguette French Recipe",
               "price": 89,
               "weight": 200,
               "units": "g",
               "quantity": 4
           },
           {
               "id": 68,
               "name": "Queso Croissant",
               "price": 79,
               "weight": 75,
               "units": "g",
               "quantity": 1
           },
           {
               "id": 69,
               "name": "French Almond Croissant",
               "price": 129,
               "weight": 120,
               "units": "g",
               "quantity": 7
           },
           {
               "id": 70,
               "name": "Chocolate Croissant",
               "price": 104,
               "weight": 96,
               "units": "g",
               "quantity": 1
           },
           {
               "id": 71,
               "name": "Smoked Salmon Croissant",
               "price": 119,
               "weight": 90,
               "units": "g",
               "quantity": 1
           },
           {
               "id": 72,
               "name": "Belgian Chocolate Cake Mix",
               "price": 359,
               "weight": 125,
               "units": "g",
               "quantity": 1
           },
           {
               "id": 73,
               "name": "Queso para untar: Queso crema",
               "price": 79,
               "weight": 130,
               "units": "g",
               "quantity": 1
           },
           {
               "id": 74,
               "name": "Queso Slices",
               "price": 239,
               "weight": 400,
               "units": "g",
               "quantity": 1
           },
           {
               "id": 75,
               "name": "Queso Spread - Roasted Garlic",
               "price": 129,
               "weight": 200,
               "units": "g",
               "quantity": 1
           },
           {
               "id": 76,
               "name": "Spicy Queso Straw",
               "price": 229,
               "weight": 250,
               "units": "g",
               "quantity": 1
           },
           {
               "id": 77,
               "name": "Rebanadas de queso procesado",
               "price": 220,
               "weight": 250,
               "units": "g",
               "quantity": 1
           },
           {
               "id": 78,
               "name": "Cubos de queso procesado",
               "price": 399,
               "weight": 200,
               "units": "g",
               "quantity": 1
           },
           {
               "id": 79,
               "name": "Soyabean Tempeh Cubes",
               "price": 209,
               "weight": 300,
               "units": "g",
               "quantity": 1
           },
           {
               "id": 82,
               "name": "Center Filled Dark Chocolate Cookies",
               "price": 129,
               "weight": 100,
               "units": "g",
               "quantity": 1
           },
           {
               "id": 83,
               "name": "Enrobed Cinnamon Milk Chocolate Dipped Cookies",
               "price": 225,
               "weight": 100,
               "units": "g",
               "quantity": 1
           },
           {
               "id": 84,
               "name": "Oreo & Crème Frozen Dessert",
               "price": 339,
               "weight": 300,
               "units": "ml",
               "quantity": 1
           },
           {
               "id": 85,
               "name": "Chocorich Eclairs Chocolate - Assorted",
               "price": 429,
               "weight": 200,
               "units": "g",
               "quantity": 1
           }
       ],
       "productsCount": 19
   }
                                                * Error: No se han encontrado kits coincidentes
HTTP/1.1 404 Not found.
{
       "code": 404,
       "message": "Not found"
   }
Main.Basket
Main.Basket - Añadir productos a la cesta
put
/api/v1/orders/:id
                                                * Ejemplos de encabezados
{
    "Content-Type": "application/json"
}
Parámetro
Campo
	Tipo
	Descripción
	id
	number
	id de la cesta en la tabla order_model. Se pasa en la URL
	productsList
	Array
	Una lista de productos que se agregarán al cesta. La lista contiene los ID de los artículos y sus cantidades. Debe enviarse en el cuerpo de la solicitud.
	                                                * Añadir productos a la cesta
{
    "productsList": [
        {
            "id": 1,
            "quantity": 4
        },
        {
            "id": 5,
            "quantity": 2
        },
        {
            "id": 3,
            "quantity": 1
        },
        {
            "id": 4,
            "quantity": 1
        }
    ]
}
                                                * Respuesta: Los artículos se han añadido a la cesta con éxito
HTTP/1.1 200 OK
 {
"productsList": [
    {
        "id": 1,
        "quantity": 10
    },
    {
        "id": 5,
        "quantity": 10
    },
    {
        "id": 3,
        "quantity": 9
    },
    {
        "id": 4,
        "quantity": 5
    }
],
        "status": 0,
        "deliveryPriceOur": 30,
        "deliveryTime": "25~30",
        "courierService": "Fast Delivery",
        "deliveryPrice": 0,
        "wareHouse": "Fresh food",
        "userId": 1,
        "id": 5,
        "productsCost": 75,
        "finalCCost": 174
    }
                                                * Error: Cesta no encontrada
                                                * Error: No hay un almacén para procesar tu pedido
HTTP/1.1 404 Not found.
{
       "code": 404,
       "message": "Not found"
Main.Basket - Crear una cesta
post
/api/v1/orders
                                                * Ejemplos de encabezados
{
    "Content-Type": "application/json"
}
Parámetro
Campo
	Tipo
	Descripción
	productsList
	Array
	Una lista de productos que se agregarán al cesta. La lista contiene los ID de los artículos y sus cantidades. Debe enviarse en el cuerpo de la solicitud.
	deliveryTime
opcional
	number
	Plazo de entrega previsto. Si no se pasa ningún valor, el sistema utiliza la hora actual
	                                                * Crear una cesta
{
    "productsList": [
        {
            "id": 1,
            "quantity": 2
        },
        {
            "id": 5,
            "quantity": 2
        },
        {
            "id": 3,
            "quantity": 1
        }
    ]
}
                                                * Respuesta: La cesta fue creada con éxito
HTTP/1.1 200 OK
{
       "productsList": [
           {
               "id": 1,
               "quantity": 2
           },
           {
               "id": 5,
               "quantity": 2
           },
           {
               "id": 3,
               "quantity": 1
           }
       ],
       "status": 0,
       "deliveryPriceOur": 30,
       "deliveryTime": "25~30",
       "courierService": "Fast Delivery",
       "deliveryPrice": 99,
       "wareHouse": "Fresh food",
       "userId": 1,
       "id": 5,
       "productsCost": 75,
       "finalCCost": 174
   }
                                                * Error: No se han aprobado todos los parámetros requeridos
                                                * Error: No hay un almacén para procesar tu pedido
HTTP/1.1 400 Bad request.
{
       "code": 400,
       "message": "No se han aprobado todos los parámetros requeridos"
   }
Main.Basket - Eliminar la cesta
delete
/api/v1/orders/:id
Parámetro
Campo
	Tipo
	Descripción
	id
	number
	id de la cesta en la tabla order_model. Se pasa en la URL
	                                                * Respuesta: Eliminar una cesta con éxito
HTTP/1.1 200 OK
{
       "ok": true
   }
Main.Basket - Hacer el pedido
put
/api/v1/orders/:id/complete
Parámetro
Campo
	Tipo
	Descripción
	id
	number
	id de la cesta en la tabla order_model. Se pasa en la URL
	                                                * Respuesta: Los artículos se han añadido a la cesta con éxito
HTTP/1.1 200 OK
{
       "ok": true,
   }
                                                * Error: El authToken no ha sido transmitido
HTTP/1.1 401 Unauthorized.
{
       "code": 401,
       "message": "No autorizado",
   }
Main.Basket - Recibir los productos de la cesta
get
/api/v1/orders/:id
Header
Campo
	Tipo
	Descripción
	Authorization
opcional
	string
	Encabezado de autorización en formato Bearer {authToken}.
	                                                * Ejemplo de autorización
{
    "Authorization": "Bearer jknnFApafP4awfAIFfafam2fma"
}
Parámetro
Campo
	Tipo
	Descripción
	id
	string
	id de la cesta en la tabla order_model. Se pasa por el parámetro de URL
	                                                * Recibir la cesta
/api/v1/orders/6
                                                * Respuesta: Los productos de la cesta recibidos con éxito
HTTP/1.1 200 OK
[
    {
           "id": 1,
           "name": "Orange Juice - Cold-Pressed, No Added Sugar, Preservative Free",
           "price": 149,
           "weight": 473,
           "units": "ml",
           "quantity": 3
       },
    {
           "id": 4,
           "name": "Refresco Sprite",
           "price": 79,
           "weight": 900,
           "units": "ml",
           "quantity": 4
       }
    ]
                                                * Error: El authToken no ha sido transmitido
                                                * Error: Cesta no encontrada
HTTP/1.1 401 Unauthorized.
{
       "code": 401,
       "message": "No autorizado",
   }
Main.Orders
Main.Orders - Recepción de pedidos de los usuarios
get
/api/v1/orders
Header
Campo
	Tipo
	Descripción
	Authorization
opcional
	string
	Encabezado de autorización en formato Bearer {authToken}.
	                                                * Recibir los pedidos de los/las usuarios/as
{
    "Authorization": "Bearer jknnFApafP4awfAIFfafam2fma"
}
                                                * Respuesta: Todos los pedidos del/de la usuario/a recibidos con éxito
HTTP/1.1 200 OK
[
    {
           "id": 6,
           "userId": 1,
           "productsList": [
               {
                   "id": 1,
                   "quantity": 2
               },
               {
                   "id": 5,
                   "quantity": 2
               },
               {
                   "id": 3,
                   "quantity": 1
               }
           ],
           "deliveryPrice": 0,
           "deliveryPriceOur": 30,
           "deliveryTime": "25~30",
           "wareHouse": "Fresh food",
           "courierService": "Fast Delivery",
           "status": 1
       }
    ]
                                                * Error: El authToken no ha sido transmitido
HTTP/1.1 401 Unauthorized.
{
       "code": 401,
       "message": "    ",
   }
Utils
Utils - Logs de mensajeros/almacenes del servidor
Se trata de una herramienta para obtener las últimas líneas del log mixto de todos los servidores secundarios (mensajeros y almacenes). The count parameter means the number of lines to be read and returned in the response
get
/api/logs/secondary
Parámetro
Campo
	Tipo
	Descripción
	count
opcional
	number
	Número de líneas desde el final
Valor por defecto: 50
	                                                * Obtener los últimos 50 registros
                                                * Obtener los últimos 100 registros
/api/logs/secondary
                                                * Respuesta: Últimos registros del log
2020-08-26T16:07:33.017Z [INFO] [Warehouse][food-city]: Server is listening at port 4022
2020-08-26T16:08:01.324Z [DEBUG] [Warehouse][everything-you-need]: [Request] - ::ffff:127.0.0.1 POST:/everything-you-need/v1/calculate - HTTP/1.1 - application/json - {"deliveryTime":10,"products":[{"id":1,"quantity":1},{"id":4,"quantity":1},{"id":44,"quantity":1}]}
2020-08-26T16:08:01.324Z [DEBUG] [Warehouse][fresh-food]: [Request] - ::ffff:127.0.0.1 POST:/fresh-food/v2.0.1/ct - HTTP/1.1 - application/json - {"deliveryTime":10,"products":[{"id":1,"quantity":1},{"id":4,"quantity":1},{"id":44,"quantity":1}]}
2020-08-26T16:08:01.324Z [DEBUG] [Warehouse][big-world]: [SOAP Client] received <?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  xmlns:tns="WebServices.WarehouseWsdl"><soap:Body><tns:checkSupply><tns:deliveryTime>10</tns:deliveryTime><tns:products><tns:products><id>1</id><quantity>1</quantity></tns:products><tns:products><id>4</id><quantity>1</quantity></tns:products><tns:products><id>44</id><quantity>1</quantity></tns:products></tns:products></tns:checkSupply></soap:Body></soap:Envelope>
2020-08-26T16:08:01.361Z [DEBUG] [Warehouse][food-city]: [Request] - ::ffff:127.0.0.1 POST:/food-city/calculate.xml - HTTP/1.1 - application/xml - <InputModel><deliveryTime>10</deliveryTime><product id="1" quantity="1"/><product id="4" quantity="1"/><product id="44" quantity="1"/></InputModel>
2020-08-26T16:39:17.168Z [DEBUG] [Warehouse][big-world]: [SOAP Client] received <?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  xmlns:tns="WebServices.WarehouseWsdl"><soap:Body><tns:checkSupply><tns:deliveryTime>10</tns:deliveryTime><tns:products><tns:products><id>1</id><quantity>1</quantity></tns:products><tns:products><id>4</id><quantity>1</quantity></tns:products><tns:products><id>44</id><quantity>1</quantity></tns:products></tns:products></tns:checkSupply></soap:Body></soap:Envelope>
2020-08-26T16:39:17.168Z [DEBUG] [Warehouse][fresh-food]: [Request] - ::ffff:127.0.0.1 POST:/fresh-food/v2.0.1/ct - HTTP/1.1 - application/json - {"deliveryTime":10,"products":[{"id":1,"quantity":1},{"id":4,"quantity":1},{"id":44,"quantity":1}]}
2020-08-26T16:39:17.170Z [DEBUG] [Warehouse][everything-you-need]: [Request] - ::ffff:127.0.0.1 POST:/everything-you-need/v1/calculate - HTTP/1.1 - application/json - {"deliveryTime":10,"products":[{"id":1,"quantity":1},{"id":4,"quantity":1},{"id":44,"quantity":1}]}
2020-08-26T16:39:17.173Z [DEBUG] [Warehouse][food-city]: [Request] - ::ffff:127.0.0.1 POST:/food-city/calculate.xml - HTTP/1.1 - application/xml - <InputModel><deliveryTime>10</deliveryTime><product id="1" quantity="1"/><product id="4" quantity="1"/><product id="44" quantity="1"/></InputModel>
2020-08-26T16:39:21.398Z [DEBUG] [Courier][food-service]: [SOAP Client] received <?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  xmlns:tns="WebServices.CourierWsdl"><soap:Body><Request xmlns="WebServices.CourierWsdl"><productsCount>3</productsCount><productsWeight>1.433</productsWeight><deliveryTime>7</deliveryTime></Request></soap:Body></soap:Envelope>
2020-08-26T16:39:21.453Z [DEBUG] [Courier][fast-delivery]: [Request] - ::ffff:127.0.0.1 POST:/fast-delivery/v3.1.1/calculate-delivery.xml - HTTP/1.1 - application/xml - {"InputModel":{"deliveryTime":["7"],"productsWeight":["1.433"],"productsCount":["3"]}}
2020-08-26T16:39:21.481Z [DEBUG] [Courier][order-and-go]: [Request] - ::ffff:127.0.0.1 POST:/order-and-go/v1/delivery - HTTP/1.1 - application/json - {"productsCount":3,"productsWeight":1.433,"deliveryTime":7}
2020-08-26T16:39:21.489Z [DEBUG] [Courier][speedy]: [Request] - ::ffff:127.0.0.1 POST:/speedy/v1/calculate - HTTP/1.1 - application/json - {"productsCount":3,"productsWeight":1.433,"deliveryTime":7}
Utils - Logs del servidor principal
Esta es una herramienta para obtener las últimas líneas en el registro del servidor principal. El parámetro count indica el número de líneas que se leerán y se devolverán a Response
get
/api/logs/main
Parámetro
Campo
	Tipo
	Descripción
	count
opcional
	number
	Número de líneas desde el final
Valor por defecto: 50
	                                                * Obtener los últimos 50 registros
                                                * Obtener los últimos 100 registros
/api/logs/main
                                                * Respuesta: Últimos registros del log
2020-08-26T16:38:31.489Z [INFO] [Main]: Server is listening at port 4000
2020-08-26T16:38:31.500Z [INFO] [Main]: [SOAP Client] Soap is listening at /api/wsdl
2020-08-26T16:38:31.532Z [DEBUG] [Main]: [SOAP Client] TRAIN client is initialized
2020-08-26T16:38:31.564Z [DEBUG] [Main]: [SOAP Client] WORLD client is initialized
2020-08-26T16:38:31.609Z [INFO] [Main]: [PostgreSQL] PostgreSQL is initialized
2020-08-26T16:38:35.057Z [DEBUG] [Main]: [Request] - ::1 GET:/api/logs/main - HTTP/1.1 -  -
2020-08-26T16:39:17.106Z [DEBUG] [Main]: [Request] - ::1 POST:/api/v1/warehouses/amount?dataType=xml - HTTP/1.1 - application/xml - <root><id>1</id><id>4</id><id>44</id></root>
2020-08-26T16:39:21.358Z [DEBUG] [Main]: [Request] - ::1 POST:/api/v1/couriers/check - HTTP/1.1 - application/json - {"ids":[1,4,44],"deliveryTime":7}
2020-08-26T16:39:36.767Z [DEBUG] [Main]: [Request] - ::1 GET:/api/v1/orders - HTTP/1.1 - application/json - {"productsList":"1,4"}
2020-08-26T16:39:47.908Z [DEBUG] [Main]: [Request] - ::1 GET:/api/logs/main - HTTP/1.1 -  -
2020-08-26T16:07:32.123Z [ERROR] [Main]: Unexpected error:
2020-08-26T16:07:32.127Z [ERROR] [Main]:          {"message":"request to http://localhost:4022/food-city/calculate.xml failed, reason: connect ECONNREFUSED 127.0.0.1:4022","type":"system","errno":"ECONNREFUSED","code":"ECONNREFUSED","stack":"FetchError: request to http://localhost:4022/food-city/calculate.xml failed, reason: connect ECONNREFUSED 127.0.0.1:4022\n    at ClientRequest.<anonymous> (/Users/vladimirlevin/Desktop/Own/ez-lavka/packages/main/node_modules/node-fetch/lib/index.js:1455:11)\n    at ClientRequest.emit (events.js:198:13)\n    at ClientRequest.EventEmitter.emit (domain.js:448:20)\n    at Socket.socketErrorListener (_http_client.js:401:9)\n    at Socket.emit (events.js:198:13)\n    at Socket.EventEmitter.emit (domain.js:448:20)\n    at emitErrorNT (internal/streams/destroy.js:91:8)\n    at emitErrorAndCloseNT (internal/streams/destroy.js:59:3)\n    at process._tickCallback (internal/process/next_tick.js:63:19)"}
2020-08-26T16:07:32.131Z [ERROR] [Main]: Unexpected error:
2020-08-26T16:07:32.162Z [ERROR] [Main]:          {"stack":"RangeError [ERR_HTTP_INVALID_STATUS_CODE]: Invalid status code: ECONNREFUSED\n    at ServerResponse.writeHead (_http_server.js:211:11)\n    at ServerResponse._implicitHeader (_http_server.js:202:8)\n    at write_ (_http_outgoing.js:585:9)\n    at ServerResponse.end (_http_outgoing.js:702:5)\n    at ServerResponse.send (/Users/vladimirlevin/Desktop/Own/ez-lavka/packages/main/node_modules/express/lib/response.js:221:10)\n    at ServerResponse.json (/Users/vladimirlevin/Desktop/Own/ez-lavka/packages/main/node_modules/express/lib/response.js:267:15)\n    at app.use (/Users/vladimirlevin/Desktop/Own/ez-lavka/packages/main/src/app.ts:77:14)\n    at Layer.handle_error (/Users/vladimirlevin/Desktop/Own/ez-lavka/packages/main/node_modules/express/lib/router/layer.js:71:5)\n    at trim_prefix (/Users/vladimirlevin/Desktop/Own/ez-lavka/packages/main/node_modules/express/lib/router/index.js:315:13)\n    at /Users/vladimirlevin/Desktop/Own/ez-lavka/packages/main/node_modules/express/lib/router/index.js:284:7\n    at Function.process_params (/Users/vladimirlevin/Desktop/Own/ez-lavka/packages/main/node_modules/express/lib/router/index.js:335:12)\n    at next (/Users/vladimirlevin/Desktop/Own/ez-lavka/packages/main/node_modules/express/lib/router/index.js:275:10)\n    at ServiceContext.next (/Users/vladimirlevin/Desktop/Own/ez-lavka/packages/main/node_modules/express/lib/router/route.js:127:14)\n    at ServiceInvoker.<anonymous> (/Users/vladimirlevin/Desktop/Own/ez-lavka/packages/main/node_modules/typescript-rest/src/server/service-invoker.ts:37:21)\n    at Generator.throw (<anonymous>)\n    at rejected (/Users/vladimirlevin/Desktop/Own/ez-lavka/packages/main/node_modules/typescript-rest/dist/server/service-invoker.js:6:65)\n    at process._tickCallback (internal/process/next_tick.js:68:7)","message":"Invalid status code: ECONNREFUSED"}
2020-08-26T16:08:01.311Z [DEBUG] [Main]: [Request] - ::1 POST:/api/v1/warehouses/amount - HTTP/1.1 - application/json - {"ids":[1,4,44]}
Utils - Recuperar información de la tabla de base de datos
get
/api/db/resources/{table_name}.csv
Parámetro
Campo
	Tipo
	Descripción
	table_name
	string
	El nombre de la tabla en la base de datos. Se pasa en la URL.
	                                                * Recibir la tabla product_model
                                                * Recibir la tabla kit_model
/api/db/resources/product_model.csv
                                                * Respuesta: Archivo con el contenido de la tabla product_model
i
Filter...
x
                                                * Warehouses
                                                * Almacén: "Big World"
                                                * Almacén: "Everything You Need"
                                                * Almacén: "Food City"
                                                * Comprobar la cantidad de productos en stock
                                                * Comprobar la disponibilidad de productos en los almacenes
                                                * Obtener la lista de almacenes
                                                * Wharehouse: "Fresh Food"
                                                * [SOAP] Comprobar la cantidad de productos en stock
                                                * Couriers
                                                * Comprobar los costes de envío
                                                * Entrega: "Fast Delivery"
                                                * Entrega: "Food Service"
                                                * Entrega: "Order and Go"
                                                * Entrega: "Speedy"
                                                * Obtener la lista de entregas
                                                * Main.User
                                                * Creación de cuenta
                                                * Main.Products
                                                * Búsqueda de kit por producto
                                                * Cambio del precio del producto
                                                * Main.Kits
                                                * Añadir productos a la kit:
                                                * Cambio de la kit
                                                * Crear un kit
                                                * Eliminación del kit
                                                * Recibir todas las kit
                                                * Recibir una kit por el nombre
                                                * Main.Basket
                                                * Añadir productos a la cesta
                                                * Crear una cesta
                                                * Eliminar la cesta
                                                * Hacer el pedido
                                                * Recibir los productos de la cesta
                                                * Main.Orders
                                                * Recepción de pedidos de los usuarios
                                                * Utils
                                                * Logs de mensajeros/almacenes del servidor
                                                * Logs del servidor principal
                                                * Recuperar información de la tabla de base de datos
API Urban Grocers
Warehouses
Warehouses - Almacén: "Big World"
La interacción se realiza a través de SOAP
post
/big-world/wsdl
Parámetro
Campo
	Tipo
	Descripción
	deliveryTime
	number
	Plazo de entrega previsto
	products
	Array
	Lista de productos
	  id
	number
	Identificador del producto de la tabla product_model
	  quantity
	number
	Cantidad de producto
	                                                * Ejemplo de solicitud
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  xmlns:tns="WebServices.WarehouseWsdl">
    <soap:Body>
        <tns:checkSupply>
            <tns:products>
                <tns:products>
                    <id>1</id>
                    <quantity>1</quantity>
                </tns:products>
                <tns:products>
                    <id>4</id>
                    <quantity>1</quantity>
                </tns:products>
                <tns:products>
                    <id>44</id>
                    <quantity>1</quantity>
                </tns:products>
            </tns:products>
            <tns:deliveryTime>10</tns:deliveryTime>
        </tns:checkSupply>
    </soap:Body>
</soap:Envelope>
                                                * Respuesta: Ejemplo de respuesta
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"  xmlns:tns="WebServices.WarehouseWsdl">
    <soap:Body>
        <tns:checkSupplyResponse>
            <tns:name>Big World</tns:name>
            <tns:workingHours>
                <start>5</start>
                <end>20</end>
            </tns:workingHours>
            <tns:price>9.5</tns:price>
            <tns:isWarehouseWorking>true</tns:isWarehouseWorking>
            <tns:isItemsAvailable>false</tns:isItemsAvailable>
            <tns:percentOfAvailableItems>33</tns:percentOfAvailableItems>
            <tns:availableProducts>
                <tns:availableProducts>
                    <id>1</id>
                    <quantity>1</quantity>
                </tns:availableProducts>
            </tns:availableProducts>
        </tns:checkSupplyResponse>
    </soap:Body>
</soap:Envelope>
Warehouses - Almacén: "Everything You Need"
post
/everything-you-need/v1/calculate
                                                * Ejemplos de encabezados
{
    "Content-Type": "application/json"
}
Parámetro
Campo
	Tipo
	Descripción
	deliveryTime
	number
	Plazo de entrega previsto
	products
	Array
	Lista de productos
	  id
	number
	Identificador del producto de la tabla product_model
	  quantity
	number
	Cantidad de producto
	                                                * Ejemplo de solicitud
{
    "deliveryTime": 9,
    "products": [
        {
            "id": 1,
            "quantity": 1
        },
        {
            "id": 4,
            "quantity": 3
        }
    ]
}
                                                * Respuesta: Ejemplo de respuesta
HTTP/1.1 200 OK
{
       "name": "Everything You Need",
       "workingHours": { "start": 8, "end": 23 },
       "price": 10,
       "availableProducts": [
           { "id": 1, "quantity": 2 }
       ],
       "isWarehouseWorking": true,
       "isItemsAvailable": true,
       "percentOfAvailableItems": 80
   }
Warehouses - Almacén: "Food City"
Interacción a través de XML
post
/food-city/calculate.xml
                                                * Ejemplos de encabezados
{
    "Content-Type": "application/xml"
}
Parámetro
Campo
	Tipo
	Descripción
	deliveryTime
	number
	Plazo de entrega previsto
	products
	Array
	Lista de productos
	  id
	number
	Identificador del producto de la tabla product_model
	  quantity
	number
	Cantidad de producto
	                                                * Ejemplo de solicitud
<?xml version="1.0" encoding="UTF-8"?>
<InputModel>
    <deliveryTime>9</deliveryTime>
    <product id="5" quantity="2" />
    <product id="4" quantity="1" />
</InputModel>
                                                * Respuesta: Ejemplo de respuesta
<response name="Food City" price="8" isWarehouseWorking="true" isItemsAvailable="true" percentOfAvailableItems="100">
    <working_hours>
       <start>8</start>
       <end>21</end>
    </working_hours>
    <available_products>
       <product id="5" quantity="6"/>
       <product id="4" quantity="12"/>
    </available_products>
</response>
Warehouses - Comprobar la cantidad de productos en stock
La versión SOAP de este punto final se llama - [SOAP] Comprobar la cantidad de productos en stock
post
/api/v1/warehouses/amount
                                                * [JSON] Ejemplos de encabezados
                                                * [XML] Ejemplos de encabezados
{
    "Content-Type": "application/json"
}
Parámetro
Campo
	Tipo
	Descripción
	ids
	number[]
	Una matriz de identificadores de productos (después de id en la tabla product_model).
	dataType
opcional
	string
	Formato de los datos de entrada. Puede tomar valores:
                                                * "json" - El cuerpo de la solicitud se espera en formato JSON
                                                * "xml" - El cuerpo de la solicitud se espera en formato XML
Valor por defecto: json
	                                                * [JSON] Comprobar la cantidad de productos
                                                * [XML] Comprobar la cantidad de productos
{
    "ids": [
        1,
        4,
        44
    ]
}
                                                * Respuesta: En qué almacén, qué hay disponible y cuánto
HTTP/1.1 200 OK
{
       "Everything You Need": {
           "Refresco Sprite": 9,
           "Gourmet Palomitas Kernels": 6
       },
       "Food City": {
           "Orange Juice - Cold-Pressed, No Added Sugar, Preservative Free": 3,
           "Refresco Sprite": 12
       },
       "Big World": {
           "Orange Juice - Cold-Pressed, No Added Sugar, Preservative Free": 1
       },
       "Fresh food": {
           "Orange Juice - Cold-Pressed, No Added Sugar, Preservative Free": 3,
           "Refresco Sprite": 12
       }
   }
Warehouses - Comprobar la disponibilidad de productos en los almacenes
post
/api/v1/warehouses/check
                                                * Ejemplos de encabezados
{
    "Content-Type": "application/json"
}
Parámetro
Campo
	Tipo
	Descripción
	products
	number[]
	Una matriz de identificadores de productos and their quantities (Campos id en la tabla product_model).
	                                                * Comprobar la disponibilidad de productos
{
    "products": [
        {
            "id": 5,
            "quantity": 1
        },
        {
            "id": 4,
            "quantity": 5
        }
    ]
}
                                                * Respuesta: En qué almacén, qué hay disponible y cuánto
HTTP/1.1 200 OK
{
       "Everything You Need": {
           "Refresco Sprite": true,
           "Gourmet Palomitas Kernels": true,
           "Orange Juice - Cold-Pressed, No Added Sugar, Preservative Free": false
       },
       "Food City": {
           "Orange Juice - Cold-Pressed, No Added Sugar, Preservative Free": true,
           "Refresco Sprite": true,
           "Gourmet Palomitas Kernels": false
       },
       "Big World": {
           "Orange Juice - Cold-Pressed, No Added Sugar, Preservative Free": true,
           "Refresco Sprite": false,
           "Gourmet Palomitas Kernels": false
       },
       "Fresh food": {
           "Orange Juice - Cold-Pressed, No Added Sugar, Preservative Free": true,
           "Refresco Sprite": true,
           "Gourmet Palomitas Kernels": false
       }
   }
Warehouses - Obtener la lista de almacenes
get
/api/v1/warehouses
                                                * Respuesta: Obtener la lista de almacenes con éxito
HTTP/1.1 200 OK
[
    {
           "name": "Everything You Need",
           "workingHours": {
               "start": 7,
               "end": 23
           }
       },
    {
           "name": "Fresh food",
           "workingHours": {
               "start": 8,
               "end": 23
           }
       },
    {
           "name": "Food City",
           "workingHours": {
               "start": 8,
               "end": 21
           }
       },
    {
           "name": "Big World",
           "workingHours": {
               "start": 5,
               "end": 20
           }
       }
    ]
Warehouses - Wharehouse: "Fresh Food"
post
/fresh-food/v2.0.1/ct
                                                * Ejemplos de encabezados
{
    "Content-Type": "application/json"
}
Parámetro
Campo
	Tipo
	Descripción
	deliveryTime
	number
	Plazo de entrega previsto
	products
	Array
	Lista de productos
	  id
	number
	Identificador del producto de la tabla product_model
	  quantity
	number
	Cantidad de producto
	                                                * Ejemplo de solicitud
{
    "deliveryTime": 9,
    "products": [
        {
            "id": 1,
            "quantity": 1
        },
        {
            "id": 4,
            "quantity": 3
        }
    ]
}
                                                * Respuesta: Ejemplo de respuesta
HTTP/1.1 200 OK
{
       "name": "Fresh food",
       "workingHours": { "start": 8, "end": 23 },
       "price": 10,
       "availableProducts": [
           { "id": 1, "quantity": 2 }
       ],
       "isWarehouseWorking": true,
       "isItemsAvailable": true,
       "percentOfAvailableItems": 80
   }
Warehouses - [SOAP] Comprobar la cantidad de productos en stock
post
/api/wsdl
Parámetro
Campo
	Tipo
	Descripción
	ids
	number[]
	Una matriz de identificadores de productos (después de id en la tabla product_model).
	                                                * [XML] Comprobar la cantidad de productos
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  xmlns:tns="WebServices.MainWsdl">
    <soap:Body>
        <Request xmlns="WebServices.MainWsdl">
            <ids>1</ids>
            <ids>4</ids>
            <ids>44</ids>
        </Request>
    </soap:Body>
</soap:Envelope>
                                                * Respuesta: En qué almacén, qué hay disponible y cuánto
   HTTP/1.1 200 OK
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"  xmlns:tns="WebServices.MainWsdl">
    <soap:Body>
        <Response>
            <name>Everything You Need</name>
            <products>
                <name>Refresco Sprite</name>
                <quantity>9</quantity>
            </products>
            <products>
                <name>Gourmet Palomitas Kernels</name>
                <quantity>6</quantity>
            </products>
        </Response>
        <Response>
            <name>Food City</name>
            <products>
                <name>Orange Juice - Cold-Pressed, No Added Sugar, Preservative Free</name>
                <quantity>3</quantity>
            </products>
            <products>
                <name>Refresco Sprite</name>
                <quantity>12</quantity>
            </products>
        </Response>
        <Response>
            <name>Big World</name>
            <products>
                <name>Orange Juice - Cold-Pressed, No Added Sugar, Preservative Free</name>
                <quantity>1</quantity>
            </products>
        </Response>
        <Response>
            <name>Fresh food</name>
            <products>
                <name>Orange Juice - Cold-Pressed, No Added Sugar, Preservative Free</name>
                <quantity>3</quantity>
            </products>
            <products>
                <name>Refresco Sprite</name>
                <quantity>12</quantity>
            </products>
        </Response>
    </soap:Body>
</soap:Envelope>
Couriers
Couriers - Comprobar los costes de envío
post
/api/v1/couriers/check
                                                * Ejemplos de encabezados
{
    "Content-Type": "application/json"
}
Parámetro
Campo
	Tipo
	Descripción
	products
	number[]
	Una matriz de identificadores de productos and their quantities (después de id en la tabla product_model).
	deliveryTime
	number
	Plazo de entrega previsto (from 0 to 23)
	                                                * Comprobar los costes de los diferentes servicios
{
    "products": [
        {
            "id": 1,
            "quantity": 3
        },
        {
            "id": 4,
            "quantity": 1
        },
        {
            "id": 9,
            "quantity": 3
        }
    ],
    "deliveryTime": 7
}
                                                * Respuesta: Cuánto costaría cada uno de los servicios
HTTP/1.1 200 OK
{
       "Fast Delivery": {
           "deliveryPrice": 0
       },
       "Speedy": {
           "deliveryPrice": 99
       },
       "Food Service": {
           "deliveryPrice": 0
       },
       "Order and Go": {
           "deliveryPrice": 99
       }
   }
Couriers - Entrega: "Fast Delivery"
La interacción se realiza mediante XML
post
/fast-delivery/v3.1.1/calculate-delivery.xml
                                                * Ejemplos de encabezados
{
    "Content-Type": "application/xml"
}
Parámetro
Campo
	Tipo
	Descripción
	productsCount
	number
	Número de productos en el pedido
	productsWeight
	number
	Peso de los productos
	deliveryTime
	number
	Plazo de entrega previsto
	                                                * Ejemplo de solicitud
<InputModel>
    <productsCount>2</productsCount>
    <productsWeight>5.115</productsWeight>
    <deliveryTime>20</deliveryTime>
</InputModel>
                                                * Respuesta: Ejemplo de respuesta
HTTP/1.1 200 OK
<response name="Fast Delivery" isItPossibleToDeliver="true" hostDeliveryCost="43" clientDeliveryCost="0">
    <toBeDeliveredTime>
        <min>25</min>
        <max>30</max>
    </toBeDeliveredTime>
</response>
Couriers - Entrega: "Food Service"
Interacción a través de SOAP
post
/food-service/wsdl
Parámetro
Campo
	Tipo
	Descripción
	productsCount
	number
	Número de productos en el pedido
	productsWeight
	number
	Peso de los productos
	deliveryTime
	number
	Plazo de entrega previsto
	                                                * Ejemplo de solicitud
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  xmlns:tns="WebServices.CourierWsdl">
    <soap:Body>
        <Request xmlns="WebServices.CourierWsdl">
            <productsCount>3</productsCount>
            <productsWeight>1.433</productsWeight>
            <deliveryTime>7</deliveryTime>
        </Request>
    </soap:Body>
</soap:Envelope>
                                                * Respuesta: Ejemplo de respuesta
HTTP/1.1 200 OK
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"  xmlns:tns="WebServices.CourierWsdl">
    <soap:Body>
        <Response xmlns="WebServices.CourierWsdl">
        <name>Food Service</name>
        <isItPossibleToDeliver>true</isItPossibleToDeliver>
        <hostDeliveryCost>29</hostDeliveryCost>
        <toBeDeliveredTime>
            <min>25</min>
            <max>30</max>
        </toBeDeliveredTime>
        <clientDeliveryCost>0</clientDeliveryCost>
        </Response>
    </soap:Body>
</soap:Envelope>
Couriers - Entrega: "Order and Go"
post
/order-and-go/v1/delivery
                                                * Ejemplos de encabezados
{
    "Content-Type": "application/json"
}
Parámetro
Campo
	Tipo
	Descripción
	productsCount
	number
	Número de productos en el pedido
	productsWeight
	number
	Peso de los productos
	deliveryTime
	number
	Plazo de entrega previsto
	                                                * Ejemplo de solicitud
{
    "deliveryTime": 9,
    "productsCount": 10,
    "productsWeight": 11
}
                                                * Respuesta: Ejemplo de respuesta
HTTP/1.1 200 OK
   {
       "name": "Order and Go",
       "clientDeliveryCost": 10,
       "toBeDeliveredTime": { "min": 10, "max": 20 },
       "hostDeliveryCost": 23,
       "isItPossibleToDeliver": true
   }
Couriers - Entrega: "Speedy"
post
/speedy/v1/calculate
                                                * Ejemplos de encabezados
{
    "Content-Type": "application/json"
}
Parámetro
Campo
	Tipo
	Descripción
	productsCount
	number
	Número de productos en el pedido
	productsWeight
	number
	Peso de los productos
	deliveryTime
	number
	Plazo de entrega previsto
	                                                * Ejemplo de solicitud
{
    "deliveryTime": 9,
    "productsCount": 10,
    "productsWeight": 11
}
                                                * Respuesta: Ejemplo de respuesta
HTTP/1.1 200 OK
   {
       "name": "Speedy",
       "clientDeliveryCost": 10,
       "toBeDeliveredTime": { "min": 10, "max": 20 },
       "hostDeliveryCost": 23,
       "isItPossibleToDeliver": true
   }
Couriers - Obtener la lista de entregas
get
/api/v1/couriers
                                                * Respuesta: Recibir las entregas con éxito
   HTTP/1.1 200 OK
    [
           {
               "name": "Order and Go",
               "workingHours": {
                   "start": 8,
                   "end": 22
               }
           },
           {
               "name": "Speedy",
               "workingHours": {
                   "start": 8,
                   "end": 22
               }
           },
           {
               "name": "Fast Delivery",
               "workingHours": {
                   "start": 7,
                   "end": 21
               }
           },
           {
               "name": "Food Service",
               "workingHours": {
                   "start": 6,
                   "end": 20
               }
           }
]
Main.User
Main.User - Creación de cuenta
post
/api/v1/users
                                                * Ejemplos de encabezados
{
    "Content-Type": "application/json"
}
Parámetro
Campo
	Tipo
	Descripción
	firstName
	string
	Nombre de usuario/a, escrito en el campo firstName de la tabla Users
	phone
	string
	El número de teléfono del/de la usuario/a se escribe en el campo phone de la tabla Users
	address
	string
	La dirección del/de la usuario/a se escribe en el campo address de la tabla Users
	email
opcional
	string
	Dirección de correo electrónico, escrita en el campo email de la tabla Users
	comment
opcional
	string
	Comentario de usuario/a, escrito en el campo comment de la tabla Users
	                                                * Conjunto mínimo de datos
                                                * Información completa sobre el/la usuario/a
{
    "firstName": "Max",
    "phone": "+10005553535",
    "address": "8042 Lancaster Ave.Hamburg, NY"
}
                                                * La cuenta de usuario se ha creado correctamente
HTTP/1.1 201 Creado
{
    authToken: 'jknnFApafP4awfAIFfafam2fma'
}
                                                * Error en los datos de entrada #1
                                                * Error en los datos de entrada #2
                                                * Error en los datos de entrada #3
                                                * Error en los datos de entrada #4
HTTP/1.1 400 Bad request.
{
    "code": 400,
    "message": "No se han aprobado todos los parámetros requeridos. Parámetros requeridos: nombre, teléfono, dirección"
}
Main.Products
Main.Products - Búsqueda de kit por producto
endpoint para buscar kit que contengan los productos especificados
post
/api/v1/products/kits
                                                * Ejemplos de encabezados
{
    "Content-Type": "application/json"
}
Parámetro
Campo
	Tipo
	Descripción
	ids
	number[]
	Una matriz de identificadores de productos from the table product_model.
	                                                * Buscar kit que contengan el producto 1 o 2 o 3:
{
    "ids": [
        1,
        2,
        3
    ]
}
                                                * Respuesta: Recibir las kit con éxito
HTTP/1.1 200 OK
[
    {
           "id": 1,
           "name": "Para pícnics",
           "productsList": [
               {
                   "id": 1,
                   "quantity": 1
               },
               {
                   "id": 2,
                   "quantity": 1
               },
               {
                   "id": 3,
                   "quantity": 1
               },
               {
                   "id": 4,
                   "quantity": 1
               },
               {
                   "id": 5,
                   "quantity": 1
               },
               {
                   "id": 6,
                   "quantity": 1
               },
               {
                   "id": 7,
                   "quantity": 1
               },
               {
                   "id": 8,
                   "quantity": 1
               },
               {
                   "id": 9,
                   "quantity": 1
               },
               {
                   "id": 10,
                   "quantity": 1
               },
               {
                   "id": 11,
                   "quantity": 1
               },
               {
                   "id": 12,
                   "quantity": 1
               },
               {
                   "id": 13,
                   "quantity": 1
               },
               {
                   "id": 14,
                   "quantity": 1
               },
               {
                   "id": 15,
                   "quantity": 1
               },
               {
                   "id": 16,
                   "quantity": 1
               },
               {
                   "id": 17,
                   "quantity": 1
               },
               {
                   "id": 18,
                   "quantity": 1
               },
               {
                   "id": 19,
                   "quantity": 1
               },
               {
                   "id": 20,
                   "quantity": 1
               },
               {
                   "id": 21,
                   "quantity": 1
               },
               {
                   "id": 22,
                   "quantity": 1
               },
               {
                   "id": 23,
                   "quantity": 1
               },
               {
                   "id": 24,
                   "quantity": 1
               },
               {
                   "id": 25,
                   "quantity": 1
               },
               {
                   "id": 26,
                   "quantity": 1
               },
               {
                   "id": 27,
                   "quantity": 1
               },
               {
                   "id": 28,
                   "quantity": 1
               },
               {
                   "id": 29,
                   "quantity": 1
               },
               {
                   "id": 30,
                   "quantity": 1
               },
               {
                   "id": 31,
                   "quantity": 1
               },
               {
                   "id": 32,
                   "quantity": 1
               },
               {
                   "id": 33,
                   "quantity": 1
               },
               {
                   "id": 34,
                   "quantity": 1
               },
               {
                   "id": 35,
                   "quantity": 1
               },
               {
                   "id": 36,
                   "quantity": 1
               },
               {
                   "id": 37,
                   "quantity": 1
               },
               {
                   "id": 38,
                   "quantity": 1
               },
               {
                   "id": 39,
                   "quantity": 1
               }
           ],
           "productsCount": 39
       },
    {
           "id": 2,
           "name": "Para películas y series",
           "productsList": [
               {
                   "id": 7,
                   "quantity": 1
               },
               {
                   "id": 8,
                   "quantity": 1
               },
               {
                   "id": 9,
                   "quantity": 1
               },
               {
                   "id": 40,
                   "quantity": 1
               },
               {
                   "id": 41,
                   "quantity": 1
               },
               {
                   "id": 42,
                   "quantity": 1
               },
               {
                   "id": 43,
                   "quantity": 1
               },
               {
                   "id": 44,
                   "quantity": 1
               },
               {
                   "id": 45,
                   "quantity": 1
               },
               {
                   "id": 46,
                   "quantity": 1
               },
               {
                   "id": 47,
                   "quantity": 1
               },
               {
                   "id": 2,
                   "quantity": 1
               },
               {
                   "id": 3,
                   "quantity": 1
               },
               {
                   "id": 4,
                   "quantity": 1
               },
               {
                   "id": 48,
                   "quantity": 1
               },
               {
                   "id": 49,
                   "quantity": 1
               },
               {
                   "id": 50,
                   "quantity": 1
               },
               {
                   "id": 51,
                   "quantity": 1
               },
               {
                   "id": 52,
                   "quantity": 1
               },
               {
                   "id": 53,
                   "quantity": 1
               },
               {
                   "id": 54,
                   "quantity": 1
               },
               {
                   "id": 55,
                   "quantity": 1
               },
               {
                   "id": 56,
                   "quantity": 1
               },
               {
                   "id": 57,
                   "quantity": 1
               },
               {
                   "id": 58,
                   "quantity": 1
               },
               {
                   "id": 59,
                   "quantity": 1
               },
               {
                   "id": 60,
                   "quantity": 1
               }
           ],
           "productsCount": 27
       }
    ]
Main.Products - Cambio del precio del producto
put
/api/v1/products/:id
                                                * Ejemplos de encabezados
{
    "Content-Type": "application/json"
}
Parámetro
Campo
	Tipo
	Descripción
	id
	number
	El id de la kit en la tabla product_model. Se pasa en la URL
	price
opcional
	string
	price del producto. Se pasa en el texto de la solicitud.
	                                                * Cambio del producto /api/v1/products/7
{
    "price": 175
}
                                                * Respuesta: El kit ha sido eliminado con éxito.
HTTP/1.1 200 OK
{
       "ok": true
   }
                                                * Error: Producto no encontrado
HTTP/1.1 404 Not found.
{
       "code": 404,
       "message": "Not found"
   }
Main.Kits
Main.Kits - Añadir productos a la kit:
post
/api/v1/kits/:id/products
                                                * Ejemplos de encabezados
{
    "Content-Type": "application/json"
}
Parámetro
Campo
	Tipo
	Descripción
	id
	number
	El id de kit en la tabla kit_model. Se pasa en la URL
	productsList
	Array
	Una lista de productos que se agregarán al kit. La lista contiene los ID de los artículos y sus cantidades. Debe enviarse en el cuerpo de la solicitud.
	                                                * Ejemplo de cuerpo de solicitud para agregar artículos al kit
{
    "productsList": [
        {
            "id": 1,
            "quantity": 2
        },
        {
            "id": 6,
            "quantity": 2
        }
    ]
}
                                                * Respuesta: Completar con éxito la kit de productos
    HTTP/1.1 200 OK
 {
    "id": 2,
    "name": "Mi conjunto del fin de semana",
    "productsList": [
        {
            "id": 1,
            "name": "Caviar rojo",
            "price": 45,
            "weight": 5,
            "units": "kg",
            "quantity": 2
        },
        {
            "id": 5,
            "name": "Baguette",
            "price": 15,
            "weight": 1,
            "units": "kg",
            "quantity": 2
        }
    ],
    "productsCount": 4
}
                                                * Error: No se han encontrado kits coincidentes
                                                * Error: El formato del JSON enviado no es correcto
                                                * Error: El valor en alguno de los parametros es incorrecto
HTTP/1.1 404 Not found.
{
       "code": 404,
       "message": "Not found"
   }
Main.Kits - Cambio de la kit
put
/api/v1/kits/:id
                                                * Ejemplos de encabezados
{
    "Content-Type": "application/json"
}
Parámetro
Campo
	Tipo
	Descripción
	id
	number
	El id de kit en la tabla kit_model. Se pasa en la URL
	name
opcional
	string
	name de la kit. Se pasa en el texto de la solicitud.
	productsList
opcional
	Array
	Una lista de productos que se agregarán al kit. La lista contiene los ID de los artículos y sus cantidades. Debe enviarse en el cuerpo de la solicitud.
	                                                * Cambio de la kit /api/v1/kits/7
{
    "name": "Mi kit modificada",
    "productsList": [
        {
            "id": 1,
            "quantity": 4
        },
        {
            "id": 5,
            "quantity": 2
        },
        {
            "id": 3,
            "quantity": 1
        },
        {
            "id": 4,
            "quantity": 1
        }
    ]
}
                                                * Respuesta: El kit ha sido eliminado con éxito.
HTTP/1.1 200 OK
{
       "ok": true
   }
                                                * Error: No se han encontrado kits coincidentes
HTTP/1.1 404 Not found.
{
       "code": 404,
       "message": "Not found"
   }
Main.Kits - Crear un kit
endpoint para crear una kit de una tarjeta específica O de usuario.
                                                * Es obligatorio pasar el encabezado Authorisation O el parámetro cardId, para crear la kit
                                                * Si se recibe una solicitud con un encabezado Authorisation que contenga el authToken de un/a usuario/a en particular - se creará la kit de este/a usuario/a.
                                                * Si se recibe el parámetro cardId, se creará una kit dentro de la tarjeta correspondiente
                                                * Si no se pasa ninguno de los parámetros, se devolverá un error.
                                                * Cuando se pasan ambos parámetros, Authorization es la prioridad
post
/api/v1/kits
Header
Campo
	Tipo
	Descripción
	Authorization
opcional
	string
	Encabezado de autorización en formato Bearer {authToken}. Cuando se pasa - se devuelven todos las cestas creadas por el/la usuario/a.
	Content-Type
opcional
	string
	Valor por defecto: application/json
	                                                * Ejemplos de encabezados
                                                * Recepción de las cestas creadas por el/la usuario/a
{
    "Content-Type": "application/json"
}
Parámetro
Campo
	Tipo
	Descripción
	cardId
opcional
	number
	El id de la tarjeta en la tabla card_model. Cuando se pasa - se creará un conjunto incluido en esta tarjeta
	name
	string
	El nombre de la kit, que será escrito en el campo correspondiente de la tabla kit_model.
	                                                * Respuesta: El conjunto ha sido creado con éxito
HTTP/1.1 201 Creado
{
       "name": "Mi conjunto",
       "card": {
           "id": 1,
           "name": "Para la situación"
       },
       "productsList": null,
       "id": 7,
       "productsCount": 0
   }
                                                * Error: No se ha transmitido ninguno de los parámetros
                                                * Error: Validación del nombre
HTTP/1.1 400 Bad request.
{
       "code": 400,
       "message": "No se han aprobado todos los parámetros requeridos"
   }
Main.Kits - Eliminación del kit
delete
/api/v1/kits/:id
Parámetro
Campo
	Tipo
	Descripción
	id
	number
	El id de kit en la tabla kit_model. Se pasa en la URL
	                                                * Eliminación de un kit con id=7
/api/v1/kits/7
                                                * Respuesta: El kit ha sido eliminado con éxito.
HTTP/1.1 200 OK
{
       "ok": true
   }
Main.Kits - Recibir todas las kit
endpoint para recuperar todas las kit dentro de una tarjeta específica O las kit creadas por el/la usuario/a.
                                                * Es obligatorio pasar el encabezado Authorisation O el parámetro cardId, para recibir las kit
                                                * Si se recibe una solicitud con un encabezado Authorisation que contenga el authToken de un/a usuario/a en particular - se devolverán las kit creadas por ese/a usuario/a.
                                                * Si se recibe el parámetro de consulta cardId, se devolverán las kit relativas a la tarjeta.
                                                * Si no se pasa ninguno de los parámetros, se devolverá un error.
                                                * Cuando se pasan ambos parámetros, Authorization es la prioridad
get
/api/v1/kits
Header
Campo
	Tipo
	Descripción
	Authorization
opcional
	string
	Encabezado de autorización en formato Bearer {authToken}. Cuando se pasa - se devuelven todos las kit creadas por el/la usuario/a.
	                                                * Recepción de las kit creadas por el/la usuario/a
{
    "Authorization": "Bearer jknnFApafP4awfAIFfafam2fma"
}
Parámetro
Campo
	Tipo
	Descripción
	cardId
opcional
	number
	El id de la tarjeta en la tabla card_model. Cuando se pasa - se devuelven todos las kit incluidas en la tarjeta.
	                                                * Recibir las kit dentro de una tarjeta with id = 1
/api/v1/kits?cardId=1
                                                * Respuesta: Recibir las kit con éxito
HTTP/1.1 200 OK
[
    {
           "id": 1,
           "name": "Para pícnics",
           "productsList": [
               {
                   "id": 1,
                   "name": "Orange Juice - Cold-Pressed, No Added Sugar, Preservative Free",
                   "price": 149,
                   "weight": 473,
                   "units": "ml",
                   "quantity": 1
               },
               {
                   "id": 2,
                   "name": "Refresco Mountain Dew",
                   "price": 89,
                   "weight": 1,
                   "units": "l",
                   "quantity": 1
               },
               {
                   "id": 3,
                   "name": "Refresco Pepsi",
                   "price": 109,
                   "weight": 1,
                   "units": "l",
                   "quantity": 1
               },
               {
                   "id": 4,
                   "name": "Refresco Sprite",
                   "price": 79,
                   "weight": 900,
                   "units": "ml",
                   "quantity": 1
               },
               {
                   "id": 5,
                   "name": "Jugo Fruit Power: Lichi",
                   "price": 349,
                   "weight": 900,
                   "units": "ml",
                   "quantity": 1
               },
               {
                   "id": 6,
                   "name": "Baguette",
                   "price": 69,
                   "weight": 160,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 7,
                   "name": "Papas fritas: Saladas Clásicas",
                   "price": 119,
                   "weight": 150,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 8,
                   "name": "Papas fritas: Paprika",
                   "price": 199,
                   "weight": 150,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 9,
                   "name": "Papas Fritas: Chile",
                   "price": 209,
                   "weight": 100,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 10,
                   "name": "Pita",
                   "price": 99,
                   "weight": 300,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 11,
                   "name": "Pan multigrano",
                   "price": 149,
                   "weight": 400,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 12,
                   "name": "Pan de ajo",
                   "price": 75,
                   "weight": 225,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 13,
                   "name": "Mini chapata",
                   "price": 45,
                   "weight": 107,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 14,
                   "name": "Brioche",
                   "price": 79,
                   "weight": 79,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 15,
                   "name": "Salchichas vienesas",
                   "price": 179,
                   "weight": 350,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 16,
                   "name": "Salchichas de pollo",
                   "price": 173,
                   "weight": 200,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 17,
                   "name": "Chorizo",
                   "price": 269,
                   "weight": 420,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 18,
                   "name": "Salchichón",
                   "price": 175,
                   "weight": 464,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 19,
                   "name": "Salami",
                   "price": 99,
                   "weight": 190,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 20,
                   "name": "Bacon",
                   "price": 269,
                   "weight": 500,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 21,
                   "name": "Pastrami",
                   "price": 143,
                   "weight": 200,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 22,
                   "name": "Pepperoni",
                   "price": 329,
                   "weight": 500,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 23,
                   "name": "Anti-Bacterial Hand Sanitizer",
                   "price": 139,
                   "weight": 50,
                   "units": "ml",
                   "quantity": 1
               },
               {
                   "id": 24,
                   "name": "Paper Napkin - Large",
                   "price": 99,
                   "weight": 60,
                   "units": "pzas",
                   "quantity": 1
               },
               {
                   "id": 25,
                   "name": "Anti Bacterial Disinfectant Sanitising Wipes - Alcohol Free",
                   "price": 199,
                   "weight": 48,
                   "units": "pzas",
                   "quantity": 1
               },
               {
                   "id": 26,
                   "name": "SMART Mosquito Repellent",
                   "price": 349,
                   "weight": 100,
                   "units": "ml",
                   "quantity": 1
               },
               {
                   "id": 27,
                   "name": "Manzana verde",
                   "price": 169,
                   "weight": 500,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 28,
                   "name": "Orange",
                   "price": 146,
                   "weight": 500,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 29,
                   "name": "Cherry",
                   "price": 249,
                   "weight": 500,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 30,
                   "name": "Raspberry",
                   "price": 239,
                   "weight": 250,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 31,
                   "name": "Blackberry",
                   "price": 125,
                   "weight": 200,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 32,
                   "name": "Lima",
                   "price": 59,
                   "weight": 1,
                   "units": "pzas",
                   "quantity": 1
               },
               {
                   "id": 33,
                   "name": "Red Grapes",
                   "price": 269,
                   "weight": 500,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 34,
                   "name": "Green Grapes",
                   "price": 179,
                   "weight": 500,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 35,
                   "name": "Banana",
                   "price": 99,
                   "weight": 1000,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 36,
                   "name": "Pear",
                   "price": 199,
                   "weight": 650,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 37,
                   "name": "Blueberry",
                   "price": 199,
                   "weight": 125,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 38,
                   "name": "Pineapple",
                   "price": 385,
                   "weight": 1,
                   "units": "pzas",
                   "quantity": 1
               },
               {
                   "id": 39,
                   "name": "Pear",
                   "price": 145,
                   "weight": 800,
                   "units": "g",
                   "quantity": 1
               }
           ],
           "productsCount": 39
       },
    {
           "id": 2,
           "name": "Para películas y series",
           "productsList": [
               {
                   "id": 2,
                   "name": "Refresco Mountain Dew",
                   "price": 89,
                   "weight": 1,
                   "units": "l",
                   "quantity": 1
               },
               {
                   "id": 3,
                   "name": "Refresco Pepsi",
                   "price": 109,
                   "weight": 1,
                   "units": "l",
                   "quantity": 1
               },
               {
                   "id": 4,
                   "name": "Refresco Sprite",
                   "price": 79,
                   "weight": 900,
                   "units": "ml",
                   "quantity": 1
               },
               {
                   "id": 7,
                   "name": "Papas fritas: Saladas Clásicas",
                   "price": 119,
                   "weight": 150,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 8,
                   "name": "Papas fritas: Paprika",
                   "price": 199,
                   "weight": 150,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 9,
                   "name": "Papas Fritas: Chile",
                   "price": 209,
                   "weight": 100,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 43,
                   "name": "Classic Hummus Dip & Spread",
                   "price": 99,
                   "weight": 150,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 44,
                   "name": "Gourmet Palomitas Kernels",
                   "price": 109,
                   "weight": 60,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 45,
                   "name": "Caramel Palomitas",
                   "price": 99,
                   "weight": 150,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 46,
                   "name": "Fruit Beer Non-Alcoholic",
                   "price": 249,
                   "weight": 250,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 47,
                   "name": "Stella Artois Beer Non-Alcoholic",
                   "price": 179,
                   "weight": 60,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 48,
                   "name": "100% Belgian Dark Chocolate - with Apricot",
                   "price": 89,
                   "weight": 45,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 49,
                   "name": "100% Belgian Dark Chocolate - Raisins",
                   "price": 69,
                   "weight": 450,
                   "units": "ml",
                   "quantity": 1
               },
               {
                   "id": 50,
                   "name": "100% Belgian Milk Chocolate - Sea Salt",
                   "price": 109,
                   "weight": 450,
                   "units": "ml",
                   "quantity": 1
               },
               {
                   "id": 54,
                   "name": "Dairy Rich Chocolate Bar - Fruit & Nut",
                   "price": 139,
                   "weight": 100,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 55,
                   "name": "Peanut Butter Nutty Cookies",
                   "price": 119,
                   "weight": 97,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 56,
                   "name": "Cookies - Orange Splash",
                   "price": 89,
                   "weight": 85,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 57,
                   "name": "Choco Nut Cookies",
                   "price": 159,
                   "weight": 160,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 58,
                   "name": "Milk Cookies",
                   "price": 239,
                   "weight": 100,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 59,
                   "name": "Sandwich Biscuits",
                   "price": 119,
                   "weight": 100,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 60,
                   "name": "Chocobakes Choc Filled Cookies",
                   "price": 139,
                   "weight": 80,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 61,
                   "name": "Baguette French Recipe",
                   "price": 179,
                   "weight": 171,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 62,
                   "name": "Queso Croissant",
                   "price": 119,
                   "weight": 50,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 63,
                   "name": "French Almond Croissant",
                   "price": 119,
                   "weight": 228,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 64,
                   "name": "Chocolate Croissant",
                   "price": 149,
                   "weight": 168,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 65,
                   "name": "Smoked Salmon Croissant",
                   "price": 59,
                   "weight": 100,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 66,
                   "name": "Belgian Chocolate Cake Mix",
                   "price": 219,
                   "weight": 250,
                   "units": "g",
                   "quantity": 1
               }
           ],
           "productsCount": 27
       },
    {
           "id": 3,
           "name": "Sabores de París",
           "productsList": [
               {
                   "id": 54,
                   "name": "Dairy Rich Chocolate Bar - Fruit & Nut",
                   "price": 139,
                   "weight": 100,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 58,
                   "name": "Milk Cookies",
                   "price": 239,
                   "weight": 100,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 67,
                   "name": "Baguette French Recipe",
                   "price": 89,
                   "weight": 200,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 68,
                   "name": "Queso Croissant",
                   "price": 79,
                   "weight": 75,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 69,
                   "name": "French Almond Croissant",
                   "price": 129,
                   "weight": 120,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 70,
                   "name": "Chocolate Croissant",
                   "price": 104,
                   "weight": 96,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 71,
                   "name": "Smoked Salmon Croissant",
                   "price": 119,
                   "weight": 90,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 72,
                   "name": "Belgian Chocolate Cake Mix",
                   "price": 359,
                   "weight": 125,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 73,
                   "name": "Queso para untar: Queso crema",
                   "price": 79,
                   "weight": 130,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 74,
                   "name": "Queso Slices",
                   "price": 239,
                   "weight": 400,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 75,
                   "name": "Queso Spread - Roasted Garlic",
                   "price": 129,
                   "weight": 200,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 76,
                   "name": "Spicy Queso Straw",
                   "price": 229,
                   "weight": 250,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 77,
                   "name": "Rebanadas de queso procesado",
                   "price": 220,
                   "weight": 250,
                   "units": "",
                   "quantity": 1
               },
               {
                   "id": 78,
                   "name": "Cubos de queso procesado",
                   "price": 399,
                   "weight": 200,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 79,
                   "name": "Soyabean Tempeh Cubes",
                   "price": 209,
                   "weight": 300,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 82,
                   "name": "Center Filled Dark Chocolate Cookies",
                   "price": 129,
                   "weight": 100,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 83,
                   "name": "Enrobed Cinnamon Milk Chocolate Dipped Cookies",
                   "price": 225,
                   "weight": 100,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 84,
                   "name": "Oreo & Crème Frozen Dessert",
                   "price": 339,
                   "weight": 300,
                   "units": "ml",
                   "quantity": 1
               },
               {
                   "id": 85,
                   "name": "Chocorich Eclairs Chocolate - Assorted",
                   "price": 429,
                   "weight": 200,
                   "units": "g",
                   "quantity": 1
               }
           ],
           "productsCount": 19
       }
    ]
                                                * Error: No se ha transmitido ninguno de los parámetros
                                                * Error: No se han encontrado kits coincidentes
HTTP/1.1 400 Bad request.
{
       "code": 400,
       "message": "No se han aprobado todos los parámetros requeridos"
   }
Main.Kits - Recibir una kit por el nombre
get
/api/v1/kits/search
Parámetro
Campo
	Tipo
	Descripción
	name
	string
	name de la kit en la tabla kit_model.
	                                                * Recibir una kit con un nombre "Sabores de París"
/api/v1/kits/search?name=Sabores%20de%20París
                                                * Respuesta: El conjunto ha sido recibido con éxito.
HTTP/1.1 200 OK
{
       "id": 3,
       "name": "Sabores de París",
       "productsList": [
           {
               "id": 54,
               "name": "Dairy Rich Chocolate Bar - Fruit & Nut",
               "price": 139,
               "weight": 100,
               "units": "g",
               "quantity": 6
           },
           {
               "id": 58,
               "name": "Milk Cookies",
               "price": 239,
               "weight": 100,
               "units": "g"
               "quantity": 8
           },
           {
               "id": 67,
               "name": "Baguette French Recipe",
               "price": 89,
               "weight": 200,
               "units": "g",
               "quantity": 4
           },
           {
               "id": 68,
               "name": "Queso Croissant",
               "price": 79,
               "weight": 75,
               "units": "g",
               "quantity": 1
           },
           {
               "id": 69,
               "name": "French Almond Croissant",
               "price": 129,
               "weight": 120,
               "units": "g",
               "quantity": 7
           },
           {
               "id": 70,
               "name": "Chocolate Croissant",
               "price": 104,
               "weight": 96,
               "units": "g",
               "quantity": 1
           },
           {
               "id": 71,
               "name": "Smoked Salmon Croissant",
               "price": 119,
               "weight": 90,
               "units": "g",
               "quantity": 1
           },
           {
               "id": 72,
               "name": "Belgian Chocolate Cake Mix",
               "price": 359,
               "weight": 125,
               "units": "g",
               "quantity": 1
           },
           {
               "id": 73,
               "name": "Queso para untar: Queso crema",
               "price": 79,
               "weight": 130,
               "units": "g",
               "quantity": 1
           },
           {
               "id": 74,
               "name": "Queso Slices",
               "price": 239,
               "weight": 400,
               "units": "g",
               "quantity": 1
           },
           {
               "id": 75,
               "name": "Queso Spread - Roasted Garlic",
               "price": 129,
               "weight": 200,
               "units": "g",
               "quantity": 1
           },
           {
               "id": 76,
               "name": "Spicy Queso Straw",
               "price": 229,
               "weight": 250,
               "units": "g",
               "quantity": 1
           },
           {
               "id": 77,
               "name": "Rebanadas de queso procesado",
               "price": 220,
               "weight": 250,
               "units": "g",
               "quantity": 1
           },
           {
               "id": 78,
               "name": "Cubos de queso procesado",
               "price": 399,
               "weight": 200,
               "units": "g",
               "quantity": 1
           },
           {
               "id": 79,
               "name": "Soyabean Tempeh Cubes",
               "price": 209,
               "weight": 300,
               "units": "g",
               "quantity": 1
           },
           {
               "id": 82,
               "name": "Center Filled Dark Chocolate Cookies",
               "price": 129,
               "weight": 100,
               "units": "g",
               "quantity": 1
           },
           {
               "id": 83,
               "name": "Enrobed Cinnamon Milk Chocolate Dipped Cookies",
               "price": 225,
               "weight": 100,
               "units": "g",
               "quantity": 1
           },
           {
               "id": 84,
               "name": "Oreo & Crème Frozen Dessert",
               "price": 339,
               "weight": 300,
               "units": "ml",
               "quantity": 1
           },
           {
               "id": 85,
               "name": "Chocorich Eclairs Chocolate - Assorted",
               "price": 429,
               "weight": 200,
               "units": "g",
               "quantity": 1
           }
       ],
       "productsCount": 19
   }
                                                * Error: No se han encontrado kits coincidentes
HTTP/1.1 404 Not found.
{
       "code": 404,
       "message": "Not found"
   }
Main.Basket
Main.Basket - Añadir productos a la cesta
put
/api/v1/orders/:id
                                                * Ejemplos de encabezados
{
    "Content-Type": "application/json"
}
Parámetro
Campo
	Tipo
	Descripción
	id
	number
	id de la cesta en la tabla order_model. Se pasa en la URL
	productsList
	Array
	Una lista de productos que se agregarán al cesta. La lista contiene los ID de los artículos y sus cantidades. Debe enviarse en el cuerpo de la solicitud.
	                                                * Añadir productos a la cesta
{
    "productsList": [
        {
            "id": 1,
            "quantity": 4
        },
        {
            "id": 5,
            "quantity": 2
        },
        {
            "id": 3,
            "quantity": 1
        },
        {
            "id": 4,
            "quantity": 1
        }
    ]
}
                                                * Respuesta: Los artículos se han añadido a la cesta con éxito
HTTP/1.1 200 OK
 {
"productsList": [
    {
        "id": 1,
        "quantity": 10
    },
    {
        "id": 5,
        "quantity": 10
    },
    {
        "id": 3,
        "quantity": 9
    },
    {
        "id": 4,
        "quantity": 5
    }
],
        "status": 0,
        "deliveryPriceOur": 30,
        "deliveryTime": "25~30",
        "courierService": "Fast Delivery",
        "deliveryPrice": 0,
        "wareHouse": "Fresh food",
        "userId": 1,
        "id": 5,
        "productsCost": 75,
        "finalCCost": 174
    }
                                                * Error: Cesta no encontrada
                                                * Error: No hay un almacén para procesar tu pedido
HTTP/1.1 404 Not found.
{
       "code": 404,
       "message": "Not found"
Main.Basket - Crear una cesta
post
/api/v1/orders
                                                * Ejemplos de encabezados
{
    "Content-Type": "application/json"
}
Parámetro
Campo
	Tipo
	Descripción
	productsList
	Array
	Una lista de productos que se agregarán al cesta. La lista contiene los ID de los artículos y sus cantidades. Debe enviarse en el cuerpo de la solicitud.
	deliveryTime
opcional
	number
	Plazo de entrega previsto. Si no se pasa ningún valor, el sistema utiliza la hora actual
	                                                * Crear una cesta
{
    "productsList": [
        {
            "id": 1,
            "quantity": 2
        },
        {
            "id": 5,
            "quantity": 2
        },
        {
            "id": 3,
            "quantity": 1
        }
    ]
}
                                                * Respuesta: La cesta fue creada con éxito
HTTP/1.1 200 OK
{
       "productsList": [
           {
               "id": 1,
               "quantity": 2
           },
           {
               "id": 5,
               "quantity": 2
           },
           {
               "id": 3,
               "quantity": 1
           }
       ],
       "status": 0,
       "deliveryPriceOur": 30,
       "deliveryTime": "25~30",
       "courierService": "Fast Delivery",
       "deliveryPrice": 99,
       "wareHouse": "Fresh food",
       "userId": 1,
       "id": 5,
       "productsCost": 75,
       "finalCCost": 174
   }
                                                * Error: No se han aprobado todos los parámetros requeridos
                                                * Error: No hay un almacén para procesar tu pedido
HTTP/1.1 400 Bad request.
{
       "code": 400,
       "message": "No se han aprobado todos los parámetros requeridos"
   }
Main.Basket - Eliminar la cesta
delete
/api/v1/orders/:id
Parámetro
Campo
	Tipo
	Descripción
	id
	number
	id de la cesta en la tabla order_model. Se pasa en la URL
	                                                * Respuesta: Eliminar una cesta con éxito
HTTP/1.1 200 OK
{
       "ok": true
   }
Main.Basket - Hacer el pedido
put
/api/v1/orders/:id/complete
Parámetro
Campo
	Tipo
	Descripción
	id
	number
	id de la cesta en la tabla order_model. Se pasa en la URL
	                                                * Respuesta: Los artículos se han añadido a la cesta con éxito
HTTP/1.1 200 OK
{
       "ok": true,
   }
                                                * Error: El authToken no ha sido transmitido
HTTP/1.1 401 Unauthorized.
{
       "code": 401,
       "message": "No autorizado",
   }
Main.Basket - Recibir los productos de la cesta
get
/api/v1/orders/:id
Header
Campo
	Tipo
	Descripción
	Authorization
opcional
	string
	Encabezado de autorización en formato Bearer {authToken}.
	                                                * Ejemplo de autorización
{
    "Authorization": "Bearer jknnFApafP4awfAIFfafam2fma"
}
Parámetro
Campo
	Tipo
	Descripción
	id
	string
	id de la cesta en la tabla order_model. Se pasa por el parámetro de URL
	                                                * Recibir la cesta
/api/v1/orders/6
                                                * Respuesta: Los productos de la cesta recibidos con éxito
HTTP/1.1 200 OK
[
    {
           "id": 1,
           "name": "Orange Juice - Cold-Pressed, No Added Sugar, Preservative Free",
           "price": 149,
           "weight": 473,
           "units": "ml",
           "quantity": 3
       },
    {
           "id": 4,
           "name": "Refresco Sprite",
           "price": 79,
           "weight": 900,
           "units": "ml",
           "quantity": 4
       }
    ]
                                                * Error: El authToken no ha sido transmitido
                                                * Error: Cesta no encontrada
HTTP/1.1 401 Unauthorized.
{
       "code": 401,
       "message": "No autorizado",
   }
Main.Orders
Main.Orders - Recepción de pedidos de los usuarios
get
/api/v1/orders
Header
Campo
	Tipo
	Descripción
	Authorization
opcional
	string
	Encabezado de autorización en formato Bearer {authToken}.
	                                                * Recibir los pedidos de los/las usuarios/as
{
    "Authorization": "Bearer jknnFApafP4awfAIFfafam2fma"
}
                                                * Respuesta: Todos los pedidos del/de la usuario/a recibidos con éxito
HTTP/1.1 200 OK
[
    {
           "id": 6,
           "userId": 1,
           "productsList": [
               {
                   "id": 1,
                   "quantity": 2
               },
               {
                   "id": 5,
                   "quantity": 2
               },
               {
                   "id": 3,
                   "quantity": 1
               }
           ],
           "deliveryPrice": 0,
           "deliveryPriceOur": 30,
           "deliveryTime": "25~30",
           "wareHouse": "Fresh food",
           "courierService": "Fast Delivery",
           "status": 1
       }
    ]
                                                * Error: El authToken no ha sido transmitido
HTTP/1.1 401 Unauthorized.
{
       "code": 401,
       "message": "    ",
   }
Utils
Utils - Logs de mensajeros/almacenes del servidor
Se trata de una herramienta para obtener las últimas líneas del log mixto de todos los servidores secundarios (mensajeros y almacenes). The count parameter means the number of lines to be read and returned in the response
get
/api/logs/secondary
Parámetro
Campo
	Tipo
	Descripción
	count
opcional
	number
	Número de líneas desde el final
Valor por defecto: 50
	                                                * Obtener los últimos 50 registros
                                                * Obtener los últimos 100 registros
/api/logs/secondary
                                                * Respuesta: Últimos registros del log
2020-08-26T16:07:33.017Z [INFO] [Warehouse][food-city]: Server is listening at port 4022
2020-08-26T16:08:01.324Z [DEBUG] [Warehouse][everything-you-need]: [Request] - ::ffff:127.0.0.1 POST:/everything-you-need/v1/calculate - HTTP/1.1 - application/json - {"deliveryTime":10,"products":[{"id":1,"quantity":1},{"id":4,"quantity":1},{"id":44,"quantity":1}]}
2020-08-26T16:08:01.324Z [DEBUG] [Warehouse][fresh-food]: [Request] - ::ffff:127.0.0.1 POST:/fresh-food/v2.0.1/ct - HTTP/1.1 - application/json - {"deliveryTime":10,"products":[{"id":1,"quantity":1},{"id":4,"quantity":1},{"id":44,"quantity":1}]}
2020-08-26T16:08:01.324Z [DEBUG] [Warehouse][big-world]: [SOAP Client] received <?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  xmlns:tns="WebServices.WarehouseWsdl"><soap:Body><tns:checkSupply><tns:deliveryTime>10</tns:deliveryTime><tns:products><tns:products><id>1</id><quantity>1</quantity></tns:products><tns:products><id>4</id><quantity>1</quantity></tns:products><tns:products><id>44</id><quantity>1</quantity></tns:products></tns:products></tns:checkSupply></soap:Body></soap:Envelope>
2020-08-26T16:08:01.361Z [DEBUG] [Warehouse][food-city]: [Request] - ::ffff:127.0.0.1 POST:/food-city/calculate.xml - HTTP/1.1 - application/xml - <InputModel><deliveryTime>10</deliveryTime><product id="1" quantity="1"/><product id="4" quantity="1"/><product id="44" quantity="1"/></InputModel>
2020-08-26T16:39:17.168Z [DEBUG] [Warehouse][big-world]: [SOAP Client] received <?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  xmlns:tns="WebServices.WarehouseWsdl"><soap:Body><tns:checkSupply><tns:deliveryTime>10</tns:deliveryTime><tns:products><tns:products><id>1</id><quantity>1</quantity></tns:products><tns:products><id>4</id><quantity>1</quantity></tns:products><tns:products><id>44</id><quantity>1</quantity></tns:products></tns:products></tns:checkSupply></soap:Body></soap:Envelope>
2020-08-26T16:39:17.168Z [DEBUG] [Warehouse][fresh-food]: [Request] - ::ffff:127.0.0.1 POST:/fresh-food/v2.0.1/ct - HTTP/1.1 - application/json - {"deliveryTime":10,"products":[{"id":1,"quantity":1},{"id":4,"quantity":1},{"id":44,"quantity":1}]}
2020-08-26T16:39:17.170Z [DEBUG] [Warehouse][everything-you-need]: [Request] - ::ffff:127.0.0.1 POST:/everything-you-need/v1/calculate - HTTP/1.1 - application/json - {"deliveryTime":10,"products":[{"id":1,"quantity":1},{"id":4,"quantity":1},{"id":44,"quantity":1}]}
2020-08-26T16:39:17.173Z [DEBUG] [Warehouse][food-city]: [Request] - ::ffff:127.0.0.1 POST:/food-city/calculate.xml - HTTP/1.1 - application/xml - <InputModel><deliveryTime>10</deliveryTime><product id="1" quantity="1"/><product id="4" quantity="1"/><product id="44" quantity="1"/></InputModel>
2020-08-26T16:39:21.398Z [DEBUG] [Courier][food-service]: [SOAP Client] received <?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  xmlns:tns="WebServices.CourierWsdl"><soap:Body><Request xmlns="WebServices.CourierWsdl"><productsCount>3</productsCount><productsWeight>1.433</productsWeight><deliveryTime>7</deliveryTime></Request></soap:Body></soap:Envelope>
2020-08-26T16:39:21.453Z [DEBUG] [Courier][fast-delivery]: [Request] - ::ffff:127.0.0.1 POST:/fast-delivery/v3.1.1/calculate-delivery.xml - HTTP/1.1 - application/xml - {"InputModel":{"deliveryTime":["7"],"productsWeight":["1.433"],"productsCount":["3"]}}
2020-08-26T16:39:21.481Z [DEBUG] [Courier][order-and-go]: [Request] - ::ffff:127.0.0.1 POST:/order-and-go/v1/delivery - HTTP/1.1 - application/json - {"productsCount":3,"productsWeight":1.433,"deliveryTime":7}
2020-08-26T16:39:21.489Z [DEBUG] [Courier][speedy]: [Request] - ::ffff:127.0.0.1 POST:/speedy/v1/calculate - HTTP/1.1 - application/json - {"productsCount":3,"productsWeight":1.433,"deliveryTime":7}
Utils - Logs del servidor principal
Esta es una herramienta para obtener las últimas líneas en el registro del servidor principal. El parámetro count indica el número de líneas que se leerán y se devolverán a Response
get
/api/logs/main
Parámetro
Campo
	Tipo
	Descripción
	count
opcional
	number
	Número de líneas desde el final
Valor por defecto: 50
	                                                * Obtener los últimos 50 registros
                                                * Obtener los últimos 100 registros
/api/logs/main
                                                * Respuesta: Últimos registros del log
2020-08-26T16:38:31.489Z [INFO] [Main]: Server is listening at port 4000
2020-08-26T16:38:31.500Z [INFO] [Main]: [SOAP Client] Soap is listening at /api/wsdl
2020-08-26T16:38:31.532Z [DEBUG] [Main]: [SOAP Client] TRAIN client is initialized
2020-08-26T16:38:31.564Z [DEBUG] [Main]: [SOAP Client] WORLD client is initialized
2020-08-26T16:38:31.609Z [INFO] [Main]: [PostgreSQL] PostgreSQL is initialized
2020-08-26T16:38:35.057Z [DEBUG] [Main]: [Request] - ::1 GET:/api/logs/main - HTTP/1.1 -  -
2020-08-26T16:39:17.106Z [DEBUG] [Main]: [Request] - ::1 POST:/api/v1/warehouses/amount?dataType=xml - HTTP/1.1 - application/xml - <root><id>1</id><id>4</id><id>44</id></root>
2020-08-26T16:39:21.358Z [DEBUG] [Main]: [Request] - ::1 POST:/api/v1/couriers/check - HTTP/1.1 - application/json - {"ids":[1,4,44],"deliveryTime":7}
2020-08-26T16:39:36.767Z [DEBUG] [Main]: [Request] - ::1 GET:/api/v1/orders - HTTP/1.1 - application/json - {"productsList":"1,4"}
2020-08-26T16:39:47.908Z [DEBUG] [Main]: [Request] - ::1 GET:/api/logs/main - HTTP/1.1 -  -
2020-08-26T16:07:32.123Z [ERROR] [Main]: Unexpected error:
2020-08-26T16:07:32.127Z [ERROR] [Main]:          {"message":"request to http://localhost:4022/food-city/calculate.xml failed, reason: connect ECONNREFUSED 127.0.0.1:4022","type":"system","errno":"ECONNREFUSED","code":"ECONNREFUSED","stack":"FetchError: request to http://localhost:4022/food-city/calculate.xml failed, reason: connect ECONNREFUSED 127.0.0.1:4022\n    at ClientRequest.<anonymous> (/Users/vladimirlevin/Desktop/Own/ez-lavka/packages/main/node_modules/node-fetch/lib/index.js:1455:11)\n    at ClientRequest.emit (events.js:198:13)\n    at ClientRequest.EventEmitter.emit (domain.js:448:20)\n    at Socket.socketErrorListener (_http_client.js:401:9)\n    at Socket.emit (events.js:198:13)\n    at Socket.EventEmitter.emit (domain.js:448:20)\n    at emitErrorNT (internal/streams/destroy.js:91:8)\n    at emitErrorAndCloseNT (internal/streams/destroy.js:59:3)\n    at process._tickCallback (internal/process/next_tick.js:63:19)"}
2020-08-26T16:07:32.131Z [ERROR] [Main]: Unexpected error:
2020-08-26T16:07:32.162Z [ERROR] [Main]:          {"stack":"RangeError [ERR_HTTP_INVALID_STATUS_CODE]: Invalid status code: ECONNREFUSED\n    at ServerResponse.writeHead (_http_server.js:211:11)\n    at ServerResponse._implicitHeader (_http_server.js:202:8)\n    at write_ (_http_outgoing.js:585:9)\n    at ServerResponse.end (_http_outgoing.js:702:5)\n    at ServerResponse.send (/Users/vladimirlevin/Desktop/Own/ez-lavka/packages/main/node_modules/express/lib/response.js:221:10)\n    at ServerResponse.json (/Users/vladimirlevin/Desktop/Own/ez-lavka/packages/main/node_modules/express/lib/response.js:267:15)\n    at app.use (/Users/vladimirlevin/Desktop/Own/ez-lavka/packages/main/src/app.ts:77:14)\n    at Layer.handle_error (/Users/vladimirlevin/Desktop/Own/ez-lavka/packages/main/node_modules/express/lib/router/layer.js:71:5)\n    at trim_prefix (/Users/vladimirlevin/Desktop/Own/ez-lavka/packages/main/node_modules/express/lib/router/index.js:315:13)\n    at /Users/vladimirlevin/Desktop/Own/ez-lavka/packages/main/node_modules/express/lib/router/index.js:284:7\n    at Function.process_params (/Users/vladimirlevin/Desktop/Own/ez-lavka/packages/main/node_modules/express/lib/router/index.js:335:12)\n    at next (/Users/vladimirlevin/Desktop/Own/ez-lavka/packages/main/node_modules/express/lib/router/index.js:275:10)\n    at ServiceContext.next (/Users/vladimirlevin/Desktop/Own/ez-lavka/packages/main/node_modules/express/lib/router/route.js:127:14)\n    at ServiceInvoker.<anonymous> (/Users/vladimirlevin/Desktop/Own/ez-lavka/packages/main/node_modules/typescript-rest/src/server/service-invoker.ts:37:21)\n    at Generator.throw (<anonymous>)\n    at rejected (/Users/vladimirlevin/Desktop/Own/ez-lavka/packages/main/node_modules/typescript-rest/dist/server/service-invoker.js:6:65)\n    at process._tickCallback (internal/process/next_tick.js:68:7)","message":"Invalid status code: ECONNREFUSED"}
2020-08-26T16:08:01.311Z [DEBUG] [Main]: [Request] - ::1 POST:/api/v1/warehouses/amount - HTTP/1.1 - application/json - {"ids":[1,4,44]}
Utils - Recuperar información de la tabla de base de datos
get
/api/db/resources/{table_name}.csv
Parámetro
Campo
	Tipo
	Descripción
	table_name
	string
	El nombre de la tabla en la base de datos. Se pasa en la URL.
	                                                * Recibir la tabla product_model
                                                * Recibir la tabla kit_model
/api/db/resources/product_model.csv
                                                * Respuesta: Archivo con el contenido de la tabla product_model
id,name,price,weight,units,categoryId,
1,Orange Juice - Cold-Pressed, No Added Sugar, Preservative Free,149,473,ml,1
2,Refresco Mountain Dew,89,1,l,1
3,Refresco Pepsi,109,1,l,1
4,Refresco Sprite,79,900,ml,1
5,Jugo Fruit Power: Lichi,349,900,ml,1
d,name,price,weight,units,categoryId,
1,Orange Juice - Cold-Pressed, No Added Sugar, Preservative Free,149,473,ml,1
2,Refresco Mountain Dew,89,1,l,1
3,Refresco Pepsi,109,1,l,1
4,Refresco Sprite,79,900,ml,1
5,Jugo Fruit Power: Lichi,349,900,ml,1
V
Filter...
x
                                                * Warehouses
                                                * Almacén: "Big World"
                                                * Almacén: "Everything You Need"
                                                * Almacén: "Food City"
                                                * Comprobar la cantidad de productos en stock
                                                * Comprobar la disponibilidad de productos en los almacenes
                                                * Obtener la lista de almacenes
                                                * Wharehouse: "Fresh Food"
                                                * [SOAP] Comprobar la cantidad de productos en stock
                                                * Couriers
                                                * Comprobar los costes de envío
                                                * Entrega: "Fast Delivery"
                                                * Entrega: "Food Service"
                                                * Entrega: "Order and Go"
                                                * Entrega: "Speedy"
                                                * Obtener la lista de entregas
                                                * Main.User
                                                * Creación de cuenta
                                                * Main.Products
                                                * Búsqueda de kit por producto
                                                * Cambio del precio del producto
                                                * Main.Kits
                                                * Añadir productos a la kit:
                                                * Cambio de la kit
                                                * Crear un kit
                                                * Eliminación del kit
                                                * Recibir todas las kit
                                                * Recibir una kit por el nombre
                                                * Main.Basket
                                                * Añadir productos a la cesta
                                                * Crear una cesta
                                                * Eliminar la cesta
                                                * Hacer el pedido
                                                * Recibir los productos de la cesta
                                                * Main.Orders
                                                * Recepción de pedidos de los usuarios
                                                * Utils
                                                * Logs de mensajeros/almacenes del servidor
                                                * Logs del servidor principal
                                                * Recuperar información de la tabla de base de datos
API Urban Grocers
Warehouses
Warehouses - Almacén: "Big World"
La interacción se realiza a través de SOAP
post
/big-world/wsdl
Parámetro
Campo
	Tipo
	Descripción
	deliveryTime
	number
	Plazo de entrega previsto
	products
	Array
	Lista de productos
	  id
	number
	Identificador del producto de la tabla product_model
	  quantity
	number
	Cantidad de producto
	                                                * Ejemplo de solicitud
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  xmlns:tns="WebServices.WarehouseWsdl">
    <soap:Body>
        <tns:checkSupply>
            <tns:products>
                <tns:products>
                    <id>1</id>
                    <quantity>1</quantity>
                </tns:products>
                <tns:products>
                    <id>4</id>
                    <quantity>1</quantity>
                </tns:products>
                <tns:products>
                    <id>44</id>
                    <quantity>1</quantity>
                </tns:products>
            </tns:products>
            <tns:deliveryTime>10</tns:deliveryTime>
        </tns:checkSupply>
    </soap:Body>
</soap:Envelope>
                                                * Respuesta: Ejemplo de respuesta
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"  xmlns:tns="WebServices.WarehouseWsdl">
    <soap:Body>
        <tns:checkSupplyResponse>
            <tns:name>Big World</tns:name>
            <tns:workingHours>
                <start>5</start>
                <end>20</end>
            </tns:workingHours>
            <tns:price>9.5</tns:price>
            <tns:isWarehouseWorking>true</tns:isWarehouseWorking>
            <tns:isItemsAvailable>false</tns:isItemsAvailable>
            <tns:percentOfAvailableItems>33</tns:percentOfAvailableItems>
            <tns:availableProducts>
                <tns:availableProducts>
                    <id>1</id>
                    <quantity>1</quantity>
                </tns:availableProducts>
            </tns:availableProducts>
        </tns:checkSupplyResponse>
    </soap:Body>
</soap:Envelope>
Warehouses - Almacén: "Everything You Need"
post
/everything-you-need/v1/calculate
                                                * Ejemplos de encabezados
{
    "Content-Type": "application/json"
}
Parámetro
Campo
	Tipo
	Descripción
	deliveryTime
	number
	Plazo de entrega previsto
	products
	Array
	Lista de productos
	  id
	number
	Identificador del producto de la tabla product_model
	  quantity
	number
	Cantidad de producto
	                                                * Ejemplo de solicitud
{
    "deliveryTime": 9,
    "products": [
        {
            "id": 1,
            "quantity": 1
        },
        {
            "id": 4,
            "quantity": 3
        }
    ]
}
                                                * Respuesta: Ejemplo de respuesta
HTTP/1.1 200 OK
{
       "name": "Everything You Need",
       "workingHours": { "start": 8, "end": 23 },
       "price": 10,
       "availableProducts": [
           { "id": 1, "quantity": 2 }
       ],
       "isWarehouseWorking": true,
       "isItemsAvailable": true,
       "percentOfAvailableItems": 80
   }
Warehouses - Almacén: "Food City"
Interacción a través de XML
post
/food-city/calculate.xml
                                                * Ejemplos de encabezados
{
    "Content-Type": "application/xml"
}
Parámetro
Campo
	Tipo
	Descripción
	deliveryTime
	number
	Plazo de entrega previsto
	products
	Array
	Lista de productos
	  id
	number
	Identificador del producto de la tabla product_model
	  quantity
	number
	Cantidad de producto
	                                                * Ejemplo de solicitud
<?xml version="1.0" encoding="UTF-8"?>
<InputModel>
    <deliveryTime>9</deliveryTime>
    <product id="5" quantity="2" />
    <product id="4" quantity="1" />
</InputModel>
                                                * Respuesta: Ejemplo de respuesta
<response name="Food City" price="8" isWarehouseWorking="true" isItemsAvailable="true" percentOfAvailableItems="100">
    <working_hours>
       <start>8</start>
       <end>21</end>
    </working_hours>
    <available_products>
       <product id="5" quantity="6"/>
       <product id="4" quantity="12"/>
    </available_products>
</response>
Warehouses - Comprobar la cantidad de productos en stock
La versión SOAP de este punto final se llama - [SOAP] Comprobar la cantidad de productos en stock
post
/api/v1/warehouses/amount
                                                * [JSON] Ejemplos de encabezados
                                                * [XML] Ejemplos de encabezados
{
    "Content-Type": "application/json"
}
Parámetro
Campo
	Tipo
	Descripción
	ids
	number[]
	Una matriz de identificadores de productos (después de id en la tabla product_model).
	dataType
opcional
	string
	Formato de los datos de entrada. Puede tomar valores:
                                                * "json" - El cuerpo de la solicitud se espera en formato JSON
                                                * "xml" - El cuerpo de la solicitud se espera en formato XML
Valor por defecto: json
	                                                * [JSON] Comprobar la cantidad de productos
                                                * [XML] Comprobar la cantidad de productos
{
    "ids": [
        1,
        4,
        44
    ]
}
                                                * Respuesta: En qué almacén, qué hay disponible y cuánto
HTTP/1.1 200 OK
{
       "Everything You Need": {
           "Refresco Sprite": 9,
           "Gourmet Palomitas Kernels": 6
       },
       "Food City": {
           "Orange Juice - Cold-Pressed, No Added Sugar, Preservative Free": 3,
           "Refresco Sprite": 12
       },
       "Big World": {
           "Orange Juice - Cold-Pressed, No Added Sugar, Preservative Free": 1
       },
       "Fresh food": {
           "Orange Juice - Cold-Pressed, No Added Sugar, Preservative Free": 3,
           "Refresco Sprite": 12
       }
   }
Warehouses - Comprobar la disponibilidad de productos en los almacenes
post
/api/v1/warehouses/check
                                                * Ejemplos de encabezados
{
    "Content-Type": "application/json"
}
Parámetro
Campo
	Tipo
	Descripción
	products
	number[]
	Una matriz de identificadores de productos and their quantities (Campos id en la tabla product_model).
	                                                * Comprobar la disponibilidad de productos
{
    "products": [
        {
            "id": 5,
            "quantity": 1
        },
        {
            "id": 4,
            "quantity": 5
        }
    ]
}
                                                * Respuesta: En qué almacén, qué hay disponible y cuánto
HTTP/1.1 200 OK
{
       "Everything You Need": {
           "Refresco Sprite": true,
           "Gourmet Palomitas Kernels": true,
           "Orange Juice - Cold-Pressed, No Added Sugar, Preservative Free": false
       },
       "Food City": {
           "Orange Juice - Cold-Pressed, No Added Sugar, Preservative Free": true,
           "Refresco Sprite": true,
           "Gourmet Palomitas Kernels": false
       },
       "Big World": {
           "Orange Juice - Cold-Pressed, No Added Sugar, Preservative Free": true,
           "Refresco Sprite": false,
           "Gourmet Palomitas Kernels": false
       },
       "Fresh food": {
           "Orange Juice - Cold-Pressed, No Added Sugar, Preservative Free": true,
           "Refresco Sprite": true,
           "Gourmet Palomitas Kernels": false
       }
   }
Warehouses - Obtener la lista de almacenes
get
/api/v1/warehouses
                                                * Respuesta: Obtener la lista de almacenes con éxito
HTTP/1.1 200 OK
[
    {
           "name": "Everything You Need",
           "workingHours": {
               "start": 7,
               "end": 23
           }
       },
    {
           "name": "Fresh food",
           "workingHours": {
               "start": 8,
               "end": 23
           }
       },
    {
           "name": "Food City",
           "workingHours": {
               "start": 8,
               "end": 21
           }
       },
    {
           "name": "Big World",
           "workingHours": {
               "start": 5,
               "end": 20
           }
       }
    ]
Warehouses - Wharehouse: "Fresh Food"
post
/fresh-food/v2.0.1/ct
                                                * Ejemplos de encabezados
{
    "Content-Type": "application/json"
}
Parámetro
Campo
	Tipo
	Descripción
	deliveryTime
	number
	Plazo de entrega previsto
	products
	Array
	Lista de productos
	  id
	number
	Identificador del producto de la tabla product_model
	  quantity
	number
	Cantidad de producto
	                                                * Ejemplo de solicitud
{
    "deliveryTime": 9,
    "products": [
        {
            "id": 1,
            "quantity": 1
        },
        {
            "id": 4,
            "quantity": 3
        }
    ]
}
                                                * Respuesta: Ejemplo de respuesta
HTTP/1.1 200 OK
{
       "name": "Fresh food",
       "workingHours": { "start": 8, "end": 23 },
       "price": 10,
       "availableProducts": [
           { "id": 1, "quantity": 2 }
       ],
       "isWarehouseWorking": true,
       "isItemsAvailable": true,
       "percentOfAvailableItems": 80
   }
Warehouses - [SOAP] Comprobar la cantidad de productos en stock
post
/api/wsdl
Parámetro
Campo
	Tipo
	Descripción
	ids
	number[]
	Una matriz de identificadores de productos (después de id en la tabla product_model).
	                                                * [XML] Comprobar la cantidad de productos
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  xmlns:tns="WebServices.MainWsdl">
    <soap:Body>
        <Request xmlns="WebServices.MainWsdl">
            <ids>1</ids>
            <ids>4</ids>
            <ids>44</ids>
        </Request>
    </soap:Body>
</soap:Envelope>
                                                * Respuesta: En qué almacén, qué hay disponible y cuánto
   HTTP/1.1 200 OK
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"  xmlns:tns="WebServices.MainWsdl">
    <soap:Body>
        <Response>
            <name>Everything You Need</name>
            <products>
                <name>Refresco Sprite</name>
                <quantity>9</quantity>
            </products>
            <products>
                <name>Gourmet Palomitas Kernels</name>
                <quantity>6</quantity>
            </products>
        </Response>
        <Response>
            <name>Food City</name>
            <products>
                <name>Orange Juice - Cold-Pressed, No Added Sugar, Preservative Free</name>
                <quantity>3</quantity>
            </products>
            <products>
                <name>Refresco Sprite</name>
                <quantity>12</quantity>
            </products>
        </Response>
        <Response>
            <name>Big World</name>
            <products>
                <name>Orange Juice - Cold-Pressed, No Added Sugar, Preservative Free</name>
                <quantity>1</quantity>
            </products>
        </Response>
        <Response>
            <name>Fresh food</name>
            <products>
                <name>Orange Juice - Cold-Pressed, No Added Sugar, Preservative Free</name>
                <quantity>3</quantity>
            </products>
            <products>
                <name>Refresco Sprite</name>
                <quantity>12</quantity>
            </products>
        </Response>
    </soap:Body>
</soap:Envelope>
Couriers
Couriers - Comprobar los costes de envío
post
/api/v1/couriers/check
                                                * Ejemplos de encabezados
{
    "Content-Type": "application/json"
}
Parámetro
Campo
	Tipo
	Descripción
	products
	number[]
	Una matriz de identificadores de productos and their quantities (después de id en la tabla product_model).
	deliveryTime
	number
	Plazo de entrega previsto (from 0 to 23)
	                                                * Comprobar los costes de los diferentes servicios
{
    "products": [
        {
            "id": 1,
            "quantity": 3
        },
        {
            "id": 4,
            "quantity": 1
        },
        {
            "id": 9,
            "quantity": 3
        }
    ],
    "deliveryTime": 7
}
                                                * Respuesta: Cuánto costaría cada uno de los servicios
HTTP/1.1 200 OK
{
       "Fast Delivery": {
           "deliveryPrice": 0
       },
       "Speedy": {
           "deliveryPrice": 99
       },
       "Food Service": {
           "deliveryPrice": 0
       },
       "Order and Go": {
           "deliveryPrice": 99
       }
   }
Couriers - Entrega: "Fast Delivery"
La interacción se realiza mediante XML
post
/fast-delivery/v3.1.1/calculate-delivery.xml
                                                * Ejemplos de encabezados
{
    "Content-Type": "application/xml"
}
Parámetro
Campo
	Tipo
	Descripción
	productsCount
	number
	Número de productos en el pedido
	productsWeight
	number
	Peso de los productos
	deliveryTime
	number
	Plazo de entrega previsto
	                                                * Ejemplo de solicitud
<InputModel>
    <productsCount>2</productsCount>
    <productsWeight>5.115</productsWeight>
    <deliveryTime>20</deliveryTime>
</InputModel>
                                                * Respuesta: Ejemplo de respuesta
HTTP/1.1 200 OK
<response name="Fast Delivery" isItPossibleToDeliver="true" hostDeliveryCost="43" clientDeliveryCost="0">
    <toBeDeliveredTime>
        <min>25</min>
        <max>30</max>
    </toBeDeliveredTime>
</response>
Couriers - Entrega: "Food Service"
Interacción a través de SOAP
post
/food-service/wsdl
Parámetro
Campo
	Tipo
	Descripción
	productsCount
	number
	Número de productos en el pedido
	productsWeight
	number
	Peso de los productos
	deliveryTime
	number
	Plazo de entrega previsto
	                                                * Ejemplo de solicitud
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  xmlns:tns="WebServices.CourierWsdl">
    <soap:Body>
        <Request xmlns="WebServices.CourierWsdl">
            <productsCount>3</productsCount>
            <productsWeight>1.433</productsWeight>
            <deliveryTime>7</deliveryTime>
        </Request>
    </soap:Body>
</soap:Envelope>
                                                * Respuesta: Ejemplo de respuesta
HTTP/1.1 200 OK
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"  xmlns:tns="WebServices.CourierWsdl">
    <soap:Body>
        <Response xmlns="WebServices.CourierWsdl">
        <name>Food Service</name>
        <isItPossibleToDeliver>true</isItPossibleToDeliver>
        <hostDeliveryCost>29</hostDeliveryCost>
        <toBeDeliveredTime>
            <min>25</min>
            <max>30</max>
        </toBeDeliveredTime>
        <clientDeliveryCost>0</clientDeliveryCost>
        </Response>
    </soap:Body>
</soap:Envelope>
Couriers - Entrega: "Order and Go"
post
/order-and-go/v1/delivery
                                                * Ejemplos de encabezados
{
    "Content-Type": "application/json"
}
Parámetro
Campo
	Tipo
	Descripción
	productsCount
	number
	Número de productos en el pedido
	productsWeight
	number
	Peso de los productos
	deliveryTime
	number
	Plazo de entrega previsto
	                                                * Ejemplo de solicitud
{
    "deliveryTime": 9,
    "productsCount": 10,
    "productsWeight": 11
}
                                                * Respuesta: Ejemplo de respuesta
HTTP/1.1 200 OK
   {
       "name": "Order and Go",
       "clientDeliveryCost": 10,
       "toBeDeliveredTime": { "min": 10, "max": 20 },
       "hostDeliveryCost": 23,
       "isItPossibleToDeliver": true
   }
Couriers - Entrega: "Speedy"
post
/speedy/v1/calculate
                                                * Ejemplos de encabezados
{
    "Content-Type": "application/json"
}
Parámetro
Campo
	Tipo
	Descripción
	productsCount
	number
	Número de productos en el pedido
	productsWeight
	number
	Peso de los productos
	deliveryTime
	number
	Plazo de entrega previsto
	                                                * Ejemplo de solicitud
{
    "deliveryTime": 9,
    "productsCount": 10,
    "productsWeight": 11
}
                                                * Respuesta: Ejemplo de respuesta
HTTP/1.1 200 OK
   {
       "name": "Speedy",
       "clientDeliveryCost": 10,
       "toBeDeliveredTime": { "min": 10, "max": 20 },
       "hostDeliveryCost": 23,
       "isItPossibleToDeliver": true
   }
Couriers - Obtener la lista de entregas
get
/api/v1/couriers
                                                * Respuesta: Recibir las entregas con éxito
   HTTP/1.1 200 OK
    [
           {
               "name": "Order and Go",
               "workingHours": {
                   "start": 8,
                   "end": 22
               }
           },
           {
               "name": "Speedy",
               "workingHours": {
                   "start": 8,
                   "end": 22
               }
           },
           {
               "name": "Fast Delivery",
               "workingHours": {
                   "start": 7,
                   "end": 21
               }
           },
           {
               "name": "Food Service",
               "workingHours": {
                   "start": 6,
                   "end": 20
               }
           }
]
Main.User
Main.User - Creación de cuenta
post
/api/v1/users
                                                * Ejemplos de encabezados
{
    "Content-Type": "application/json"
}
Parámetro
Campo
	Tipo
	Descripción
	firstName
	string
	Nombre de usuario/a, escrito en el campo firstName de la tabla Users
	phone
	string
	El número de teléfono del/de la usuario/a se escribe en el campo phone de la tabla Users
	address
	string
	La dirección del/de la usuario/a se escribe en el campo address de la tabla Users
	email
opcional
	string
	Dirección de correo electrónico, escrita en el campo email de la tabla Users
	comment
opcional
	string
	Comentario de usuario/a, escrito en el campo comment de la tabla Users
	                                                * Conjunto mínimo de datos
                                                * Información completa sobre el/la usuario/a
{
    "firstName": "Max",
    "phone": "+10005553535",
    "address": "8042 Lancaster Ave.Hamburg, NY"
}
                                                * La cuenta de usuario se ha creado correctamente
HTTP/1.1 201 Creado
{
    authToken: 'jknnFApafP4awfAIFfafam2fma'
}
                                                * Error en los datos de entrada #1
                                                * Error en los datos de entrada #2
                                                * Error en los datos de entrada #3
                                                * Error en los datos de entrada #4
HTTP/1.1 400 Bad request.
{
    "code": 400,
    "message": "No se han aprobado todos los parámetros requeridos. Parámetros requeridos: nombre, teléfono, dirección"
}
Main.Products
Main.Products - Búsqueda de kit por producto
endpoint para buscar kit que contengan los productos especificados
post
/api/v1/products/kits
                                                * Ejemplos de encabezados
{
    "Content-Type": "application/json"
}
Parámetro
Campo
	Tipo
	Descripción
	ids
	number[]
	Una matriz de identificadores de productos from the table product_model.
	                                                * Buscar kit que contengan el producto 1 o 2 o 3:
{
    "ids": [
        1,
        2,
        3
    ]
}
                                                * Respuesta: Recibir las kit con éxito
HTTP/1.1 200 OK
[
    {
           "id": 1,
           "name": "Para pícnics",
           "productsList": [
               {
                   "id": 1,
                   "quantity": 1
               },
               {
                   "id": 2,
                   "quantity": 1
               },
               {
                   "id": 3,
                   "quantity": 1
               },
               {
                   "id": 4,
                   "quantity": 1
               },
               {
                   "id": 5,
                   "quantity": 1
               },
               {
                   "id": 6,
                   "quantity": 1
               },
               {
                   "id": 7,
                   "quantity": 1
               },
               {
                   "id": 8,
                   "quantity": 1
               },
               {
                   "id": 9,
                   "quantity": 1
               },
               {
                   "id": 10,
                   "quantity": 1
               },
               {
                   "id": 11,
                   "quantity": 1
               },
               {
                   "id": 12,
                   "quantity": 1
               },
               {
                   "id": 13,
                   "quantity": 1
               },
               {
                   "id": 14,
                   "quantity": 1
               },
               {
                   "id": 15,
                   "quantity": 1
               },
               {
                   "id": 16,
                   "quantity": 1
               },
               {
                   "id": 17,
                   "quantity": 1
               },
               {
                   "id": 18,
                   "quantity": 1
               },
               {
                   "id": 19,
                   "quantity": 1
               },
               {
                   "id": 20,
                   "quantity": 1
               },
               {
                   "id": 21,
                   "quantity": 1
               },
               {
                   "id": 22,
                   "quantity": 1
               },
               {
                   "id": 23,
                   "quantity": 1
               },
               {
                   "id": 24,
                   "quantity": 1
               },
               {
                   "id": 25,
                   "quantity": 1
               },
               {
                   "id": 26,
                   "quantity": 1
               },
               {
                   "id": 27,
                   "quantity": 1
               },
               {
                   "id": 28,
                   "quantity": 1
               },
               {
                   "id": 29,
                   "quantity": 1
               },
               {
                   "id": 30,
                   "quantity": 1
               },
               {
                   "id": 31,
                   "quantity": 1
               },
               {
                   "id": 32,
                   "quantity": 1
               },
               {
                   "id": 33,
                   "quantity": 1
               },
               {
                   "id": 34,
                   "quantity": 1
               },
               {
                   "id": 35,
                   "quantity": 1
               },
               {
                   "id": 36,
                   "quantity": 1
               },
               {
                   "id": 37,
                   "quantity": 1
               },
               {
                   "id": 38,
                   "quantity": 1
               },
               {
                   "id": 39,
                   "quantity": 1
               }
           ],
           "productsCount": 39
       },
    {
           "id": 2,
           "name": "Para películas y series",
           "productsList": [
               {
                   "id": 7,
                   "quantity": 1
               },
               {
                   "id": 8,
                   "quantity": 1
               },
               {
                   "id": 9,
                   "quantity": 1
               },
               {
                   "id": 40,
                   "quantity": 1
               },
               {
                   "id": 41,
                   "quantity": 1
               },
               {
                   "id": 42,
                   "quantity": 1
               },
               {
                   "id": 43,
                   "quantity": 1
               },
               {
                   "id": 44,
                   "quantity": 1
               },
               {
                   "id": 45,
                   "quantity": 1
               },
               {
                   "id": 46,
                   "quantity": 1
               },
               {
                   "id": 47,
                   "quantity": 1
               },
               {
                   "id": 2,
                   "quantity": 1
               },
               {
                   "id": 3,
                   "quantity": 1
               },
               {
                   "id": 4,
                   "quantity": 1
               },
               {
                   "id": 48,
                   "quantity": 1
               },
               {
                   "id": 49,
                   "quantity": 1
               },
               {
                   "id": 50,
                   "quantity": 1
               },
               {
                   "id": 51,
                   "quantity": 1
               },
               {
                   "id": 52,
                   "quantity": 1
               },
               {
                   "id": 53,
                   "quantity": 1
               },
               {
                   "id": 54,
                   "quantity": 1
               },
               {
                   "id": 55,
                   "quantity": 1
               },
               {
                   "id": 56,
                   "quantity": 1
               },
               {
                   "id": 57,
                   "quantity": 1
               },
               {
                   "id": 58,
                   "quantity": 1
               },
               {
                   "id": 59,
                   "quantity": 1
               },
               {
                   "id": 60,
                   "quantity": 1
               }
           ],
           "productsCount": 27
       }
    ]
Main.Products - Cambio del precio del producto
put
/api/v1/products/:id
                                                * Ejemplos de encabezados
{
    "Content-Type": "application/json"
}
Parámetro
Campo
	Tipo
	Descripción
	id
	number
	El id de la kit en la tabla product_model. Se pasa en la URL
	price
opcional
	string
	price del producto. Se pasa en el texto de la solicitud.
	                                                * Cambio del producto /api/v1/products/7
{
    "price": 175
}
                                                * Respuesta: El kit ha sido eliminado con éxito.
HTTP/1.1 200 OK
{
       "ok": true
   }
                                                * Error: Producto no encontrado
HTTP/1.1 404 Not found.
{
       "code": 404,
       "message": "Not found"
   }
Main.Kits
Main.Kits - Añadir productos a la kit:
post
/api/v1/kits/:id/products
                                                * Ejemplos de encabezados
{
    "Content-Type": "application/json"
}
Parámetro
Campo
	Tipo
	Descripción
	id
	number
	El id de kit en la tabla kit_model. Se pasa en la URL
	productsList
	Array
	Una lista de productos que se agregarán al kit. La lista contiene los ID de los artículos y sus cantidades. Debe enviarse en el cuerpo de la solicitud.
	                                                * Ejemplo de cuerpo de solicitud para agregar artículos al kit
{
    "productsList": [
        {
            "id": 1,
            "quantity": 2
        },
        {
            "id": 6,
            "quantity": 2
        }
    ]
}
                                                * Respuesta: Completar con éxito la kit de productos
    HTTP/1.1 200 OK
 {
    "id": 2,
    "name": "Mi conjunto del fin de semana",
    "productsList": [
        {
            "id": 1,
            "name": "Caviar rojo",
            "price": 45,
            "weight": 5,
            "units": "kg",
            "quantity": 2
        },
        {
            "id": 5,
            "name": "Baguette",
            "price": 15,
            "weight": 1,
            "units": "kg",
            "quantity": 2
        }
    ],
    "productsCount": 4
}
                                                * Error: No se han encontrado kits coincidentes
                                                * Error: El formato del JSON enviado no es correcto
                                                * Error: El valor en alguno de los parametros es incorrecto
HTTP/1.1 404 Not found.
{
       "code": 404,
       "message": "Not found"
   }
Main.Kits - Cambio de la kit
put
/api/v1/kits/:id
                                                * Ejemplos de encabezados
{
    "Content-Type": "application/json"
}
Parámetro
Campo
	Tipo
	Descripción
	id
	number
	El id de kit en la tabla kit_model. Se pasa en la URL
	name
opcional
	string
	name de la kit. Se pasa en el texto de la solicitud.
	productsList
opcional
	Array
	Una lista de productos que se agregarán al kit. La lista contiene los ID de los artículos y sus cantidades. Debe enviarse en el cuerpo de la solicitud.
	                                                * Cambio de la kit /api/v1/kits/7
{
    "name": "Mi kit modificada",
    "productsList": [
        {
            "id": 1,
            "quantity": 4
        },
        {
            "id": 5,
            "quantity": 2
        },
        {
            "id": 3,
            "quantity": 1
        },
        {
            "id": 4,
            "quantity": 1
        }
    ]
}
                                                * Respuesta: El kit ha sido eliminado con éxito.
HTTP/1.1 200 OK
{
       "ok": true
   }
                                                * Error: No se han encontrado kits coincidentes
HTTP/1.1 404 Not found.
{
       "code": 404,
       "message": "Not found"
   }
Main.Kits - Crear un kit
endpoint para crear una kit de una tarjeta específica O de usuario.
                                                * Es obligatorio pasar el encabezado Authorisation O el parámetro cardId, para crear la kit
                                                * Si se recibe una solicitud con un encabezado Authorisation que contenga el authToken de un/a usuario/a en particular - se creará la kit de este/a usuario/a.
                                                * Si se recibe el parámetro cardId, se creará una kit dentro de la tarjeta correspondiente
                                                * Si no se pasa ninguno de los parámetros, se devolverá un error.
                                                * Cuando se pasan ambos parámetros, Authorization es la prioridad
post
/api/v1/kits
Header
Campo
	Tipo
	Descripción
	Authorization
opcional
	string
	Encabezado de autorización en formato Bearer {authToken}. Cuando se pasa - se devuelven todos las cestas creadas por el/la usuario/a.
	Content-Type
opcional
	string
	Valor por defecto: application/json
	                                                * Ejemplos de encabezados
                                                * Recepción de las cestas creadas por el/la usuario/a
{
    "Content-Type": "application/json"
}
Parámetro
Campo
	Tipo
	Descripción
	cardId
opcional
	number
	El id de la tarjeta en la tabla card_model. Cuando se pasa - se creará un conjunto incluido en esta tarjeta
	name
	string
	El nombre de la kit, que será escrito en el campo correspondiente de la tabla kit_model.
	                                                * Respuesta: El conjunto ha sido creado con éxito
HTTP/1.1 201 Creado
{
       "name": "Mi conjunto",
       "card": {
           "id": 1,
           "name": "Para la situación"
       },
       "productsList": null,
       "id": 7,
       "productsCount": 0
   }
                                                * Error: No se ha transmitido ninguno de los parámetros
                                                * Error: Validación del nombre
HTTP/1.1 400 Bad request.
{
       "code": 400,
       "message": "No se han aprobado todos los parámetros requeridos"
   }
Main.Kits - Eliminación del kit
delete
/api/v1/kits/:id
Parámetro
Campo
	Tipo
	Descripción
	id
	number
	El id de kit en la tabla kit_model. Se pasa en la URL
	                                                * Eliminación de un kit con id=7
/api/v1/kits/7
                                                * Respuesta: El kit ha sido eliminado con éxito.
HTTP/1.1 200 OK
{
       "ok": true
   }
Main.Kits - Recibir todas las kit
endpoint para recuperar todas las kit dentro de una tarjeta específica O las kit creadas por el/la usuario/a.
                                                * Es obligatorio pasar el encabezado Authorisation O el parámetro cardId, para recibir las kit
                                                * Si se recibe una solicitud con un encabezado Authorisation que contenga el authToken de un/a usuario/a en particular - se devolverán las kit creadas por ese/a usuario/a.
                                                * Si se recibe el parámetro de consulta cardId, se devolverán las kit relativas a la tarjeta.
                                                * Si no se pasa ninguno de los parámetros, se devolverá un error.
                                                * Cuando se pasan ambos parámetros, Authorization es la prioridad
get
/api/v1/kits
Header
Campo
	Tipo
	Descripción
	Authorization
opcional
	string
	Encabezado de autorización en formato Bearer {authToken}. Cuando se pasa - se devuelven todos las kit creadas por el/la usuario/a.
	                                                * Recepción de las kit creadas por el/la usuario/a
{
    "Authorization": "Bearer jknnFApafP4awfAIFfafam2fma"
}
Parámetro
Campo
	Tipo
	Descripción
	cardId
opcional
	number
	El id de la tarjeta en la tabla card_model. Cuando se pasa - se devuelven todos las kit incluidas en la tarjeta.
	                                                * Recibir las kit dentro de una tarjeta with id = 1
/api/v1/kits?cardId=1
                                                * Respuesta: Recibir las kit con éxito
HTTP/1.1 200 OK
[
    {
           "id": 1,
           "name": "Para pícnics",
           "productsList": [
               {
                   "id": 1,
                   "name": "Orange Juice - Cold-Pressed, No Added Sugar, Preservative Free",
                   "price": 149,
                   "weight": 473,
                   "units": "ml",
                   "quantity": 1
               },
               {
                   "id": 2,
                   "name": "Refresco Mountain Dew",
                   "price": 89,
                   "weight": 1,
                   "units": "l",
                   "quantity": 1
               },
               {
                   "id": 3,
                   "name": "Refresco Pepsi",
                   "price": 109,
                   "weight": 1,
                   "units": "l",
                   "quantity": 1
               },
               {
                   "id": 4,
                   "name": "Refresco Sprite",
                   "price": 79,
                   "weight": 900,
                   "units": "ml",
                   "quantity": 1
               },
               {
                   "id": 5,
                   "name": "Jugo Fruit Power: Lichi",
                   "price": 349,
                   "weight": 900,
                   "units": "ml",
                   "quantity": 1
               },
               {
                   "id": 6,
                   "name": "Baguette",
                   "price": 69,
                   "weight": 160,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 7,
                   "name": "Papas fritas: Saladas Clásicas",
                   "price": 119,
                   "weight": 150,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 8,
                   "name": "Papas fritas: Paprika",
                   "price": 199,
                   "weight": 150,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 9,
                   "name": "Papas Fritas: Chile",
                   "price": 209,
                   "weight": 100,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 10,
                   "name": "Pita",
                   "price": 99,
                   "weight": 300,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 11,
                   "name": "Pan multigrano",
                   "price": 149,
                   "weight": 400,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 12,
                   "name": "Pan de ajo",
                   "price": 75,
                   "weight": 225,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 13,
                   "name": "Mini chapata",
                   "price": 45,
                   "weight": 107,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 14,
                   "name": "Brioche",
                   "price": 79,
                   "weight": 79,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 15,
                   "name": "Salchichas vienesas",
                   "price": 179,
                   "weight": 350,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 16,
                   "name": "Salchichas de pollo",
                   "price": 173,
                   "weight": 200,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 17,
                   "name": "Chorizo",
                   "price": 269,
                   "weight": 420,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 18,
                   "name": "Salchichón",
                   "price": 175,
                   "weight": 464,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 19,
                   "name": "Salami",
                   "price": 99,
                   "weight": 190,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 20,
                   "name": "Bacon",
                   "price": 269,
                   "weight": 500,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 21,
                   "name": "Pastrami",
                   "price": 143,
                   "weight": 200,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 22,
                   "name": "Pepperoni",
                   "price": 329,
                   "weight": 500,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 23,
                   "name": "Anti-Bacterial Hand Sanitizer",
                   "price": 139,
                   "weight": 50,
                   "units": "ml",
                   "quantity": 1
               },
               {
                   "id": 24,
                   "name": "Paper Napkin - Large",
                   "price": 99,
                   "weight": 60,
                   "units": "pzas",
                   "quantity": 1
               },
               {
                   "id": 25,
                   "name": "Anti Bacterial Disinfectant Sanitising Wipes - Alcohol Free",
                   "price": 199,
                   "weight": 48,
                   "units": "pzas",
                   "quantity": 1
               },
               {
                   "id": 26,
                   "name": "SMART Mosquito Repellent",
                   "price": 349,
                   "weight": 100,
                   "units": "ml",
                   "quantity": 1
               },
               {
                   "id": 27,
                   "name": "Manzana verde",
                   "price": 169,
                   "weight": 500,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 28,
                   "name": "Orange",
                   "price": 146,
                   "weight": 500,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 29,
                   "name": "Cherry",
                   "price": 249,
                   "weight": 500,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 30,
                   "name": "Raspberry",
                   "price": 239,
                   "weight": 250,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 31,
                   "name": "Blackberry",
                   "price": 125,
                   "weight": 200,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 32,
                   "name": "Lima",
                   "price": 59,
                   "weight": 1,
                   "units": "pzas",
                   "quantity": 1
               },
               {
                   "id": 33,
                   "name": "Red Grapes",
                   "price": 269,
                   "weight": 500,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 34,
                   "name": "Green Grapes",
                   "price": 179,
                   "weight": 500,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 35,
                   "name": "Banana",
                   "price": 99,
                   "weight": 1000,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 36,
                   "name": "Pear",
                   "price": 199,
                   "weight": 650,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 37,
                   "name": "Blueberry",
                   "price": 199,
                   "weight": 125,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 38,
                   "name": "Pineapple",
                   "price": 385,
                   "weight": 1,
                   "units": "pzas",
                   "quantity": 1
               },
               {
                   "id": 39,
                   "name": "Pear",
                   "price": 145,
                   "weight": 800,
                   "units": "g",
                   "quantity": 1
               }
           ],
           "productsCount": 39
       },
    {
           "id": 2,
           "name": "Para películas y series",
           "productsList": [
               {
                   "id": 2,
                   "name": "Refresco Mountain Dew",
                   "price": 89,
                   "weight": 1,
                   "units": "l",
                   "quantity": 1
               },
               {
                   "id": 3,
                   "name": "Refresco Pepsi",
                   "price": 109,
                   "weight": 1,
                   "units": "l",
                   "quantity": 1
               },
               {
                   "id": 4,
                   "name": "Refresco Sprite",
                   "price": 79,
                   "weight": 900,
                   "units": "ml",
                   "quantity": 1
               },
               {
                   "id": 7,
                   "name": "Papas fritas: Saladas Clásicas",
                   "price": 119,
                   "weight": 150,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 8,
                   "name": "Papas fritas: Paprika",
                   "price": 199,
                   "weight": 150,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 9,
                   "name": "Papas Fritas: Chile",
                   "price": 209,
                   "weight": 100,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 43,
                   "name": "Classic Hummus Dip & Spread",
                   "price": 99,
                   "weight": 150,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 44,
                   "name": "Gourmet Palomitas Kernels",
                   "price": 109,
                   "weight": 60,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 45,
                   "name": "Caramel Palomitas",
                   "price": 99,
                   "weight": 150,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 46,
                   "name": "Fruit Beer Non-Alcoholic",
                   "price": 249,
                   "weight": 250,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 47,
                   "name": "Stella Artois Beer Non-Alcoholic",
                   "price": 179,
                   "weight": 60,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 48,
                   "name": "100% Belgian Dark Chocolate - with Apricot",
                   "price": 89,
                   "weight": 45,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 49,
                   "name": "100% Belgian Dark Chocolate - Raisins",
                   "price": 69,
                   "weight": 450,
                   "units": "ml",
                   "quantity": 1
               },
               {
                   "id": 50,
                   "name": "100% Belgian Milk Chocolate - Sea Salt",
                   "price": 109,
                   "weight": 450,
                   "units": "ml",
                   "quantity": 1
               },
               {
                   "id": 54,
                   "name": "Dairy Rich Chocolate Bar - Fruit & Nut",
                   "price": 139,
                   "weight": 100,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 55,
                   "name": "Peanut Butter Nutty Cookies",
                   "price": 119,
                   "weight": 97,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 56,
                   "name": "Cookies - Orange Splash",
                   "price": 89,
                   "weight": 85,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 57,
                   "name": "Choco Nut Cookies",
                   "price": 159,
                   "weight": 160,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 58,
                   "name": "Milk Cookies",
                   "price": 239,
                   "weight": 100,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 59,
                   "name": "Sandwich Biscuits",
                   "price": 119,
                   "weight": 100,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 60,
                   "name": "Chocobakes Choc Filled Cookies",
                   "price": 139,
                   "weight": 80,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 61,
                   "name": "Baguette French Recipe",
                   "price": 179,
                   "weight": 171,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 62,
                   "name": "Queso Croissant",
                   "price": 119,
                   "weight": 50,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 63,
                   "name": "French Almond Croissant",
                   "price": 119,
                   "weight": 228,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 64,
                   "name": "Chocolate Croissant",
                   "price": 149,
                   "weight": 168,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 65,
                   "name": "Smoked Salmon Croissant",
                   "price": 59,
                   "weight": 100,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 66,
                   "name": "Belgian Chocolate Cake Mix",
                   "price": 219,
                   "weight": 250,
                   "units": "g",
                   "quantity": 1
               }
           ],
           "productsCount": 27
       },
    {
           "id": 3,
           "name": "Sabores de París",
           "productsList": [
               {
                   "id": 54,
                   "name": "Dairy Rich Chocolate Bar - Fruit & Nut",
                   "price": 139,
                   "weight": 100,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 58,
                   "name": "Milk Cookies",
                   "price": 239,
                   "weight": 100,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 67,
                   "name": "Baguette French Recipe",
                   "price": 89,
                   "weight": 200,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 68,
                   "name": "Queso Croissant",
                   "price": 79,
                   "weight": 75,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 69,
                   "name": "French Almond Croissant",
                   "price": 129,
                   "weight": 120,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 70,
                   "name": "Chocolate Croissant",
                   "price": 104,
                   "weight": 96,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 71,
                   "name": "Smoked Salmon Croissant",
                   "price": 119,
                   "weight": 90,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 72,
                   "name": "Belgian Chocolate Cake Mix",
                   "price": 359,
                   "weight": 125,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 73,
                   "name": "Queso para untar: Queso crema",
                   "price": 79,
                   "weight": 130,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 74,
                   "name": "Queso Slices",
                   "price": 239,
                   "weight": 400,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 75,
                   "name": "Queso Spread - Roasted Garlic",
                   "price": 129,
                   "weight": 200,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 76,
                   "name": "Spicy Queso Straw",
                   "price": 229,
                   "weight": 250,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 77,
                   "name": "Rebanadas de queso procesado",
                   "price": 220,
                   "weight": 250,
                   "units": "",
                   "quantity": 1
               },
               {
                   "id": 78,
                   "name": "Cubos de queso procesado",
                   "price": 399,
                   "weight": 200,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 79,
                   "name": "Soyabean Tempeh Cubes",
                   "price": 209,
                   "weight": 300,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 82,
                   "name": "Center Filled Dark Chocolate Cookies",
                   "price": 129,
                   "weight": 100,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 83,
                   "name": "Enrobed Cinnamon Milk Chocolate Dipped Cookies",
                   "price": 225,
                   "weight": 100,
                   "units": "g",
                   "quantity": 1
               },
               {
                   "id": 84,
                   "name": "Oreo & Crème Frozen Dessert",
                   "price": 339,
                   "weight": 300,
                   "units": "ml",
                   "quantity": 1
               },
               {
                   "id": 85,
                   "name": "Chocorich Eclairs Chocolate - Assorted",
                   "price": 429,
                   "weight": 200,
                   "units": "g",
                   "quantity": 1
               }
           ],
           "productsCount": 19
       }
    ]
                                                * Error: No se ha transmitido ninguno de los parámetros
                                                * Error: No se han encontrado kits coincidentes
HTTP/1.1 400 Bad request.
{
       "code": 400,
       "message": "No se han aprobado todos los parámetros requeridos"
   }
Main.Kits - Recibir una kit por el nombre
get
/api/v1/kits/search
Parámetro
Campo
	Tipo
	Descripción
	name
	string
	name de la kit en la tabla kit_model.
	                                                * Recibir una kit con un nombre "Sabores de París"
/api/v1/kits/search?name=Sabores%20de%20París
                                                * Respuesta: El conjunto ha sido recibido con éxito.
HTTP/1.1 200 OK
{
       "id": 3,
       "name": "Sabores de París",
       "productsList": [
           {
               "id": 54,
               "name": "Dairy Rich Chocolate Bar - Fruit & Nut",
               "price": 139,
               "weight": 100,
               "units": "g",
               "quantity": 6
           },
           {
               "id": 58,
               "name": "Milk Cookies",
               "price": 239,
               "weight": 100,
               "units": "g"
               "quantity": 8
           },
           {
               "id": 67,
               "name": "Baguette French Recipe",
               "price": 89,
               "weight": 200,
               "units": "g",
               "quantity": 4
           },
           {
               "id": 68,
               "name": "Queso Croissant",
               "price": 79,
               "weight": 75,
               "units": "g",
               "quantity": 1
           },
           {
               "id": 69,
               "name": "French Almond Croissant",
               "price": 129,
               "weight": 120,
               "units": "g",
               "quantity": 7
           },
           {
               "id": 70,
               "name": "Chocolate Croissant",
               "price": 104,
               "weight": 96,
               "units": "g",
               "quantity": 1
           },
           {
               "id": 71,
               "name": "Smoked Salmon Croissant",
               "price": 119,
               "weight": 90,
               "units": "g",
               "quantity": 1
           },
           {
               "id": 72,
               "name": "Belgian Chocolate Cake Mix",
               "price": 359,
               "weight": 125,
               "units": "g",
               "quantity": 1
           },
           {
               "id": 73,
               "name": "Queso para untar: Queso crema",
               "price": 79,
               "weight": 130,
               "units": "g",
               "quantity": 1
           },
           {
               "id": 74,
               "name": "Queso Slices",
               "price": 239,
               "weight": 400,
               "units": "g",
               "quantity": 1
           },
           {
               "id": 75,
               "name": "Queso Spread - Roasted Garlic",
               "price": 129,
               "weight": 200,
               "units": "g",
               "quantity": 1
           },
           {
               "id": 76,
               "name": "Spicy Queso Straw",
               "price": 229,
               "weight": 250,
               "units": "g",
               "quantity": 1
           },
           {
               "id": 77,
               "name": "Rebanadas de queso procesado",
               "price": 220,
               "weight": 250,
               "units": "g",
               "quantity": 1
           },
           {
               "id": 78,
               "name": "Cubos de queso procesado",
               "price": 399,
               "weight": 200,
               "units": "g",
               "quantity": 1
           },
           {
               "id": 79,
               "name": "Soyabean Tempeh Cubes",
               "price": 209,
               "weight": 300,
               "units": "g",
               "quantity": 1
           },
           {
               "id": 82,
               "name": "Center Filled Dark Chocolate Cookies",
               "price": 129,
               "weight": 100,
               "units": "g",
               "quantity": 1
           },
           {
               "id": 83,
               "name": "Enrobed Cinnamon Milk Chocolate Dipped Cookies",
               "price": 225,
               "weight": 100,
               "units": "g",
               "quantity": 1
           },
           {
               "id": 84,
               "name": "Oreo & Crème Frozen Dessert",
               "price": 339,
               "weight": 300,
               "units": "ml",
               "quantity": 1
           },
           {
               "id": 85,
               "name": "Chocorich Eclairs Chocolate - Assorted",
               "price": 429,
               "weight": 200,
               "units": "g",
               "quantity": 1
           }
       ],
       "productsCount": 19
   }
                                                * Error: No se han encontrado kits coincidentes
HTTP/1.1 404 Not found.
{
       "code": 404,
       "message": "Not found"
   }
Main.Basket
Main.Basket - Añadir productos a la cesta
put
/api/v1/orders/:id
                                                * Ejemplos de encabezados
{
    "Content-Type": "application/json"
}
Parámetro
Campo
	Tipo
	Descripción
	id
	number
	id de la cesta en la tabla order_model. Se pasa en la URL
	productsList
	Array
	Una lista de productos que se agregarán al cesta. La lista contiene los ID de los artículos y sus cantidades. Debe enviarse en el cuerpo de la solicitud.
	                                                * Añadir productos a la cesta
{
    "productsList": [
        {
            "id": 1,
            "quantity": 4
        },
        {
            "id": 5,
            "quantity": 2
        },
        {
            "id": 3,
            "quantity": 1
        },
        {
            "id": 4,
            "quantity": 1
        }
    ]
}
                                                * Respuesta: Los artículos se han añadido a la cesta con éxito
HTTP/1.1 200 OK
 {
"productsList": [
    {
        "id": 1,
        "quantity": 10
    },
    {
        "id": 5,
        "quantity": 10
    },
    {
        "id": 3,
        "quantity": 9
    },
    {
        "id": 4,
        "quantity": 5
    }
],
        "status": 0,
        "deliveryPriceOur": 30,
        "deliveryTime": "25~30",
        "courierService": "Fast Delivery",
        "deliveryPrice": 0,
        "wareHouse": "Fresh food",
        "userId": 1,
        "id": 5,
        "productsCost": 75,
        "finalCCost": 174
    }
                                                * Error: Cesta no encontrada
                                                * Error: No hay un almacén para procesar tu pedido
HTTP/1.1 404 Not found.
{
       "code": 404,
       "message": "Not found"
Main.Basket - Crear una cesta
post
/api/v1/orders
                                                * Ejemplos de encabezados
{
    "Content-Type": "application/json"
}
Parámetro
Campo
	Tipo
	Descripción
	productsList
	Array
	Una lista de productos que se agregarán al cesta. La lista contiene los ID de los artículos y sus cantidades. Debe enviarse en el cuerpo de la solicitud.
	deliveryTime
opcional
	number
	Plazo de entrega previsto. Si no se pasa ningún valor, el sistema utiliza la hora actual
	                                                * Crear una cesta
{
    "productsList": [
        {
            "id": 1,
            "quantity": 2
        },
        {
            "id": 5,
            "quantity": 2
        },
        {
            "id": 3,
            "quantity": 1
        }
    ]
}
                                                * Respuesta: La cesta fue creada con éxito
HTTP/1.1 200 OK
{
       "productsList": [
           {
               "id": 1,
               "quantity": 2
           },
           {
               "id": 5,
               "quantity": 2
           },
           {
               "id": 3,
               "quantity": 1
           }
       ],
       "status": 0,
       "deliveryPriceOur": 30,
       "deliveryTime": "25~30",
       "courierService": "Fast Delivery",
       "deliveryPrice": 99,
       "wareHouse": "Fresh food",
       "userId": 1,
       "id": 5,
       "productsCost": 75,
       "finalCCost": 174
   }
                                                * Error: No se han aprobado todos los parámetros requeridos
                                                * Error: No hay un almacén para procesar tu pedido
HTTP/1.1 400 Bad request.
{
       "code": 400,
       "message": "No se han aprobado todos los parámetros requeridos"
   }
Main.Basket - Eliminar la cesta
delete
/api/v1/orders/:id
Parámetro
Campo
	Tipo
	Descripción
	id
	number
	id de la cesta en la tabla order_model. Se pasa en la URL
	                                                * Respuesta: Eliminar una cesta con éxito
HTTP/1.1 200 OK
{
       "ok": true
   }
Main.Basket - Hacer el pedido
put
/api/v1/orders/:id/complete
Parámetro
Campo
	Tipo
	Descripción
	id
	number
	id de la cesta en la tabla order_model. Se pasa en la URL
	                                                * Respuesta: Los artículos se han añadido a la cesta con éxito
HTTP/1.1 200 OK
{
       "ok": true,
   }
                                                * Error: El authToken no ha sido transmitido
HTTP/1.1 401 Unauthorized.
{
       "code": 401,
       "message": "No autorizado",
   }
Main.Basket - Recibir los productos de la cesta
get
/api/v1/orders/:id
Header
Campo
	Tipo
	Descripción
	Authorization
opcional
	string
	Encabezado de autorización en formato Bearer {authToken}.
	                                                * Ejemplo de autorización
{
    "Authorization": "Bearer jknnFApafP4awfAIFfafam2fma"
}
Parámetro
Campo
	Tipo
	Descripción
	id
	string
	id de la cesta en la tabla order_model. Se pasa por el parámetro de URL
	                                                * Recibir la cesta
/api/v1/orders/6
                                                * Respuesta: Los productos de la cesta recibidos con éxito
HTTP/1.1 200 OK
[
    {
           "id": 1,
           "name": "Orange Juice - Cold-Pressed, No Added Sugar, Preservative Free",
           "price": 149,
           "weight": 473,
           "units": "ml",
           "quantity": 3
       },
    {
           "id": 4,
           "name": "Refresco Sprite",
           "price": 79,
           "weight": 900,
           "units": "ml",
           "quantity": 4
       }
    ]
                                                * Error: El authToken no ha sido transmitido
                                                * Error: Cesta no encontrada
HTTP/1.1 401 Unauthorized.
{
       "code": 401,
       "message": "No autorizado",
   }
Main.Orders
Main.Orders - Recepción de pedidos de los usuarios
get
/api/v1/orders
Header
Campo
	Tipo
	Descripción
	Authorization
opcional
	string
	Encabezado de autorización en formato Bearer {authToken}.
	                                                * Recibir los pedidos de los/las usuarios/as
{
    "Authorization": "Bearer jknnFApafP4awfAIFfafam2fma"
}
                                                * Respuesta: Todos los pedidos del/de la usuario/a recibidos con éxito
HTTP/1.1 200 OK
[
    {
           "id": 6,
           "userId": 1,
           "productsList": [
               {
                   "id": 1,
                   "quantity": 2
               },
               {
                   "id": 5,
                   "quantity": 2
               },
               {
                   "id": 3,
                   "quantity": 1
               }
           ],
           "deliveryPrice": 0,
           "deliveryPriceOur": 30,
           "deliveryTime": "25~30",
           "wareHouse": "Fresh food",
           "courierService": "Fast Delivery",
           "status": 1
       }
    ]
                                                * Error: El authToken no ha sido transmitido
HTTP/1.1 401 Unauthorized.
{
       "code": 401,
       "message": "    ",
   }
Utils
Utils - Logs de mensajeros/almacenes del servidor
Se trata de una herramienta para obtener las últimas líneas del log mixto de todos los servidores secundarios (mensajeros y almacenes). The count parameter means the number of lines to be read and returned in the response
get
/api/logs/secondary
Parámetro
Campo
	Tipo
	Descripción
	count
opcional
	number
	Número de líneas desde el final
Valor por defecto: 50
	                                                * Obtener los últimos 50 registros
                                                * Obtener los últimos 100 registros
/api/logs/secondary
                                                * Respuesta: Últimos registros del log
2020-08-26T16:07:33.017Z [INFO] [Warehouse][food-city]: Server is listening at port 4022
2020-08-26T16:08:01.324Z [DEBUG] [Warehouse][everything-you-need]: [Request] - ::ffff:127.0.0.1 POST:/everything-you-need/v1/calculate - HTTP/1.1 - application/json - {"deliveryTime":10,"products":[{"id":1,"quantity":1},{"id":4,"quantity":1},{"id":44,"quantity":1}]}
2020-08-26T16:08:01.324Z [DEBUG] [Warehouse][fresh-food]: [Request] - ::ffff:127.0.0.1 POST:/fresh-food/v2.0.1/ct - HTTP/1.1 - application/json - {"deliveryTime":10,"products":[{"id":1,"quantity":1},{"id":4,"quantity":1},{"id":44,"quantity":1}]}
2020-08-26T16:08:01.324Z [DEBUG] [Warehouse][big-world]: [SOAP Client] received <?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  xmlns:tns="WebServices.WarehouseWsdl"><soap:Body><tns:checkSupply><tns:deliveryTime>10</tns:deliveryTime><tns:products><tns:products><id>1</id><quantity>1</quantity></tns:products><tns:products><id>4</id><quantity>1</quantity></tns:products><tns:products><id>44</id><quantity>1</quantity></tns:products></tns:products></tns:checkSupply></soap:Body></soap:Envelope>
2020-08-26T16:08:01.361Z [DEBUG] [Warehouse][food-city]: [Request] - ::ffff:127.0.0.1 POST:/food-city/calculate.xml - HTTP/1.1 - application/xml - <InputModel><deliveryTime>10</deliveryTime><product id="1" quantity="1"/><product id="4" quantity="1"/><product id="44" quantity="1"/></InputModel>
2020-08-26T16:39:17.168Z [DEBUG] [Warehouse][big-world]: [SOAP Client] received <?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  xmlns:tns="WebServices.WarehouseWsdl"><soap:Body><tns:checkSupply><tns:deliveryTime>10</tns:deliveryTime><tns:products><tns:products><id>1</id><quantity>1</quantity></tns:products><tns:products><id>4</id><quantity>1</quantity></tns:products><tns:products><id>44</id><quantity>1</quantity></tns:products></tns:products></tns:checkSupply></soap:Body></soap:Envelope>
2020-08-26T16:39:17.168Z [DEBUG] [Warehouse][fresh-food]: [Request] - ::ffff:127.0.0.1 POST:/fresh-food/v2.0.1/ct - HTTP/1.1 - application/json - {"deliveryTime":10,"products":[{"id":1,"quantity":1},{"id":4,"quantity":1},{"id":44,"quantity":1}]}
2020-08-26T16:39:17.170Z [DEBUG] [Warehouse][everything-you-need]: [Request] - ::ffff:127.0.0.1 POST:/everything-you-need/v1/calculate - HTTP/1.1 - application/json - {"deliveryTime":10,"products":[{"id":1,"quantity":1},{"id":4,"quantity":1},{"id":44,"quantity":1}]}
2020-08-26T16:39:17.173Z [DEBUG] [Warehouse][food-city]: [Request] - ::ffff:127.0.0.1 POST:/food-city/calculate.xml - HTTP/1.1 - application/xml - <InputModel><deliveryTime>10</deliveryTime><product id="1" quantity="1"/><product id="4" quantity="1"/><product id="44" quantity="1"/></InputModel>
2020-08-26T16:39:21.398Z [DEBUG] [Courier][food-service]: [SOAP Client] received <?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  xmlns:tns="WebServices.CourierWsdl"><soap:Body><Request xmlns="WebServices.CourierWsdl"><productsCount>3</productsCount><productsWeight>1.433</productsWeight><deliveryTime>7</deliveryTime></Request></soap:Body></soap:Envelope>
2020-08-26T16:39:21.453Z [DEBUG] [Courier][fast-delivery]: [Request] - ::ffff:127.0.0.1 POST:/fast-delivery/v3.1.1/calculate-delivery.xml - HTTP/1.1 - application/xml - {"InputModel":{"deliveryTime":["7"],"productsWeight":["1.433"],"productsCount":["3"]}}
2020-08-26T16:39:21.481Z [DEBUG] [Courier][order-and-go]: [Request] - ::ffff:127.0.0.1 POST:/order-and-go/v1/delivery - HTTP/1.1 - application/json - {"productsCount":3,"productsWeight":1.433,"deliveryTime":7}
2020-08-26T16:39:21.489Z [DEBUG] [Courier][speedy]: [Request] - ::ffff:127.0.0.1 POST:/speedy/v1/calculate - HTTP/1.1 - application/json - {"productsCount":3,"productsWeight":1.433,"deliveryTime":7}
Utils - Logs del servidor principal
Esta es una herramienta para obtener las últimas líneas en el registro del servidor principal. El parámetro count indica el número de líneas que se leerán y se devolverán a Response
get
/api/logs/main
Parámetro
Campo
	Tipo
	Descripción
	count
opcional
	number
	Número de líneas desde el final
Valor por defecto: 50
	                                                * Obtener los últimos 50 registros
                                                * Obtener los últimos 100 registros
/api/logs/main
                                                * Respuesta: Últimos registros del log
2020-08-26T16:38:31.489Z [INFO] [Main]: Server is listening at port 4000
2020-08-26T16:38:31.500Z [INFO] [Main]: [SOAP Client] Soap is listening at /api/wsdl
2020-08-26T16:38:31.532Z [DEBUG] [Main]: [SOAP Client] TRAIN client is initialized
2020-08-26T16:38:31.564Z [DEBUG] [Main]: [SOAP Client] WORLD client is initialized
2020-08-26T16:38:31.609Z [INFO] [Main]: [PostgreSQL] PostgreSQL is initialized
2020-08-26T16:38:35.057Z [DEBUG] [Main]: [Request] - ::1 GET:/api/logs/main - HTTP/1.1 -  -
2020-08-26T16:39:17.106Z [DEBUG] [Main]: [Request] - ::1 POST:/api/v1/warehouses/amount?dataType=xml - HTTP/1.1 - application/xml - <root><id>1</id><id>4</id><id>44</id></root>
2020-08-26T16:39:21.358Z [DEBUG] [Main]: [Request] - ::1 POST:/api/v1/couriers/check - HTTP/1.1 - application/json - {"ids":[1,4,44],"deliveryTime":7}
2020-08-26T16:39:36.767Z [DEBUG] [Main]: [Request] - ::1 GET:/api/v1/orders - HTTP/1.1 - application/json - {"productsList":"1,4"}
2020-08-26T16:39:47.908Z [DEBUG] [Main]: [Request] - ::1 GET:/api/logs/main - HTTP/1.1 -  -
2020-08-26T16:07:32.123Z [ERROR] [Main]: Unexpected error:
2020-08-26T16:07:32.127Z [ERROR] [Main]:          {"message":"request to http://localhost:4022/food-city/calculate.xml failed, reason: connect ECONNREFUSED 127.0.0.1:4022","type":"system","errno":"ECONNREFUSED","code":"ECONNREFUSED","stack":"FetchError: request to http://localhost:4022/food-city/calculate.xml failed, reason: connect ECONNREFUSED 127.0.0.1:4022\n    at ClientRequest.<anonymous> (/Users/vladimirlevin/Desktop/Own/ez-lavka/packages/main/node_modules/node-fetch/lib/index.js:1455:11)\n    at ClientRequest.emit (events.js:198:13)\n    at ClientRequest.EventEmitter.emit (domain.js:448:20)\n    at Socket.socketErrorListener (_http_client.js:401:9)\n    at Socket.emit (events.js:198:13)\n    at Socket.EventEmitter.emit (domain.js:448:20)\n    at emitErrorNT (internal/streams/destroy.js:91:8)\n    at emitErrorAndCloseNT (internal/streams/destroy.js:59:3)\n    at process._tickCallback (internal/process/next_tick.js:63:19)"}
2020-08-26T16:07:32.131Z [ERROR] [Main]: Unexpected error:
2020-08-26T16:07:32.162Z [ERROR] [Main]:          {"stack":"RangeError [ERR_HTTP_INVALID_STATUS_CODE]: Invalid status code: ECONNREFUSED\n    at ServerResponse.writeHead (_http_server.js:211:11)\n    at ServerResponse._implicitHeader (_http_server.js:202:8)\n    at write_ (_http_outgoing.js:585:9)\n    at ServerResponse.end (_http_outgoing.js:702:5)\n    at ServerResponse.send (/Users/vladimirlevin/Desktop/Own/ez-lavka/packages/main/node_modules/express/lib/response.js:221:10)\n    at ServerResponse.json (/Users/vladimirlevin/Desktop/Own/ez-lavka/packages/main/node_modules/express/lib/response.js:267:15)\n    at app.use (/Users/vladimirlevin/Desktop/Own/ez-lavka/packages/main/src/app.ts:77:14)\n    at Layer.handle_error (/Users/vladimirlevin/Desktop/Own/ez-lavka/packages/main/node_modules/express/lib/router/layer.js:71:5)\n    at trim_prefix (/Users/vladimirlevin/Desktop/Own/ez-lavka/packages/main/node_modules/express/lib/router/index.js:315:13)\n    at /Users/vladimirlevin/Desktop/Own/ez-lavka/packages/main/node_modules/express/lib/router/index.js:284:7\n    at Function.process_params (/Users/vladimirlevin/Desktop/Own/ez-lavka/packages/main/node_modules/express/lib/router/index.js:335:12)\n    at next (/Users/vladimirlevin/Desktop/Own/ez-lavka/packages/main/node_modules/express/lib/router/index.js:275:10)\n    at ServiceContext.next (/Users/vladimirlevin/Desktop/Own/ez-lavka/packages/main/node_modules/express/lib/router/route.js:127:14)\n    at ServiceInvoker.<anonymous> (/Users/vladimirlevin/Desktop/Own/ez-lavka/packages/main/node_modules/typescript-rest/src/server/service-invoker.ts:37:21)\n    at Generator.throw (<anonymous>)\n    at rejected (/Users/vladimirlevin/Desktop/Own/ez-lavka/packages/main/node_modules/typescript-rest/dist/server/service-invoker.js:6:65)\n    at process._tickCallback (internal/process/next_tick.js:68:7)","message":"Invalid status code: ECONNREFUSED"}
2020-08-26T16:08:01.311Z [DEBUG] [Main]: [Request] - ::1 POST:/api/v1/warehouses/amount - HTTP/1.1 - application/json - {"ids":[1,4,44]}
Utils - Recuperar información de la tabla de base de datos
get
/api/db/resources/{table_name}.csv
Parámetro
Campo
	Tipo
	Descripción
	table_name
	string
	El nombre de la tabla en la base de datos. Se pasa en la URL.
	                                                * Recibir la tabla product_model
                                                * Recibir la tabla kit_model
/api/db/resources/product_model.csv
                                                * Respuesta: Archivo con el contenido de la tabla product_model
id,name,price,weight,units,categoryId,
1,Orange Juice - Cold-Pressed, No Added Sugar, Preservative Free,149,473,ml,1
2,Refresco Mountain Dew,89,1,l,1
3,Refresco Pepsi,109,1,l,1
4,Refresco Sprite,79,900,ml,1
5,Jugo Fruit Power: Lichi,349,900,ml,1