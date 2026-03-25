# Semana 2 - Sesión 2: Microservicios — DDD y Bounded Contexts

## Actividad 1: Identificar Subdominios

Para el proyecto **Gestión de Citas Inteligentes**, se identifican los siguientes subdominios:

### 1. Gestión de Usuarios
**Entidades principales:**
- Usuario
- Perfil

**Value Objects:**
- Nombre
- Correo electrónico
- Contraseña

**Clasificación:** Supporting

**Justificación:**  
Este subdominio permite administrar la información de los usuarios y sus perfiles, apoyando el funcionamiento general del sistema, aunque no constituye el núcleo principal del negocio.

---

### 2. Gestión de Citas
**Entidades principales:**
- Cita
- Horario
- Profesional

**Value Objects:**
- Fecha
- Hora
- Estado de la cita
- Especialidad

**Clasificación:** Core

**Justificación:**  
Este es el subdominio central del sistema, ya que el objetivo principal del proyecto es permitir la creación, modificación, cancelación y consulta de citas médicas.

---

### 3. Gestión de Notificaciones
**Entidades principales:**
- Notificación
- Recordatorio

**Value Objects:**
- Mensaje
- Tipo de notificación
- Fecha de envío

**Clasificación:** Supporting

**Justificación:**  
Este subdominio apoya el proceso principal de citas, informando al usuario sobre confirmaciones, cancelaciones, reprogramaciones y recordatorios.

---

### 4. Autenticación y Seguridad
**Entidades principales:**
- Credencial
- Sesión

**Value Objects:**
- Token
- Rol
- Estado de autenticación

**Clasificación:** Generic

**Justificación:**  
Es un subdominio común en muchos sistemas de software y puede resolverse mediante patrones y soluciones estándar, por lo que se clasifica como genérico.

---

## Actividad 2: Dibujar Context Map

A partir de los subdominios identificados, se proponen los siguientes **Bounded Contexts**:

- **Usuarios**
- **Citas**
- **Notificaciones**
- **Autenticación**

### Relaciones entre Bounded Contexts
- **Usuarios → Citas:** un usuario solicita, consulta, cancela o reprograma citas.
- **Citas → Notificaciones:** cuando una cita se confirma, cancela o reprograma, se genera una notificación.
- **Usuarios → Autenticación:** la autenticación valida la identidad y acceso del usuario.
- **Notificaciones → Usuarios:** las notificaciones se dirigen al usuario correspondiente.

### Tipo de comunicación
- REST entre frontend y API Gateway
- REST entre algunos microservicios
- Posible comunicación por eventos entre **Citas** y **Notificaciones**

### Datos compartidos
- ID de usuario
- ID de cita
- Fecha y hora de la cita
- Estado de la cita
- Información de contacto del usuario

### Representación textual del Context Map
~~~text
[Usuarios] ───────► [Citas]
    │                 │
    │                 ▼
    └────────────► [Autenticación]

[Citas] ───────► [Notificaciones]
[Usuarios] ────► [Notificaciones]
~~~

### Explicación general
Cada Bounded Context encapsula una parte específica del dominio.  
La separación permite reducir el acoplamiento, mejorar la mantenibilidad y facilitar la evolución del sistema.

---

## Actividad 3: Mapear Bounded Contexts a Microservicios

| Bounded Context | Microservicio | Base de datos | Método de comunicación | Release |
|-----------------|---------------|----------------|-------------------------|---------|
| Usuarios | ms-usuarios | PostgreSQL | REST | 1 |
| Citas | ms-citas | PostgreSQL | REST | 1 |
| Notificaciones | ms-notificaciones | PostgreSQL | REST / Eventos | 1 |
| Autenticación | ms-auth | PostgreSQL | REST | 1 |

### Observación
Este mapeo permite al equipo asignar responsabilidades claras a cada microservicio, desacoplar componentes del sistema y planear una arquitectura distribuida más escalable desde etapas tempranas del proyecto.