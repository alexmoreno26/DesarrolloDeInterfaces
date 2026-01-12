# Sistema Cliente–Servidor con Sockets  
**Cliente:** Python (Sockets) + QtDesigner + PySide6  
**Servidor:** Java (Sockets) Multihilo  

---

## 1. Arquitectura General
┌──────────────┐ TCP/IP ┌────────────────────┐
│ Cliente │ ───────────────▶ │ Servidor Java │
│ Python │ ◀─────────────── │ Multihilo │
│ PySide6 GUI │ │ Socket TCP │
└──────────────┘ └────────────────────┘
## 2. Requisitos Funcionales (Capacidades)

- Enviar mensajes
- Recibir mensajes
- Envío de documentos
- Manejo de horarios
- Gestión de usuarios
- Creación y administración de grupos
- Filtro de mensajes
- Disponibilidad de usuarios
- Reenvío de mensajes
- Responder mensajes (reply)

---

## 3. Requisitos No Funcionales (Tecnología)

| Componente | Tecnología |
|-----------|------------|
| Cliente | Python 3 |
| GUI | QtDesigner + PySide6 |
| Comunicación | Sockets TCP |
| Servidor | Java |
| Concurrencia | Multihilo |
| Seguridad | Criptografía de mensajes |

---

Time Stamp + usuario + mensaje = cripto --> pay load 

---

- investigar cripto  
- sockets python  
- mockup interfaz  
- diagrama de clases  
- interfaz QtDesigner  
- servidor multihilo  
- clientes python con sockets  
- interfaz --> señales + slots  
- documentacion  
