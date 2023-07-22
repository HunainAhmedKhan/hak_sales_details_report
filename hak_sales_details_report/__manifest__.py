# -*- coding: utf-8 -*-

{
    'name': "Sales Details Tax Report",
    'author': "HAK Technologies",
    'category': 'point_of_sale',
    'summary': """Sales Details Tax Report within the particular date period""",
    'website': 'http://www.haksolutions.com',
    'license': 'AGPL-3',
    'description': """
""",
    'version': '15.0.1.0',
    'depends': ['base','account','point_of_sale'],
    'data': ['security/ir.model.access.csv',
             'report/sale_detail.xml',
             'report/sale_details_tax_report.xml',
             ],

    'installable': True,
    'images': ['static/description/icon.png'],
    'application': True,
    'auto_install': False,
}
