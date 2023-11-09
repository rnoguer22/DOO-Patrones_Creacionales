# DOO-Patrones_Creacionales

---

[Pincha aqui para acceder al link del repositorio](https://github.com/rnoguer22/DOO-Patrones_Creacionales.git)

---

## Justificacion Patron Builder en el gestor de una pizzeria

En una pizzeria, la construccion de una pizza puede ser mas complejo de lo que parece, tenemos multitud de masas, ingredientes, ect. que intervienen en la construccion de la pizza. De esta manera podemos construir nuestra pizza paso a paso, personalizada a nuestro gusto. En resumen, nos proporciona la flexibilidad y robustez para construir pizzas con rigurosas configuraciones.

EL patron builder tiene como grandes ventajas que podemos añadir ingredientes facilmente, creando metodos nuevos para no afectar nuestro codigo actual. A su vez, podemos crear variantes de pizza sin modificar el codigo del director o de otros builder ya existentes, lo que facilita la introduccion de mayor opciones en el menu. Por otra parte, otra de las muchas ventajas del builder es que podmos modificar la construccion de la pizza facilmente aun habiendose creado anteriormente.

En cuanto a la robustez de dicho patron, este es de facil mantenimiento, ya que cada aspecto de construccion de la pizza esta encapsulado en su propio builder, por lo que si queremos realizar alguna modificacion, no afectamos a otras partes del codigo. Otro aspecto de robustez es que con este patron se reduce en gran medida el codigo duplicado, es decir, ganamos en cuanto a reutilizacion de codigo se refiere.

Comparando un patron builder con otros enfoques, este patron supera a un simple constructor con muchos parametros al incluir una estructura mas organizada, mejorando la legibilidad del codigo.

En resumen, el patron builder es una eleccion solida para el gestor de una pizzeria debido a la complejidad y variabilidad inherentes en la construccion de pizzas. Proporciona un diseño robusto y adaptable que facilita la gestion de diferentes tipos de pizzas y permite la incorporacion de nuevas caracteristicas y opciones sin comprometer la integridad del sistema.
