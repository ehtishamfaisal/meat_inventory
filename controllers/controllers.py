# -*- coding: utf-8 -*-
from odoo import http

# class MeatInventory(http.Controller):
#     @http.route('/meat_inventory/meat_inventory/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/meat_inventory/meat_inventory/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('meat_inventory.listing', {
#             'root': '/meat_inventory/meat_inventory',
#             'objects': http.request.env['meat_inventory.meat_inventory'].search([]),
#         })

#     @http.route('/meat_inventory/meat_inventory/objects/<model("meat_inventory.meat_inventory"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('meat_inventory.object', {
#             'object': obj
#         })