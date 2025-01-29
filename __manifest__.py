{
    'name': 'Library Management',
    'version': '1.0.0',
    'summary': 'Basic library management module',
    'description': 'A module to manage books for a library system',
    'author': 'Grupo Hernández S.U.R.L',
    'company': 'Grupo Hernández S.U.R.L',
    'category': 'Education',
    'depends': ['base'],
    'license': 'OPL-1',
    'application': True,
    'installable': True,
    'auto_install': False,
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/library_book_views.xml',
        'views/library_loan_views.xml',
        'views/library_menus.xml',
        'views/res.partner.views.xml',
        'report/library_loan_template.xml',
        'report/library_loan_report.xml',
    ],
    'demo': [
        'demo/demo.xml'
    ]
}