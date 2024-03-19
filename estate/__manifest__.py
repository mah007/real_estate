# -*- coding: utf-8 -*-
{
    'name': "Real Estate App",

    'summary': "Real Estate App ",

    'description': """
Real Estate App
    
    """,

    'author': "Kamatech",
    'website': "https://www.kama.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','product','board'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        "views/estate_property_offer_views.xml",
        "views/estate_property_tag_views.xml",
        "views/estate_property_type_views.xml",
        "views/estate_property_views.xml",
        "views/res_users_views.xml",
        "views/estate_menus.xml",
        "report/template.xml",
        "report/report_doc.xml",
        'views/res_settings.xml',
        # "report/estate_report_views.xml",
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'sequence': 1,
    'application': True,
    'license': 'LGPL-3',

}

