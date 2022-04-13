# -*- coding: utf-8 -*-
# from odoo import http


# class Tokoid(http.Controller):
#     @http.route('/tokoid/tokoid/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tokoid/tokoid/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tokoid.listing', {
#             'root': '/tokoid/tokoid',
#             'objects': http.request.env['tokoid.tokoid'].search([]),
#         })

#     @http.route('/tokoid/tokoid/objects/<model("tokoid.tokoid"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tokoid.object', {
#             'object': obj
#         })
