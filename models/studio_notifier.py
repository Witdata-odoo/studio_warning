# -*- coding: utf-8 -*-
from odoo import models, api

class partnerStudioNotifier(models.AbstractModel):
    _name = 'partner.studio.notifier'
    _description = 'Notificador de uso de Studio para partner'

    @api.model
    def notify_partner(self):
        user = self.env.user
        company = user.company_id
        
        email_to = self.env['ir.config_parameter'].sudo().get_param('partner.studio.email', '')

        mail_values = {
            'subject': f'⚠️ Alerta: Odoo Studio activado por {user.name}',
            'body_html': f'''
                <div style="font-family: Arial, sans-serif; color: #333; padding: 20px; border: 1px solid #e0e0e0; border-radius: 5px;">
                    <h2 style="color: #d9534f; margin-top: 0;">Alerta de uso de Odoo Studio</h2>
                    <p>Hola Equipo de partner,</p>
                    <p>El usuario <b>{user.name}</b> (<i>{user.login}</i>) ha aceptado los términos de responsabilidad y acaba de activar la herramienta <b>Odoo Studio</b>.</p>
                    <div style="background-color: #f9f2f4; border-left: 4px solid #d9534f; padding: 10px; margin: 15px 0;">
                        <b>Nota de exclusión:</b> Queda registrado que no se aceptarán tickets de soporte sobre su uso o futuros errores generados por las modificaciones realizadas por este usuario.
                    </div>
                </div>
            ''',
            'email_to': email_to,
            'email_from': company.catchall_formatted or company.email_formatted or user.email_formatted,
            'auto_delete': True,
        }

        
        mail = self.env['mail.mail'].sudo().create(mail_values)
        mail.send(raise_exception=False)
        
        return True