from odoo import models, fields, api, _

class LoanWizard(models.TransientModel):
    _name =  'loan.wizard'
    
    loan_ids = fields.Many2many(comodel_name='library.loan', string='Courses')
    status = fields.Selection(selection=[('draft', 'Draft'), ('pending', 'Pending'), ('returned', 'Returned')], default='pending')
    
    def print_pdf_report(self):
        
        data = {
            'status': self.status,
            'loan_ids': self.loan_ids.ids,
        }
        
        return self.env.ref('library_management.report_library_loan_wz').report_action(self, data)