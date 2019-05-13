# -*- coding: utf-8 -*-

{
    'name': "di_mapama",

    'summary': """
        Modulo para enviar Di's generados al servidor de MAPAMA""",

    'description': """
        Comunicación Mapama
    """,

    'author': "Pedro Guirao",
    'website': "https://ingenieriacloud.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','x_di'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/button_view.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'installable': True,
    'application': True,
    'auto_install': False,
}