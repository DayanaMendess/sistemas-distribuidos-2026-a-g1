# Semana 4 - Sesión 2: PostgreSQL y Persistencia con Spring Data JPA

## Actividad 1: Levantar PostgreSQL con Docker

Para el proyecto **Gestión-De-Citas-Inteligente**, se propone levantar PostgreSQL con Docker para facilitar el desarrollo local del backend.

### Archivo `docker-compose.yml` propuesto

~~~yaml
version: '3.8'

services:
  postgres:
    image: postgres:16
    container_name: gestion-citas-postgres
    environment:
      POSTGRES_DB: gestion_citas
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
~~~

### Ubicación dentro del proyecto
Teniendo en cuenta la estructura actual del repositorio, este archivo debe ubicarse en:

~~~text
docker/docker-compose.yml
~~~

### Pasos propuestos
1. Agregar el archivo `docker-compose.yml`
2. Ejecutar el comando:

~~~bash
docker-compose up -d
~~~

3. Verificar que PostgreSQL quede disponible en el puerto `5432`
4. Acceder con pgAdmin o cliente SQL y comprobar la creación de la base de datos `gestion_citas`
5. Levantar el microservicio de citas y verificar que las tablas se creen automáticamente

### Objetivo
Contar con una base de datos local estable para las pruebas y persistencia de los microservicios del proyecto.

---

## Actividad 2: Implementar 2+ Entidades con Relación

Para el dominio del proyecto se propone trabajar con dos entidades relacionadas: **Cita** y **Profesional**.

### Entidad Profesional
**Atributos sugeridos:**
- id
- nombre
- especialidad

### Entidad Cita
**Atributos sugeridos:**
- id
- usuarioId
- fecha
- hora
- estado
- profesional

### Relación propuesta
- Un **Profesional** puede tener muchas **Citas**
- Una **Cita** pertenece a un **Profesional**

### Ejemplo de relación JPA

~~~java
@Entity
public class Profesional {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String nombre;
    private String especialidad;

    @OneToMany(mappedBy = "profesional")
    private List<Cita> citas;
}
~~~

~~~java
@Entity
public class Cita {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private Long usuarioId;
    private String fecha;
    private String hora;
    private String estado;

    @ManyToOne
    @JoinColumn(name = "profesional_id")
    private Profesional profesional;
}
~~~

### Capas requeridas
Para ambas entidades se propone implementar:
- Repository
- Service
- Controller
- DTOs

### Uso de DTOs
Se recomienda usar DTOs para:
- evitar exponer directamente las entidades
- controlar mejor la estructura de las respuestas
- prevenir problemas de serialización en relaciones bidireccionales

### Verificación esperada
- Crear profesionales
- Crear citas asociadas a profesionales
- Consultar información correctamente en Postman
- Verificar los registros en PostgreSQL

---

## Actividad 3: Manejo de Errores y Validación

Para fortalecer el backend, se propone implementar validaciones y manejo global de excepciones.

### Validaciones sugeridas en DTOs
- `@NotBlank`
- `@NotNull`
- `@Email`
- `@Size`

### Ejemplo de DTO con validaciones

~~~java
public class CitaRequestDTO {

    @NotNull(message = "El usuario es obligatorio")
    private Long usuarioId;

    @NotBlank(message = "La fecha es obligatoria")
    private String fecha;

    @NotBlank(message = "La hora es obligatoria")
    private String hora;

    @NotNull(message = "El profesional es obligatorio")
    private Long profesionalId;
}
~~~

### Manejo global de errores
Se propone implementar un `GlobalExceptionHandler` para capturar errores comunes del API y responder con mensajes claros.

### Comportamiento esperado
Cuando se envíe un request inválido:
- el sistema debe responder con código HTTP `400 Bad Request`
- debe devolver un mensaje claro indicando qué campo falló

### Beneficio
Esto mejora la calidad del API, facilita la depuración y hace más clara la integración con el frontend.

---

## Actividad 4: Commit, PR y Merge

Para mantener buenas prácticas de trabajo colaborativo, se propone el siguiente flujo:

### Convención de commit sugerida
~~~text
feat(ms-citas): add PostgreSQL persistence
~~~

### Flujo propuesto
1. Trabajar en una rama feature
2. Hacer commits con nombres claros
3. Hacer push de la rama
4. Crear Pull Request hacia `develop`
5. Solicitar review a otro integrante
6. Aprobar el PR
7. Hacer merge y verificar que `develop` siga funcionando correctamente con la base de datos

### Observación
La integración de PostgreSQL, relaciones JPA, validaciones y revisión mediante Pull Request fortalece la base técnica del backend y mejora el flujo de trabajo del equipo.