# -*- coding: utf-8 -*-
# from odoo import http


# class AdrianlopezOdoo(http.Controller):
#     @http.route('/adrianlopez_odoo/adrianlopez_odoo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/adrianlopez_odoo/adrianlopez_odoo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('adrianlopez_odoo.listing', {
#             'root': '/adrianlopez_odoo/adrianlopez_odoo',
#             'objects': http.request.env['adrianlopez_odoo.adrianlopez_odoo'].search([]),
#         })

#     @http.route('/adrianlopez_odoo/adrianlopez_odoo/objects/<model("adrianlopez_odoo.adrianlopez_odoo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('adrianlopez_odoo.object', {
#             'object': obj
#         })
