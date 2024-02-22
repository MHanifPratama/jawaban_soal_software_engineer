from odoo import models, fields, api

class MataPelajaran(models.Model):
    _name = 'matapelajaran'
    _description = 'Mata Pelajaran'
    
    nm_matapelajaran = fields.Char('Nama Matapelajaran')
    mata_pelajaran_ids = fields.One2many('jadwal', 'mata_pelajaran', string='Mata Pelajaran')
    jurusan = fields.Char('Jurusan')

    