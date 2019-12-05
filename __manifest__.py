# -*- coding: utf-8 -*-
{
    'name': "purchase_update",

    'summary': """
        Modifica el formulario de compra para que el usuario estandart de compras no pudo confirmar el pedido""",

    'description': """
        Modifica el formulario de compra para que el usuario estandart de compras no pudo confirmar el pedido
    """,

    'author': "Fimar",
    'website': "http://www.fimarcorp.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/purchase_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}