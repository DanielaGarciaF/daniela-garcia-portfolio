<div align="center">

#  Ingeniería y Calidad de Software (ICSW) – Proyecto UTN-FRC  
### Trabajo Práctico – TDD & Testing Caja Negra

[![ICSW](https://img.shields.io/badge/Materia-ICSW-blue?logo=book&logoColor=white)]()
[![UTN](https://img.shields.io/badge/Universidad-UTN_FRC-black?logo=academia&logoColor=white)]()
[![TDD](https://img.shields.io/badge/Metodología-TDD-red?logo=pytest&logoColor=white)]()
[![Testing](https://img.shields.io/badge/Testing-Caja%20Negra-green?logo=checkmarx&logoColor=white)]()

</div>

---

## 🎓 Sobre la materia: Ingeniería y Calidad de Software (ICSW)

Este proyecto fue realizado en la asignatura **Ingeniería y Calidad de Software (ICSW)**, perteneciente al 4to nivel de la carrera **Ingeniería en Sistemas de Información** en la **Universidad Tecnológica Nacional – Facultad Regional Córdoba (UTN-FRC)**.

La materia forma parte del Área de Desarrollo de Software y se orienta a:

- Desarrollar disciplinas de **gestión** y **soporte** del proceso de software.  
- Aplicar prácticas para construir **software de calidad**, manteniendo integridad, confiabilidad y satisfacción del usuario.  
- Entender el ciclo completo del desarrollo desde el punto de vista de la calidad: requerimientos, análisis, diseño, pruebas y mantenimiento.

###  Objetivos formativos de la materia
- Aplicar métodos, técnicas y herramientas para asegurar la calidad del software.  
- Comprender disciplinas como:  
  **Gestión de configuración**, **modelos de calidad**, **verificación y validación**, **métricas**, **estimaciones**, **auditorías** y **despliegue**.  
- Desarrollar habilidades para administrar proyectos de software y garantizar calidad del producto final.  
- Formar profesionales capaces de **analizar, diseñar y administrar** sistemas de información con pensamiento crítico.

---

#  Proyecto 1 – TDD (Trabajo Práctico 6)

## 🔧 Desarrollo dirigido por pruebas (TDD)  
Unidad: Aseguramiento de Calidad de Proceso y Producto – Unidad 4

Este trabajo consistió en implementar una funcionalidad aplicando estrictamente el ciclo:

1. **RED** → escribir una prueba que falle  
2. **GREEN** → implementar la mínima solución para pasar la prueba  
3. **REFACTOR** → mejorar el código manteniendo todas las pruebas verdes  

---

##  User Story implementada (nuestro grupo)  
### **“Comprar entradas” – EcoHarmony Park**

**COMO** visitante  
**QUIERO** comprar una entrada  
**PARA** asegurar mi visita al parque

###  Criterios de aceptación
- Indicar fecha de visita válida (hoy o futura).  
- Cantidad de entradas ≤ 10.  
- Ingresar edad de cada visitante y tipo de pase (VIP o regular).  
- Seleccionar forma de pago (efectivo o tarjeta → Mercado Pago).  
- Enviar confirmación por correo electrónico.  
- Solo disponible para usuarios registrados.  
- Validar que el parque esté abierto en la fecha seleccionada.  
- Al finalizar, mostrar resumen de compra (cantidad + fecha).

###  Pruebas de usuario (resumen)
**Pasan:**
- Compra válida con fecha disponible, menos de 10 entradas, pago con tarjeta, pase correcto y mail de confirmación.

**Fallan:**
- Sin seleccionar forma de pago.  
- Fecha en un día donde el parque está cerrado.  
- Más de 10 entradas.

---

#  Proyecto 2 – Testing Caja Negra  
### Trabajo Práctico 11 – Ejecución de casos de prueba

Unidad: Aseguramiento de Calidad de Proceso y Producto – Unidad 4

El objetivo fue ejecutar los casos de prueba diseñados previamente, reportar defectos y evaluar la calidad del producto generado por otro grupo.

###  Actividad asignada para testear  
Nuestro grupo **probó la User Story implementada por otro equipo**:

### **“Inscribirme a actividad”**

**COMO** visitante  
**QUIERO** inscribirme a una actividad  
**PARA** reservar mi lugar  

###  Criterios de aceptación
- Selección de actividad disponible: Tirolesa, Safari, Palestra o Jardinería.  
- Cupones y horarios disponibles.  
- Cantidad de personas.  
- Datos completos por visitante: nombre, DNI, edad y talla si aplica.  
- Aceptar términos y condiciones específicos.

###  Pruebas realizadas (resumen)
**Pasan:**
- Actividad con cupo + horario válido + datos completos + aceptación de términos.  
- Actividad sin requerir talle y no ingresarlo.

**Fallan:**
- Inscripción a actividad sin cupo.  
- No ingresar talle cuando es obligatorio.  
- No aceptar términos.  
- Seleccionar horario en el que el parque está cerrado.

###  Entregables del TP
- Casos de prueba diseñados en base a clases de equivalencia.  
- Ejecución completa de los casos.  
- Planilla con **defectos encontrados** (DeliverEat_Template_Caso_De_Prueba_Defectos.xlsx).

---

#  Tecnologías y herramientas utilizadas

[![Java](https://img.shields.io/badge/Java-ED8B00?logo=java&logoColor=white)]()
[![JUnit](https://img.shields.io/badge/Testing-JUnit5-green?logo=junit5&logoColor=white)]()
[![Git](https://img.shields.io/badge/Git-Versionado-F05032?logo=git&logoColor=white)]()
[![Agile](https://img.shields.io/badge/Metodología-Ágil-blue?logo=scrumalliance&logoColor=white)]()
[![TDD](https://img.shields.io/badge/TDD-Red--Green--Refactor-red?logo=testinglibrary&logoColor=white)]()

---

<div align="center">

###  Este proyecto representa el enfoque real de ICSW:  
**Diseñar, implementar y validar software con calidad desde el origen.**

</div>
