from odoo import api, fields, models


class Minuman(models.Model):
    _name = 'toko.minuman'
    _description = 'Daftar Minuman '

    name = fields.Char(string='Name')
    deskripsi = fields.Char(string='Deskripsi Minuman')
    harga = fields.Integer(string='Harga Minuman')