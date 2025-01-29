from odoo import fields, models

class Loan(models.Model):
    _name = 'library.loan'
    
    book_id = fields.Many2one('library.book', string='Book')
    reader_id = fields.Many2one('res.partner', string='Reader name')
    loan_date = fields.Date()
    return_deadline = fields.Date()
    status = fields.Selection(selection=[('draft', 'Draft'), ('pending', 'Pending'), ('returned', 'Returned')], default='draft')
    
    def action_pending(self):
        for loan in self:
            loan.status = 'pending'
            
    def action_return(self):
        for loan in self:
            loan.status = 'returned'