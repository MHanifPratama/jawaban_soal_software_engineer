from odoo import models, fields, api

class Guru(models.Model):
    _name = 'guru'
    _description = 'Guru'
    _rec_name = 'nm_guru'
    
    nip = fields.Char('NIP')
    nm_guru = fields.Char('Nama Guru')
    jns_kelamin = fields.Selection([
        ('pria', 'Pria'),
        ('wanita', 'Wanita')
    ], string='Jenis Kelamin')
    mata_pelajaran = fields.Many2one('matapelajaran', string='mata_pelajaran')
    kelas_ids = fields.Many2many('kelas', string='Kelas')
    usia = fields.Integer('Usia')
    no_telp = fields.Char('Nomor Telepon')
    alamat = fields.Text('Alamat')