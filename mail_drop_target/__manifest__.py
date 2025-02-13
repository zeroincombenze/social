# -*- coding: utf-8 -*-
# Copyright 2018 Therp BV <https://therp.nl>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Drag & drop emails to Odoo",
    "version": "10.0.1.0.1",
    "author": "Therp BV,Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "category": "Discuss",
    "summary": "Attach emails to Odoo by dragging them from your desktop",
    'website': 'https://github.com/OCA/social',
    "depends": [
        'mail',
        'web_drop_target',
    ],
    "data": [
        'views/templates.xml',
    ],
}
