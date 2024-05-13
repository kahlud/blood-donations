# -*- coding: utf-8 -*-
# from odoo import http


# class BloodDonation(http.Controller):
#     @http.route('/blood_donation/blood_donation', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/blood_donation/blood_donation/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('blood_donation.listing', {
#             'root': '/blood_donation/blood_donation',
#             'objects': http.request.env['blood_donation.blood_donation'].search([]),
#         })

#     @http.route('/blood_donation/blood_donation/objects/<model("blood_donation.blood_donation"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('blood_donation.object', {
#             'object': obj
#         })
