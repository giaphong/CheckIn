from odoo import  api, fields , models

class CheckIn(models.Model):
    _name='mobile.checkin'
    _description = 'Mobile CheckIn'


    name = fields.Char("Name", compute='_compute_name')
    timestamp = fields.Datetime('Timestamp', required = True)
    lat = fields.Float('Latitude', digits=(19, 16), required = True)
    lng = fields.Float('Longitude', digits=(19, 16), required = True)
    photo = fields.Char('Photo', required = True)
    user_id = fields.Many2one('res.users', string = u'User')


    @api.multi
    @api.depends('create_uid', 'timestamp')
    def _compute_name(self):
        for c in self:
            c.name = ((c.create_uid.name + ' - ') if c.create_uid else '') + (str(c.timestamp) if c.timestamp else '')
