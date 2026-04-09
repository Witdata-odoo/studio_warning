/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { ConfirmationDialog } from "@web/core/confirmation_dialog/confirmation_dialog";
import { systrayItem } from "@web_studio/systray_item/systray_item";

patch(systrayItem.Component.prototype, "partner_studio_warning.systray_patch", {
    _onClick() {
        if (this.isLoading) {
            return;
        }

        this.env.services.dialog.add(ConfirmationDialog, {
            title: "⚠️ AVISO DE RESPONSABILIDAD",
            body: "Al usar Odoo Studio asumes toda la responsabilidad de las modificaciones en el sistema. No se aceptarán tickets de soporte por errores derivados de su uso o futuras consultas sobre la herramienta. Si aceptas, se enviará una notificación a partner.",
            confirmLabel: "Acepto los riesgos, abrir Studio",
            cancelLabel: "Cancelar",
            confirm: async () => {
                try {
                    // 1. Notificar a partner llamando al modelo de Python
                    await this.env.services.orm.call("partner.studio.notifier", "notify_partner", []);
                } catch (error) {
                    console.error("Error al notificar:", error);
                }
                
                // 2. Ejecutar la acción original de abrir Studio
                this.studio.open();
            },
            cancel: () => {
                // Se cierra sin hacer nada
            }
        });
    }
});