<div align="center">

#  Simulación – UTN-FRC  
### Trabajo Práctico Final – Simulación de un Polideportivo

[![Simulación](https://img.shields.io/badge/Materia-Simulación-blue?logo=chart-line&logoColor=white)]()
[![UTN](https://img.shields.io/badge/Universidad-UTN_FRC-black?logo=academia&logoColor=white)]()
[![Python](https://img.shields.io/badge/Lenguaje-Python-yellow?logo=python&logoColor=white)]()
[![Monte Carlo](https://img.shields.io/badge/Método-Monte%20Carlo-green?logo=shuffle&logoColor=white)]()

</div>

---

##  Sobre la materia: Simulación

Este proyecto fue desarrollado en el marco de la asignatura **Simulación**, correspondiente a la carrera **Ingeniería en Sistemas de Información** de la **Universidad Tecnológica Nacional – Facultad Regional Córdoba (UTN-FRC)**.

La materia tiene como objetivo principal el **modelado y análisis de sistemas reales complejos**, donde la resolución analítica resulta inviable o poco representativa, utilizando técnicas de **simulación discreta** y **métodos Monte Carlo**.

### Objetivos formativos de la materia
- Modelar sistemas reales mediante **eventos discretos**.
- Incorporar **variables aleatorias** y distribuciones de probabilidad.
- Analizar indicadores de desempeño del sistema.
- Evaluar alternativas de operación sin intervenir el sistema real.
- Comprender el impacto de la **variabilidad** y la **aleatoriedad** en los procesos.

---

##  Objetivo del trabajo práctico

El objetivo del trabajo es **simular el funcionamiento de un polideportivo** en el que ingresan grupos de deportistas para practicar distintas disciplinas, con el fin de:

> **Determinar el tiempo promedio de espera de los grupos, discriminado por tipo de disciplina deportiva.**

Para ello se construye un **modelo de simulación de eventos discretos**, que representa el comportamiento del sistema a lo largo del tiempo, considerando reglas de prioridad, restricciones operativas y tiempos aleatorios.

---

##  Dominio del problema: Polideportivo

### Disciplinas deportivas
El sistema contempla la llegada de grupos para practicar tres disciplinas:

-  **Fútbol**
-  **Hand Ball**
-  **Basket Ball**

El polideportivo cuenta con un **predio único de piso sintético**, donde se encuentran marcadas las canchas correspondientes a las tres disciplinas.

---

### Reglas operativas del sistema

- Solo se puede practicar **una disciplina por vez** en el predio.
- **Excepción Basket Ball**:
  - Cuando se practica Basket, el predio permite que **dos canchas operen simultáneamente**.
- Los grupos ingresan:
  - **De a uno**
  - En **orden de llegada**
- Existen **prioridades de acceso**:
  - Un grupo de Basket puede ingresar si:
    - Hay otro grupo de Basket esperando, o
    - Es el único grupo de Basket y **no hay grupos de otras disciplinas esperando**.
  - En caso contrario, **Fútbol y Hand Ball tienen prioridad**.
- Cada vez que se cambia de disciplina:
  - Se debe **acondicionar la cancha**
  - Tiempo de acondicionamiento: **10 minutos**

---

##  Variables aleatorias del modelo

Las llegadas y los tiempos de ocupación de cancha se modelan mediante distribuciones probabilísticas:

| Disciplina | Llegadas | Ocupación de cancha |
|-----------|---------|---------------------|
| Fútbol | Exponencial Negativa (media 10 hs) | Normal (90 ± 10 min) |
| Hand Ball | Normal (12 ± 2 hs) | Normal (80 ± 20 min) |
| Basket Ball | Normal (8 ± 2 hs) | Normal (100 ± 30 min) |

Estas distribuciones se generan mediante **números pseudoaleatorios**, aplicando técnicas de simulación Monte Carlo.

---

##  Enfoque de simulación

- **Tipo de simulación**: Simulación de **eventos discretos**
- **Método**: Monte Carlo
- **Estado del sistema**:
  - Reloj de simulación
  - Evento actual
  - Disciplina en uso
  - Estado de las canchas
  - Colas por disciplina
  - Equipos en espera y en servicio
- **Eventos principales**:
  - Llegada de grupo
  - Inicio de ocupación de cancha
  - Fin de ocupación
  - Cambio de disciplina
  - Fin de acondicionamiento

---

##  Resultados esperados

La simulación permite obtener:

- Tiempo promedio de espera para:
  - Grupos de **Fútbol**
  - Grupos de **Hand Ball**
  - Grupos de **Basket Ball**
- Evaluación del impacto de:
  - Prioridades de atención
  - Capacidad especial del Basket
  - Tiempos de acondicionamiento
- Análisis del comportamiento del sistema a largo plazo mediante grandes cantidades de iteraciones.

---

##  Implementación

- Lenguaje: **Python**
- Modelo vectorial de simulación
- Registro de estados en un **vector de resultados**
- Exportación opcional de resultados a **CSV**
- Visualización parcial de trazabilidad para validación del modelo

El diseño permite:
- Ajustar parámetros (medias, varianzas y lambdas).
- Ejecutar simulaciones extensas.
- Analizar el sistema sin intervenir la operación real del polideportivo.

---

##  Contexto académico

Este trabajo refleja el enfoque de la materia **Simulación**:

> **Simular no es predecir exactamente, sino comprender el comportamiento de un sistema bajo incertidumbre.**

---

<div align="center">

###  La simulación permite tomar decisiones informadas  
### sin necesidad de modificar el sistema real.

</div>
