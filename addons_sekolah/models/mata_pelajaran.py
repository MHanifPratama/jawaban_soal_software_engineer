from odoo import models, fields, api

class MataPelajaran(models.Model):
    _name = 'matapelajaran'
    _description = 'Mata Pelajaran'
    
    nm_matapelajaran = fields.Char('Nama Matapelajaran')
    mata_pelajaran_ids = fields.One2many('jadwal', 'mata_pelajaran', string='Mata Pelajaran')
    guru_ids = fields.One2many('guru', 'mata_pelajaran', string='Guru')
    jurusan = fields.Char('Jurusan')
    
    def name_get(self):
        result = []
        for record in self:
            name = record.nm_matapelajaran + " - "+ record.jurusan
            result.append((record.id, name))
        return result
