from odoo import api, fields, models


class Barang(models.Model):
    _name = 'toko.barang'
    _description = 'model untuk tabel barang'
    minuman = fields.Many2one(comodel_name='toko.minuman', string='Tipe Minuman')
    
    name = fields.Char(string='name')
    tipebarang = fields.Selection(string='tipe barang', selection=[( 'barang jadi', 'Barang Jadi'), ('barang mentah', 'Barang Mentah'), ])
    harga = fields.Integer(string='harga barang')
    jumlah = fields.Integer(string='jumlah barang')
    
    
