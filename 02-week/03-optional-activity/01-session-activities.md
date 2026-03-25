# Semana 2 - Sesión 1: Definición del Proyecto — User Stories y Arquitectura

## Actividad 1: Escribir User Stories

Proyecto seleccionado: **Gestión de Citas Inteligentes**

A continuación se presentan 10 User Stories del proyecto, usando el formato solicitado:  
**Como [rol], quiero [acción], para [beneficio]**, incluyendo criterios de aceptación y prioridad MoSCoW.

### US-01
**Como** paciente,  
**quiero** registrarme en la plataforma,  
**para** poder solicitar y gestionar mis citas médicas.

**Criterios de aceptación:**
- El sistema debe permitir ingresar nombre, correo y contraseña.
- El correo no debe estar repetido.
- El usuario debe quedar registrado exitosamente.

**Prioridad:** Must Have

---

### US-02
**Como** paciente,  
**quiero** iniciar sesión,  
**para** acceder a mis citas y notificaciones.

**Criterios de aceptación:**
- El sistema debe validar correo y contraseña.
- Si los datos son incorrectos, debe mostrar un mensaje de error.
- Si los datos son correctos, debe permitir el acceso.

**Prioridad:** Must Have

---

### US-03
**Como** paciente,  
**quiero** consultar los horarios disponibles,  
**para** seleccionar la cita que mejor se ajuste a mi disponibilidad.

**Criterios de aceptación:**
- El sistema debe mostrar fechas y horas disponibles.
- Los horarios ocupados no deben poder seleccionarse.
- La disponibilidad debe actualizarse correctamente.

**Prioridad:** Must Have

---

### US-04
**Como** paciente,  
**quiero** agendar una cita,  
**para** reservar atención con el profesional de salud requerido.

**Criterios de aceptación:**
- El usuario debe poder seleccionar especialidad, fecha y hora.
- El sistema debe guardar la cita correctamente.
- El sistema debe mostrar confirmación de la cita agendada.

**Prioridad:** Must Have

---

### US-05
**Como** paciente,  
**quiero** cancelar una cita,  
**para** liberar el espacio si no puedo asistir.

**Criterios de aceptación:**
- El sistema debe permitir cancelar una cita activa.
- La cita debe cambiar su estado a cancelada.
- El horario cancelado debe volver a quedar disponible.

**Prioridad:** Must Have

---

### US-06
**Como** paciente,  
**quiero** reprogramar una cita,  
**para** cambiarla a una fecha u hora más conveniente.

**Criterios de aceptación:**
- El sistema debe permitir elegir un nuevo horario disponible.
- La cita debe actualizarse con la nueva información.
- El sistema debe confirmar el cambio realizado.

**Prioridad:** Should Have

---

### US-07
**Como** paciente,  
**quiero** recibir notificaciones dentro de la aplicación,  
**para** enterarme de confirmaciones, recordatorios, cancelaciones o reprogramaciones.

**Criterios de aceptación:**
- El sistema debe mostrar un centro de notificaciones.
- Deben existir notificaciones de confirmación, cancelación, reprogramación y recordatorio.
- Las notificaciones deben poder marcarse como leídas.

**Prioridad:** Must Have

---

### US-08
**Como** paciente,  
**quiero** recibir notificaciones por correo electrónico,  
**para** recordar la información de mi cita incluso fuera de la plataforma.

**Criterios de aceptación:**
- El sistema debe enviar correo al confirmar una cita.
- El sistema debe enviar correo al cancelar o reprogramar una cita.
- El correo debe contener fecha, hora y estado de la cita.

**Prioridad:** Should Have

---

### US-09
**Como** administrador,  
**quiero** gestionar la disponibilidad de horarios,  
**para** controlar la agenda de atención del sistema.

**Criterios de aceptación:**
- El administrador debe poder crear horarios disponibles.
- El administrador debe poder modificar horarios existentes.
- El administrador debe poder desactivar horarios.

**Prioridad:** Should Have

---

### US-10
**Como** paciente,  
**quiero** consultar el historial de mis citas,  
**para** revisar mis solicitudes anteriores y su estado.

**Criterios de aceptación:**
- El sistema debe mostrar citas actuales y pasadas.
- Cada cita debe mostrar su estado.
- La información debe visualizarse en orden cronológico.

**Prioridad:** Could Have

---

## Actividad 2: Diagrama de Arquitectura

Se propone una arquitectura inicial basada en microservicios para el proyecto **Gestión de Citas Inteligentes**.

### Microservicios identificados
- **Microservicio de Usuarios**
- **Microservicio de Citas**
- **Microservicio de Notificaciones**
- **Microservicio de Autenticación**
- **API Gateway**

### Base de datos por microservicio
- **Usuarios:** PostgreSQL
- **Citas:** PostgreSQL
- **Notificaciones:** PostgreSQL
- **Autenticación:** PostgreSQL

### Comunicación entre microservicios
- Comunicación principal mediante **REST API**
- Posible uso de **eventos** para desacoplar el envío de notificaciones

### Ubicación del API Gateway
El **API Gateway** funcionará como punto de entrada único entre el frontend y los microservicios.

### Flujo general de la arquitectura
~~~text
Frontend
   │
   ▼
API Gateway
   │
   ├── Microservicio de Usuarios
   ├── Microservicio de Citas
   ├── Microservicio de Notificaciones
   └── Microservicio de Autenticación
~~~

### Explicación general
El frontend no se comunicará directamente con cada microservicio, sino a través del API Gateway.  
Esto permitirá centralizar la seguridad, el enrutamiento y el control de las solicitudes.

---

## Actividad 3: Configurar GitHub Project

Para la gestión del trabajo del equipo, se plantea un tablero Kanban en GitHub Project.

### Columnas propuestas
- Backlog
- To Do
- In Progress
- In Review
- Done

### Issues iniciales sugeridos
1. Diseñar módulo de registro e inicio de sesión
2. Diseñar interfaz de solicitud de citas
3. Implementar microservicio de citas
4. Implementar microservicio de notificaciones
5. Implementar historial de citas

### Labels sugeridos
- frontend
- backend
- bug
- enhancement
- documentation
- urgent

### Milestone propuesto
**Release 1 — MVP**

### Observación
El GitHub Project permite organizar el trabajo del equipo, dar seguimiento a las tareas más importantes y mantener control sobre el avance del proyecto durante el semestre.