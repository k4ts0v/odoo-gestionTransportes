# -*- coding: utf-8 -*-
# from odoo import http


# class GestionTransportes(http.Controller):
#     @http.route('/gestion_transportes/gestion_transportes', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion_transportes/gestion_transportes/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion_transportes.listing', {
#             'root': '/gestion_transportes/gestion_transportes',
#             'objects': http.request.env['gestion_transportes.gestion_transportes'].search([]),
#         })

#     @http.route('/gestion_transportes/gestion_transportes/objects/<model("gestion_transportes.gestion_transportes"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion_transportes.object', {
#             'object': obj
#         })

