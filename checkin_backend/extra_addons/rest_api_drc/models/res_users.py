# -*- coding: utf-8 -*-
import uuid
from openerp import fields, models


class ResUsers(models.Model):
    _inherit = "res.users"

    token = fields.Char(string='Token',copy=False)

    def get_user_access_token(self):
        return uuid.uuid4().hex
