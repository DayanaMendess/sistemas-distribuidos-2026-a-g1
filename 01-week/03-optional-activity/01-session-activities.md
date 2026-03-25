# Semana 1 - Sesión 1: Introducción a Sistemas Distribuidos

## Actividad 1: Identificar Sistemas Distribuidos

A continuación, se presentan 3 aplicaciones de uso diario y su posible clasificación como monolíticas o distribuidas.

### 1. WhatsApp
**Clasificación:** Distribuida

**Justificación:**
- Tiene aplicación móvil y versión web.
- Permite enviar mensajes, imágenes, audios y documentos.
- Diferentes funcionalidades parecen operar de manera independiente.
- Los mensajes se sincronizan entre varios dispositivos.
- Requiere comunicación constante con servidores para entregar mensajes y mantener disponibilidad.

### 2. Google Drive
**Clasificación:** Distribuida

**Justificación:**
- Funciona desde navegador web y desde aplicación móvil.
- Permite almacenamiento, edición, sincronización y compartición de archivos.
- Soporta acceso desde distintos dispositivos.
- Algunas funciones pueden trabajar parcialmente offline y luego sincronizarse.
- Maneja grandes cantidades de datos distribuidos entre servidores.

### 3. Calculadora del celular
**Clasificación:** Monolítica

**Justificación:**
- Ejecuta toda su lógica dentro del mismo dispositivo.
- No depende de servidores externos para operar.
- Su funcionalidad es simple y centralizada.
- No necesita sincronización ni comunicación con otros sistemas.

---

## Actividad 2: Formación de Equipos

### Integrantes del equipo
- Sofia Perafan
- [Nombre integrante 2]
- [Nombre integrante 3]
- [Nombre integrante 4]

### Roles iniciales
| Integrante | Rol |
|-----------|-----|
| Sofia Perafan | Frontend |
| [Nombre integrante 2] | Backend |
| [Nombre integrante 3] | DevOps |
| [Nombre integrante 4] | Tech Lead |

**Nota:** Los roles pueden rotar durante el semestre según lo indicado por el docente.

---

## Actividad 3: Brainstorming del Proyecto

El equipo propuso las siguientes ideas de proyecto:

### Idea 1: Gestión de Citas Inteligentes
**Problema que resuelve:**  
Facilita la programación, confirmación, cancelación y recordatorio de citas, evitando desorganización y olvidos.

**Microservicios que necesitaría:**
- Microservicio de usuarios
- Microservicio de citas
- Microservicio de notificaciones
- Microservicio de autenticación

**Datos que maneja:**
- Datos de usuarios
- Información de citas
- Horarios disponibles
- Estados de confirmación
- Historial de notificaciones

---

### Idea 2: Sistema de Rutas Seguras
**Problema que resuelve:**  
Ayuda a los usuarios a elegir rutas no solo rápidas, sino también seguras, basadas en incidentes reportados y zonas de riesgo.

**Microservicios que necesitaría:**
- Microservicio de usuarios
- Microservicio de rutas
- Microservicio de incidentes
- Microservicio de geolocalización
- Microservicio de notificaciones

**Datos que maneja:**
- Ubicación del usuario
- Historial de incidentes
- Zonas de riesgo
- Rutas sugeridas
- Reportes de usuarios

---

## Proyecto seleccionado

**Proyecto elegido:** Gestión de Citas Inteligentes

**Justificación:**  
El equipo seleccionó esta idea porque resuelve una necesidad real, permite aplicar arquitectura distribuida mediante varios microservicios y es viable de desarrollar durante el semestre.