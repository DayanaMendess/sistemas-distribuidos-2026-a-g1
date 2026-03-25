# Semana 4 - Sesión 1: Spring Boot y Estructura de un Microservicio

## Actividad 1: Crear el Microservicio Base

Para el proyecto **Gestión-De-Citas-Inteligente**, se toma como microservicio base el **microservicio de citas**, ya que representa el núcleo principal del sistema.

### Generación del proyecto
El microservicio se propone crear desde **start.spring.io** con la siguiente configuración:

- **Project:** Maven
- **Language:** Java
- **Spring Boot:** versión estable compatible
- **Group:** com.gestioncitas
- **Artifact:** ms-citas
- **Name:** ms-citas
- **Packaging:** Jar
- **Java:** 17

### Dependencias propuestas
- Spring Web
- Spring Data JPA
- PostgreSQL Driver
- Lombok
- Validation

### Ubicación dentro del repositorio
Teniendo en cuenta la estructura real del proyecto, el microservicio debe ubicarse dentro de la carpeta:

~~~text
backend/ms-citas
~~~

### Estructura de paquetes propuesta

~~~text
backend/ms-citas/
└── src/main/java/com/gestioncitas/mscitas/
    ├── controller/
    ├── service/
    ├── repository/
    ├── entity/
    ├── dto/
    └── MsCitasApplication.java
~~~

### Explicación de paquetes
- **controller/**: contiene los endpoints REST del microservicio
- **service/**: contiene la lógica de negocio
- **repository/**: acceso a la base de datos mediante Spring Data JPA
- **entity/**: entidades del dominio
- **dto/**: objetos de transferencia para request y response

### Configuración inicial de `application.yml`
Se propone una configuración base para conectar el microservicio a PostgreSQL:

~~~yaml
server:
  port: 8081

spring:
  datasource:
    url: jdbc:postgresql://localhost:5432/gestion_citas
    username: postgres
    password: postgres
  jpa:
    hibernate:
      ddl-auto: update
    show-sql: true
    properties:
      hibernate:
        format_sql: true
~~~

### Observación
Con esta estructura base, el microservicio queda preparado para implementar la lógica principal del sistema y mantener una organización clara dentro del backend del proyecto.

---

## Actividad 2: Implementar CRUD Completo

Para el microservicio de citas, se propone implementar la entidad principal **Cita** con sus operaciones CRUD.

### Entidad principal propuesta: Cita

**Atributos principales:**
- id
- usuarioId
- especialidad
- fecha
- hora
- estado

### Endpoints CRUD propuestos

#### 1. Obtener todas las citas
**GET** `/api/citas`

#### 2. Obtener una cita por ID
**GET** `/api/citas/{id}`

#### 3. Crear una cita
**POST** `/api/citas`

#### 4. Actualizar una cita
**PUT** `/api/citas/{id}`

#### 5. Eliminar una cita
**DELETE** `/api/citas/{id}`

### Ejemplo de entidad `Cita`

~~~java
@Entity
public class Cita {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private Long usuarioId;
    private String especialidad;
    private String fecha;
    private String hora;
    private String estado;
}
~~~

### Ejemplo de request para crear una cita

~~~json
{
  "usuarioId": 10,
  "especialidad": "Cardiología",
  "fecha": "2026-04-05",
  "hora": "10:00",
  "estado": "PENDIENTE"
}
~~~

### Verificación esperada
- Los 5 endpoints deben responder correctamente.
- La información debe guardarse en PostgreSQL.
- Las pruebas deben poder realizarse con Postman o Thunder Client.
- Los registros deben verse reflejados en la base de datos.

### Observación
La implementación del CRUD completo permite validar la base funcional del microservicio principal del proyecto.

---

## Actividad 3: Hacer Commit y PR

Para trabajar de manera ordenada dentro del proyecto, se propone usar una rama feature específica para este microservicio.

### Nombre de rama sugerido
~~~text
feature/ms-citas-crud
~~~

### Ejemplos de commits descriptivos
- `feat(ms-citas): add cita entity`
- `feat(ms-citas): add cita repository`
- `feat(ms-citas): add cita service`
- `feat(ms-citas): add cita controller`

### Flujo propuesto
1. Crear la rama feature a partir de `develop`
2. Implementar cada capa del microservicio
3. Realizar commits claros y separados
4. Hacer push de la rama feature
5. Crear Pull Request hacia `develop`
6. Solicitar revisión a un compañero
7. Aprobar e integrar los cambios

### Observación
Este flujo permite mantener control sobre el desarrollo del backend y facilita la integración ordenada del trabajo del equipo.