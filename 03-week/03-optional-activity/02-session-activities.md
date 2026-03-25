# Semana 3 - Sesión 2: API Gateway, Service Discovery y REST APIs

## Actividad 1: Diseñar la API del Proyecto

Para el proyecto **Gestión de Citas Inteligentes**, se toma como microservicio principal el **Microservicio de Citas**.

### Recurso principal
`/api/citas`

### Endpoints REST propuestos

#### 1. Listar todas las citas
**Método:** `GET`  
**Endpoint:** `/api/citas`

**Respuesta ejemplo:**
~~~json
[
  {
    "id": 1,
    "usuarioId": 10,
    "especialidad": "Cardiología",
    "fecha": "2026-03-28",
    "hora": "10:00",
    "estado": "CONFIRMADA"
  },
  {
    "id": 2,
    "usuarioId": 11,
    "especialidad": "Dermatología",
    "fecha": "2026-03-29",
    "hora": "14:00",
    "estado": "PENDIENTE"
  }
]
~~~

#### 2. Obtener una cita por ID
**Método:** `GET`  
**Endpoint:** `/api/citas/{id}`

**Respuesta ejemplo:**
~~~json
{
  "id": 1,
  "usuarioId": 10,
  "especialidad": "Cardiología",
  "fecha": "2026-03-28",
  "hora": "10:00",
  "estado": "CONFIRMADA"
}
~~~

#### 3. Crear una nueva cita
**Método:** `POST`  
**Endpoint:** `/api/citas`

**Request ejemplo:**
~~~json
{
  "usuarioId": 10,
  "especialidad": "Medicina General",
  "fecha": "2026-03-30",
  "hora": "09:00"
}
~~~

**Response ejemplo:**
~~~json
{
  "id": 3,
  "usuarioId": 10,
  "especialidad": "Medicina General",
  "fecha": "2026-03-30",
  "hora": "09:00",
  "estado": "PENDIENTE"
}
~~~

#### 4. Actualizar una cita
**Método:** `PUT`  
**Endpoint:** `/api/citas/{id}`

**Request ejemplo:**
~~~json
{
  "especialidad": "Medicina General",
  "fecha": "2026-03-31",
  "hora": "11:00",
  "estado": "REPROGRAMADA"
}
~~~

**Response ejemplo:**
~~~json
{
  "id": 3,
  "usuarioId": 10,
  "especialidad": "Medicina General",
  "fecha": "2026-03-31",
  "hora": "11:00",
  "estado": "REPROGRAMADA"
}
~~~

#### 5. Eliminar una cita
**Método:** `DELETE`  
**Endpoint:** `/api/citas/{id}`

**Response ejemplo:**
~~~json
{
  "mensaje": "Cita eliminada correctamente"
}
~~~

### Observación
Estos endpoints cubren las operaciones CRUD básicas y sirven como base para documentar y construir el microservicio de citas.

---

## Actividad 2: Crear Proyecto Spring Boot del Gateway

Para la arquitectura del proyecto se propone crear un **API Gateway** con Spring Boot.

### Configuración propuesta
- **Proyecto:** Maven
- **Lenguaje:** Java
- **Versión Java:** 17
- **Dependencia principal:** Spring Cloud Gateway

### Ubicación en el monorepo
El proyecto del gateway debe quedar dentro de:

~~~text
gateway/
~~~

### Archivo de configuración inicial
Se plantea una configuración simple en `application.yml` para enrutar solicitudes hacia el primer microservicio.

### Ejemplo de `application.yml`

~~~yaml
server:
  port: 8080

spring:
  cloud:
    gateway:
      routes:
        - id: ms-citas
          uri: http://localhost:8081
          predicates:
            - Path=/api/citas/**
~~~

### Explicación
- El gateway escuchará en el puerto `8080`
- Las solicitudes a `/api/citas/**` se redirigirán al microservicio de citas en `localhost:8081`

### Objetivo
Centralizar la entrada al sistema para que el frontend no consuma directamente cada microservicio.

---

## Actividad 3: Probar con Postman / Thunder Client

Para validar la API propuesta, se plantea usar una herramienta de pruebas como **Postman** o **Thunder Client**.

### Colección de pruebas sugerida
La colección debe contener los endpoints del microservicio de citas:

- `GET /api/citas`
- `GET /api/citas/{id}`
- `POST /api/citas`
- `PUT /api/citas/{id}`
- `DELETE /api/citas/{id}`

### Ejemplo de prueba de creación de cita
**Método:** `POST`  
**Endpoint:** `http://localhost:8080/api/citas`

**Body ejemplo:**
~~~json
{
  "usuarioId": 10,
  "especialidad": "Odontología",
  "fecha": "2026-04-01",
  "hora": "08:30"
}
~~~

**Respuesta esperada:**
~~~json
{
  "id": 4,
  "usuarioId": 10,
  "especialidad": "Odontología",
  "fecha": "2026-04-01",
  "hora": "08:30",
  "estado": "PENDIENTE"
}
~~~

### Utilidad de la colección
- validar que la API esté bien diseñada
- probar request y response
- documentar ejemplos reales de uso
- servir como apoyo para el desarrollo del backend

### Observación
El diseño del API Gateway y de los endpoints REST permite definir una base clara de integración entre frontend y backend, además de preparar la futura conexión entre microservicios.