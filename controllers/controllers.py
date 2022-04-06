# -*- coding: utf-8 -*-
from odoo import http


# class Environment(http.Controller):
#     @http.route('/environment/environment', auth='public')
#     def index(self, **kw):
#         return "Hello, world"
#
#     @http.route('/environment/environment/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('environment.listing', {
#             'root': '/environment/environment',
#             'objects': http.request.env['environment.environment'].search([]),
#         })
#
#     @http.route('/environment/environment/objects/<model("environment.environment"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('environment.object', {
#             'object': obj
#         })

class Organization(http.Controller):
    @http.route('/organization/organization' , auth='public')
    def index(self,**kw):
        return "Hi, Team"

    @http.route('/organization/organization/objects', auth='public')
    def list(self, **kw):
        return http.request.render('organization.listing', {
            'root': '/organization/organization',
            'objects': http.request.env['organization.organization'].search([]),
        })
    @http.route('/organization/organization/objects/<model("organization.organization"):obj', auth='public')
    def object(self, obj, **kw):
        return http.request.render('organization.object', {
            'object' : obj
        })