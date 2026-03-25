# Semana 3 - Sesión 1: Repositorio — Monorepo, Branching y Git Flow

## Actividad 1: Configurar el Monorepo

Para el proyecto **Gestión de Citas Inteligentes**, se plantea una estructura inicial de monorepo que permita organizar los microservicios, el gateway y la automatización del repositorio.

### Estructura propuesta del monorepo

~~~text
Gestion-De-Citas-Inteligente/
│
├── gateway/
│
├── ms-usuarios/
│
├── ms-citas/
│
├── ms-notificaciones/
│
├── ms-auth/
│
├── frontend/
│
├── .github/
│   └── workflows/
│
├── .gitignore
│
└── README.md
~~~

### Explicación de la estructura

- **gateway/**: contendrá el API Gateway del sistema.
- **ms-usuarios/**: microservicio encargado de la gestión de usuarios.
- **ms-citas/**: microservicio encargado de agendar, cancelar y reprogramar citas.
- **ms-notificaciones/**: microservicio encargado de notificaciones in-app y correo electrónico.
- **ms-auth/**: microservicio encargado de autenticación y seguridad.
- **frontend/**: interfaz visual del sistema.
- **.github/workflows/**: configuración de automatización y GitHub Actions.
- **.gitignore**: exclusión de archivos innecesarios o sensibles.
- **README.md**: descripción general del proyecto, integrantes y arquitectura base.

### Archivo .gitignore propuesto

Se propone incluir exclusiones para:

- carpetas de dependencias como `node_modules/`
- carpetas compiladas como `target/`, `dist/`
- archivos de entorno como `.env`
- configuraciones locales del sistema o editor

### README propuesto

El archivo `README.md` debe contener:

- nombre del proyecto
- integrantes del equipo
- breve descripción del sistema
- arquitectura general del monorepo

---

## Actividad 2: Configurar Ramas y Protecciones

Para el flujo de trabajo del equipo se propone la siguiente estrategia de ramas:

### Ramas principales

- `main`: rama estable del proyecto
- `develop`: rama de integración de avances
- `qa`: rama de pruebas y validación

### Flujo de trabajo propuesto

- Los desarrolladores crean ramas `feature/...` a partir de `develop`
- Los cambios se integran primero en `develop`
- Luego se validan en `qa`
- Finalmente se llevan a `main`

### Ejemplo de ramas feature

- `feature/frontend-notificaciones`
- `feature/backend-citas`
- `feature/auth-login`

### Protección de la rama main

Se propone configurar reglas de protección para `main` con:

- prohibición de push directo
- obligación de Pull Request
- al menos 1 aprobación antes del merge

### Verificación esperada

Si un integrante intenta hacer push directo a `main`, la operación debe fallar.  
Esto garantiza mayor control sobre los cambios y reduce riesgos de errores en producción.

### Proceso correcto

1. Crear rama feature
2. Realizar cambios
3. Hacer push de la rama feature
4. Crear Pull Request hacia `develop`
5. Revisar y aprobar cambios
6. Integrar posteriormente a `qa` y `main`

---

## Actividad 3: Primer GitHub Action

Se propone crear un workflow básico de GitHub Actions en:

~~~text
.github/workflows/ci.yml
~~~

### Objetivo del workflow

Automatizar una verificación inicial del repositorio cada vez que se haga push o pull request.

### Ejemplo de workflow básico

~~~yaml
name: CI

on:
  push:
    branches:
      - develop
      - main
  pull_request:
    branches:
      - develop
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout del repositorio
        uses: actions/checkout@v4

      - name: Mostrar mensaje de validación
        run: echo "Workflow ejecutado correctamente"
~~~

### Resultado esperado

- El workflow debe ejecutarse en la pestaña **Actions** de GitHub.
- Debe aparecer un check de estado en los Pull Requests.
- Esto sirve como base para automatizaciones futuras más completas.

### Observación

El uso de un monorepo con ramas bien definidas y un primer GitHub Action fortalece la organización del proyecto, mejora el control del código y prepara al equipo para un flujo de trabajo más profesional.
