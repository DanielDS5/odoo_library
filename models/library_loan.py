from odoo import fields, models, api
from odoo.exceptions import ValidationError
from datetime import timedelta

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
            
    @api.constrains('loan_date', 'return_deadline')
    def _check_dates(self):
        for record in self:
            if record.return_deadline and record.return_deadline < record.loan_date:
                raise ValidationError("The return deadline cannot be earlier than the loan date.")
            
    def send_loan_reminders(self):
        today = fields.Date.today()
        reminder_date = today + timedelta(days=3)
        loans = self.search([('return_deadline', '=', reminder_date), ('status', '=', 'pending')])
        for loan in loans:
            template_id = self.env.ref('library_management.mail_template_loan_reminder').id
            self.env['mail.template'].browse(template_id).send_mail(loan.id, force_send=True)