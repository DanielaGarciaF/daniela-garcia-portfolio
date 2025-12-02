<div align="center">

#  Seguridad de Desarrollo de Sistemas (SDS) - Proyecto UTN-FRC  
### Laboratorio educativo de hacking ético y seguridad web

[![React](https://img.shields.io/badge/Frontend-React-61DAFB?logo=react&logoColor=black)]()
[![Flask](https://img.shields.io/badge/Backend-Flask-000000?logo=flask&logoColor=white)]()
[![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite&logoColor=white)]()
[![Security](https://img.shields.io/badge/Focus-Seguridad%20Inform%C3%A1tica-red?logo=hackthebox&logoColor=white)]()
[![CTF](https://img.shields.io/badge/Modo-CTF%20%2F%20Pentesting%20Lab-8A2BE2)]()

</div>

---

##  Sobre la materia donde se desarrolló este proyecto

Este trabajo práctico fue realizado para la materia:

La materia tiene como propósito enseñar seguridad aplicada desde el inicio del ciclo de desarrollo de software (SDLC), incorporando pensamiento crítico y prácticas de ataque/defensa.

###  **Objetivos de la materia**
1. Aplicar seguridad informática desde el inicio del desarrollo de software.  
2. Aprender técnicas de ataque y de defensa.  
3. Aprender y escribir código seguro.

###  **Aportes al desarrollo profesional**
1. Habilidades técnicas aplicadas a seguridad ofensiva y defensiva.  
2. Capacidad para pensar como un hacker para detectar fallas.  
3. Fomento del trabajo en equipo en entornos de seguridad realista.

---

##  ¿Qué es esta aplicación?

Es una plataforma interactiva tipo **CTF / Pentesting Lab**, creada para **aprender y practicar vulnerabilidades web reales** en un entorno totalmente seguro y controlado.  
El usuario actúa como un *hacker ético*, encontrando fallas, explotándolas y aprendiendo las contramedidas.

Este proyecto está inspirado en herramientas como:

[![WebGoat](https://img.shields.io/badge/OWASP-WebGoat-orange?logo=owasp&logoColor=white)](https://owasp.org/www-project-webgoat/)
[![HackTheBox](https://img.shields.io/badge/HackTheBox-Platform-9FEF00?logo=hackthebox&logoColor=black)](https://www.hackthebox.com/)
[![TryHackMe](https://img.shields.io/badge/TryHackMe-Learning_Platform-red?logo=tryhackme&logoColor=white)](https://tryhackme.com/)
[![SoftwareSeguro](https://img.shields.io/badge/SoftwareSeguro.com.ar-Seguridad_Web-blue?logo=linux&logoColor=white)](https://www.softwareseguro.com.ar/)

---

##  Vulnerabilidades Incluidas (Explicación breve)

| Vulnerabilidad | Descripción corta |
|----------------|------------------|
| **IDOR (Insecure Direct Object Reference)** | Permite acceder a recursos ajenos modificando IDs en la URL o request. Tiene análisis profundo en esta aplicación. |
| **SQL Injection** | Entrada no validada permite inyectar consultas SQL, exponiendo datos o comprometiendo la base. |
| **Information Disclosure** | Se revela información sensible como rutas, errores detallados o datos internos. |
| **Broken Access Control** | Usuarios sin permisos pueden acceder a funciones restringidas. |
| **Weak Authentication** | Sistema de login débil, predecible o evadible mediante ataques básicos. |

---

##  Componentes del Proyecto

###  **Frontend – React + Vite**
- Interfaz moderna
- Panel de usuario y panel de administración
- Formularios vulnerables
- Secciones diseñadas para practicar fallas

###  **Backend – Flask**
- API con vulnerabilidades intencionadas
- Endpoints inseguros para cada reto
- Sistema de autenticación débil
- Manejo básico de sesiones
- Respuestas útiles para análisis y explotación

###  **Bases de Datos – SQLite**
- **users.db** → Usuarios, credenciales y roles  
- **game.db** → Retos, puntajes y flags obtenidas  

---

##  Propósito Educativo

Esta aplicación permite:

- Aprender cómo funcionan las vulnerabilidades más comunes
- Explorar fallas en un entorno seguro
- Practicar técnicas reales de explotación
- Observar el código vulnerable y su corrección
- Comprender buenas prácticas de seguridad web

###  **Flujo típico del usuario**

1. Registrarse  
2. Iniciar sesión  
3. Elegir un reto/vulnerabilidad  
4. Intentar explotarla  
5. Obtener la “flag” o puntaje  
6. Leer la explicación y las soluciones  

---

##  Arquitectura del Proyecto

Usuario → Frontend (React) → Backend (Flask) → DB SQLite
                 ↓
         Panel de vulnerabilidades
                 ↓
          Retos de seguridad
                 ↓
            Sistema de scoring


---

## 🚨 Advertencia 🚨

Esta es una aplicación **deliberadamente vulnerable**.  
No debe usarse en producción ni conectarse a sistemas reales.  
Su único propósito es educativo y experimental.

---

