
from datetime import datetime, timedelta
from odoo import models, fields, api

class donor(models.Model):
    _name = 'blood_donation.donor_data'
    name_donor = fields.Char(string='Nombre')
    last_name_donor = fields.Char(string='Apellido')
    addres_donor= fields.Char(string='Domicilio')
    phone_donor = fields.Char(string='Telefono')
    email_donor = fields.Char(string='Email')
    donation_date= fields.One2many('donor_data.donation_date', 'donor_id', string='Donaciones')
    donation_six_months = fields.Boolean(string='Donacion hace seis meses', compute='_compute_donation_six_months', store=True)


    @api.model
    def get_last_donation(self):
        last_donations = {}    
        for donor in self.search([]):
            last_donation = donor.donation_date and max(donor.donation_date, key=lambda d: d.date_time_donation)
            if last_donation:
                last_donations[donor.id] = last_donation.date_time_donation
        return last_donations


    @api.model
    def _compute_donation_six_months(self):
        last_donations = self.get_last_donation()
        fecha_limite = datetime.now() - timedelta(days=180)
        for donor_id, last_donation_date in last_donations.items():
            if last_donation_date <= fecha_limite:
                donor = self.browse(donor_id)
                donor.donation_six_months = True
            else:
                donor = self.browse(donor_id)
                donor.donation_six_months = False

