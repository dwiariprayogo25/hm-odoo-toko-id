from odoo import api, fields, models


class partner(models.Model):
    _name = 'toko.partner'
    _description = 'Stardar class partners'

    name = fields.Char(string='Name')
    alamat = fields.Char(string='Alamat')
    no_tlp = fields.Char(string='Telepon/HP')
    
