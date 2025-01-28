from odoo import fields, models

class Loan(models.Model):
    _name = 'library.loan'
    
    book_id = fields.Many2one('library.book', string='Libro')
    reader_id = fields.Many2one('res.partner', string='Nombre del lector')
    loan_date = fields.Date(string='Fecha de préstamo')
    return_date = fields.Date(string='Fecha límite de devolución')
    status = fields.Selection(selection=[('draft', 'Borrador'), ('pending', 'Pendiente'), ('returned', 'Devuelto')], string="Estado", default='draft')
    
    def action_pending(self):
        for loan in self:
            loan.status = 'pending'
            
    def action_return(self):
        for loan in self:
            loan.status = 'returned'