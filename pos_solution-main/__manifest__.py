# -*- coding: utf-8 -*-
{
    'name': "POS Payment QR Code",

    'summary': "POS Payment QR Code",

    'description': """
        Long description of module's purpose
    """,
    
    "license": "AGPL-3",
    'author': "AACC Thailand.",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Point of Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/res_config_settings.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/res_company.xml',
        'views/assets.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'qweb': [
        'static/src/view/view.xml',
    ],

    "images": ["static/description/image2.png",],
    "price": 27,
    "Currency": "EUR",
}
