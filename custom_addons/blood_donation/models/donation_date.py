from odoo import models,fields, api

class date(models.Model):
    _name = 'donor_data.donation_date'

    date_time_donation = fields.Date(string='Fecha de donación')
    type_donation = fields.Selection([('sangre', 'Sangre'), ('medula', 'Médula')], string='Tipo de donación')
    donor_id= fields.Many2one('blood_donation.donor_data', string='Donador')