# Semana 5 - Sesión 2: Retrospectiva y Planificación Release 2

## Actividad 1: Retrospectiva del Equipo

El equipo realizó una retrospectiva usando la dinámica **Start - Stop - Continue** con base en el trabajo desarrollado durante las primeras semanas del proyecto **Gestión-De-Citas-Inteligente**.

### Start
Acciones que el equipo debería comenzar a hacer:
- Documentar mejor los acuerdos técnicos y funcionales de cada semana.
- Crear issues más detallados en GitHub para dividir mejor las tareas.
- Hacer revisiones cruzadas antes de subir cambios importantes.
- Mantener más sincronización entre frontend y backend antes de integrar.

### Stop
Acciones que el equipo debería dejar de hacer:
- Subir cambios sin verificar antes la rama o el remoto correcto.
- Trabajar partes importantes sin validar primero el flujo acordado del repositorio.
- Dejar decisiones técnicas solo habladas y no registradas.
- Depender de mensajes informales en lugar de usar issues o comentarios en el repositorio.

### Continue
Acciones que el equipo debería continuar haciendo:
- Mantener la estructura organizada del proyecto.
- Trabajar por módulos separados entre frontend y backend.
- Usar ramas y commits para evidenciar el trabajo realizado.
- Repartir responsabilidades por roles según el avance del proyecto.

### Action items priorizados
Después de la retrospectiva, el equipo prioriza estos 3 action items:
1. Mejorar la comunicación entre frontend y backend antes de integrar cambios.
2. Mantener documentadas las actividades y acuerdos de cada weekly dentro del repositorio.
3. Organizar mejor las tareas mediante issues y tablero del proyecto.

### Observación
La retrospectiva permitió identificar oportunidades de mejora en la organización del trabajo y en la coordinación del equipo para las siguientes releases.

---

## Actividad 2: Analizar Métricas en GitHub

Se revisaron las métricas disponibles en GitHub para evaluar el avance del equipo y el uso del repositorio.

### Revisión de Contributors
A partir de **Insights > Contributors**, se observó que las métricas visibles en GitHub no siempre reflejan todos los aportes realizados, especialmente cuando:
- los cambios se hacen en ramas distintas a `main`
- los merges no se cuentan directamente
- algunos aportes aún no han sido integrados al repositorio principal

### Issues cerrados vs planificados
El equipo plantea revisar:
- cantidad de tareas planificadas
- cantidad de tareas cerradas
- tareas aún pendientes

Esto permite medir el cumplimiento del trabajo planeado.

### Verificación de commits del equipo
Se verificó que los integrantes del equipo tengan actividad en Git, evidenciada mediante:
- commits
- ramas de trabajo
- pushes
- Pull Requests

### Velocity del equipo
La velocidad del equipo se puede estimar como:
**Issues o tareas completadas durante las primeras 5 semanas**

### Observación
Las métricas de GitHub son útiles para analizar participación y avance, pero deben interpretarse junto con el historial de ramas, commits y Pull Requests para reflejar correctamente el trabajo real del equipo.

---

## Actividad 3: Planificar Release 2

Para la segunda release del proyecto **Gestión-De-Citas-Inteligente**, el equipo propone enfocarse en fortalecer el backend y la integración con el frontend.

### Bounded Context / Microservicio priorizado para Release 2
**Microservicio de Notificaciones**

### Justificación
Se selecciona este microservicio porque:
- complementa el flujo principal de citas
- mejora la experiencia del usuario
- ya existe avance visual desde el frontend
- permite integrar notificaciones in-app y correo electrónico

### Issues propuestos para Sprint 6 y Sprint 7
1. Crear estructura base del microservicio de notificaciones
2. Implementar entidad de notificación
3. Crear CRUD de notificaciones
4. Integrar notificaciones in-app con el frontend
5. Implementar envío de correo con JavaMailSender
6. Crear endpoint para marcar notificaciones como leídas
7. Integrar eventos de citas con notificaciones
8. Validar flujo completo de confirmación, cancelación y recordatorio

### Asignación general del trabajo
- **Frontend:** vista y consumo de notificaciones
- **Backend:** microservicio, endpoints y persistencia
- **Integración:** conexión entre flujo de citas y notificaciones
- **Gestión:** issues, revisión y seguimiento del tablero

### Organización del tablero
Los nuevos issues deben ubicarse en el GitHub Project dentro de columnas como:
- Backlog
- To Do
- In Progress
- In Review
- Done

### Observación
La planificación de Release 2 busca consolidar la parte de notificaciones como siguiente avance importante del sistema.

---

## Actividad 4: Aplicar un Action Item de Mejora

Como acción inmediata de mejora, el equipo decide:

**Mejorar la documentación del proyecto y de las actividades realizadas**

### Aplicación de la mejora
Se propone:
- mantener actualizados los archivos `.md` de las actividades semanales
- organizar mejor la evidencia del trabajo dentro del repositorio
- dejar más claro qué avances corresponden al frontend y cuáles al backend

### Beneficio esperado
- mayor claridad para el equipo
- mejor seguimiento del avance
- evidencia más organizada para revisión del docente
- menos confusión al integrar cambios y continuar las siguientes releases

### Observación final
Aplicar esta mejora fortalece la organización del proyecto y facilita tanto la evaluación académica como la continuidad técnica del desarrollo.