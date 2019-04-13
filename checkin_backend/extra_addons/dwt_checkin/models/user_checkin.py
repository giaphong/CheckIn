from odoo import  api, fields , models

class UserCheckIn(models.Model):
    _name='mobile.user_checkin'
    _description = 'User CheckIn'


    name = fields.Char("Name", required = True)
    email = fields.Char("Email", required = True)
    password = fields.Char("Password", required = True)
