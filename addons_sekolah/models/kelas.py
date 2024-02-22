from odoo import models, fields, api

class Kelas(models.Model):
    _name = 'kelas'
    _description = 'Kelas'
    _rec_name = 'nm_kelas'
    
    nm_kelas = fields.Char('Nama Kelas')
    jadwal_ids = fields.One2many('jadwal', 'kelas', string='Jadwal')
    nm_siswa = fields.One2many('siswa', 'kelas_ids', string='Nama Siswa')
    wali_kelas = fields.Many2many('guru', string='Guru')