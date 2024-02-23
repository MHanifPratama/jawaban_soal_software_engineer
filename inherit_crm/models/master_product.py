from odoo import models, fields, api

class MasterProduct(models.Model):
    _name = "master.product"
    _rec_name = "product_name"
    
    product_name = fields.Char('Nama Produk')