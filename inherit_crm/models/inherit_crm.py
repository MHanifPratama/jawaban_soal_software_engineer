from odoo import models, fields, api

class InheritCRM(models.Model):
    _inherit = "crm.lead"
    
    is_new_customer = fields.Boolean(string="Pelanggan Baru")
    customer_segment = fields.Selection([
        ('konstruksi', 'Kontruksi'),
        ('perbankan', 'Perbankan'),
        ('pemerintah', 'Pemerintah'),
        ('bumd/bumn', 'BUMD/BUMN'),
        ('kementrian', 'Kementrian'),
        ('swasta', 'Swasta'),
        ('lainnya','Lainya')
    ], string='Segment Customer')
    task_progress_ids = fields.One2many('task.progress', 'task_progress_id', string='task_progress')