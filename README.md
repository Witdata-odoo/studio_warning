# ⚠️ Studio Warning (Odoo Module)

Este módulo agrega una advertencia de responsabilidad antes de permitir el uso de **Odoo Studio**, y notifica automáticamente al partner cuando un usuario lo activa.

---

## 🚀 Funcionalidad

Cuando un usuario intenta abrir **Odoo Studio**:

1. Se muestra un diálogo de confirmación con advertencia.
2. Si el usuario acepta:
   - Se envía un email al partner.
   - Se abre Odoo Studio normalmente.
3. Si cancela:
   - No ocurre ninguna acción.

---

## 🧩 Componentes del módulo

### 🔹 Backend (Python)
- Modelo: `partner.studio.notifier`
- Método: `notify_partner()`
- Envía un email al partner configurado.

### 🔹 Configuración
- Parámetro del sistema:
  ```
  partner.studio.email
  ```

### 🔹 Frontend (JS)
- Parche del systray de Odoo Studio
- Muestra diálogo de advertencia
- Llama al backend para notificar

---

## ⚙️ Instalación

1. Copiar el módulo en tu carpeta de addons:
   ```
   studio_warning/
   ```

2. Actualizar lista de apps

3. Instalar módulo:
   ```
   Studio Warning
   ```

---

## 🔧 Configuración

Ir a:

Ajustes → Parámetros del sistema

Configurar:

```
partner.studio.email = partner@tuempresa.com
```

---

## 📧 Notificación

El sistema enviará un email cuando un usuario active Studio.

Incluye:
- Usuario
- Login
- Advertencia de responsabilidad

---

## ⚠️ Importante

- No bloquea Studio
- Solo agrega advertencia + notificación
- Deja registro del uso

---

## 📦 Dependencias

- base
- web
- web_studio
- mail

---

## 👨‍💻 Autor

Francisco Sulé - Witdata

---

## 📜 Licencia

LGPL-3
