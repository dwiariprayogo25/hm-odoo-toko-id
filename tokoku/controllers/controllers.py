# -*- coding: utf-8 -*-
# from odoo import http


# class Tokoku(http.Controller):
#     @http.route('/tokoku/tokoku/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tokoku/tokoku/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tokoku.listing', {
#             'root': '/tokoku/tokoku',
#             'objects': http.request.env['tokoku.tokoku'].search([]),
#         })

#     @http.route('/tokoku/tokoku/objects/<model("tokoku.tokoku"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tokoku.object', {
#             'object': obj
#         })
