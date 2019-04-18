# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Checkin',
    'summary': 'Check-in',
    'license': 'AGPL-3',
    'sequence': 1,
    'description': """
        Mobile Check-in
    """,
    'website': 'https://dnpcorp.vn',
    'depends': ['base'],
    'data': [
        'security/checkin_security.xml',
        'security/ir.model.access.csv',
        'security/ir_rule.xml',
        'views/checkin_views.xml',
        'views/menu.xml'
    ],
    'css': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
