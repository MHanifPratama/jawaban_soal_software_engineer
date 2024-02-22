from odoo import models, fields, api

class MasterProduct(models.Model):
    _name = "master.product"
    
    product_name = fields.Char('Nama Produk')