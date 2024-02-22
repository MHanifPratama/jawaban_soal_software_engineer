from odoo import models, fields, api

class Kelas(models.Model):
    _name = 'kelas'
    _description = 'Kelas'
    _rec_name = 'nm_kelas'
    
    nm_kelas = fields.Char('Nama Kelas')
    nm_siswa = fields.Many2one('siswa', string='Nama Siswa')
    wali_kelas = fields.Char('Wali Kelas')    