# -*- coding: utf-8 -*-
# from odoo import http


# class InheritCrm(http.Controller):
#     @http.route('/inherit_crm/inherit_crm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inherit_crm/inherit_crm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('inherit_crm.listing', {
#             'root': '/inherit_crm/inherit_crm',
#             'objects': http.request.env['inherit_crm.inherit_crm'].search([]),
#         })

#     @http.route('/inherit_crm/inherit_crm/objects/<model("inherit_crm.inherit_crm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inherit_crm.object', {
#             'object': obj
#         })
