from odoo import models, fields, api, _

class LibraryLoanReport(models.AbstractModel):
    _name = 'report.library_management.report_library_loan_wz_view'
    
    def _get_report_values(self, docids, data=None):
        
        status = data['status']
        loan_ids = data['loan_ids']
        
        docs = self.env['library.loan'].browse(loan_ids)
        
        
        return {
            'doc_ids': docs.ids,
            'doc_model': 'library.loan',
            'docs': docs,
            'data': data,
        }