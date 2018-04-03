# -*- coding: utf-8 -*-
from odoo import http

# class Mobile(http.Controller):
#     @http.route('/mobile/mobile/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mobile/mobile/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mobile.listing', {
#             'root': '/mobile/mobile',
#             'objects': http.request.env['mobile.mobile'].search([]),
#         })

#     @http.route('/mobile/mobile/objects/<model("mobile.mobile"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mobile.object', {
#             'object': obj
#         })