{
    'name': 'Library Management',
    'version': '1.0.0',
    'summary': 'Basic library management module',
    'description': 'A module to manage books for a library system',
    'author': 'Grupo Hernández S.U.R.L',
    'company': 'Grupo Hernández S.U.R.L',
    'category': 'Education',
    'depends': ['base', 'mail', 'portal'],
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
        'data/library_loan_cron.xml',
        'data/mail_template.xml',
        'views/portal_templates.xml',
        # Wizards
        'wizard/report_loan_wizard.xml',
        # Reports
        'report/library_loan_report.xml',
        'report/library_loan_template.xml',
        'report/loan_pdf_report.xml',
    ],
    'demo': [
        'demo/demo.xml'
    ]
}