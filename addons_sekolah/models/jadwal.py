from odoo import models, fields, api
from datetime import datetime

class Jadwal(models.Model):
    _name = 'jadwal'
    _description = 'Jadwal'
    
    hari = fields.Selection([
        ('senin', 'Senin'),
        ('selasa', 'Selasa'),
        ('rabu', 'Rabu'),
        ('kamis', 'Kamis'),
        ('jumat', 'Jumat'),
        ('sabtu', 'Sabtu'),
        ('minggu', 'Minggu'),
    ], string='Hari')
    kelas = fields.Many2one('kelas', string='Kelas')
    jam = fields.Datetime('Jam', default=datetime.now())
    mata_pelajaran = fields.Many2one('matapelajaran', string='Mata Pelajaran')
    
    

    