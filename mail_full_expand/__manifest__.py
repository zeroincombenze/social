# -*- coding: utf-8 -*-
# © 2014-2015 Grupo ESOC <http://www.grupoesoc.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Mail full expand",
    "summary": "Expand mail in a big window",
    "version": "10.0.1.0.1",
    "category": "Social Network",
    "website": "https://github.com/OCA/social",
    "author": "Grupo ESOC, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    'installable': True,
    "depends": [
        "mail",
        "web",
    ],
    "data": [
        "views/mail_full_expand.xml",
        "views/assets.xml",
    ],
    "qweb": [
        "static/src/xml/mail_full_expand.xml",
    ],
}
