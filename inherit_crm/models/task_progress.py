from odoo import models, fields, api
from datetime import datetime

class TaskProgress(models.Model):
    _name = "task.progress"
    
    
    task_progress_id = fields.Many2one('crm.lead', string='task_progress')
    task_name = fields.Char('Task')
    deadline = fields.Datetime('Deadline', default=datetime.now())
    state = fields.Selection([
        ('todo', 'To Do'),
        ('progress', 'Progress'),
        ('Done', 'Done')
    ], string='Status')