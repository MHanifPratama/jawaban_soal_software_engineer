from odoo import models, fields, api
from datetime import datetime

class Siswa(models.Model):
    _name = 'siswa'
    _description = 'Siswa'
    _rec_name = 'nm_siswa'

    nis = fields.Char("NIS")
    nm_siswa = fields.Char("Nama Siswa")
    kelas_ids = fields.One2many('kelas', 'nm_siswa', string='kelas')
    jns_kelamin = fields.Selection([
        ('pria', 'Pria'),
        ('wanita', 'Wanita')
    ], string='Jenis Kelamin')
    tgl_lahir = fields.Date('Tanggal Lahir')
    agama = fields.Char('Agama')
    nm_ayah = fields.Char('Nama Ayah')
    nm_ibu = fields.Char('Nama Ibu')
    alamat = fields.Text('Alamat')
    usia = fields.Char(compute='_compute_usia', string='usia')
    
    @api.depends('tgl_lahir')
    def _compute_usia(self):
        today = datetime.today().date()
        for record in self:
            if record.tgl_lahir:
                usia = today.year - record.tgl_lahir.year - ((today.month, today.day) < (record.tgl_lahir.month, record.tgl_lahir.day))
                record.usia = usia
            else:
                record.usia = 0
    