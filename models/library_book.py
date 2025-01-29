from odoo import fields, models, api

class Book(models.Model):
    _name = 'library.book'
    
    name = fields.Char(required=True, string="Book name")
    isbn = fields.Char(required=True, string="ISBN", index=True)
    author = fields.Char()
    publication_date = fields.Date()
    loan_ids = fields.One2many('library.loan', 'book_id')
    is_loaned = fields.Boolean(compute='_compute_is_loaned', default=False)
    
    _sql_constraints = [
        ('check_isbn', 'UNIQUE(isbn)', 'The ISBN must be unique')
    ]
    
    @api.depends('loan_ids')
    def _compute_is_loaned(self):
        for book in self:
            if 'pending' in book.loan_ids.mapped('status'):
                book.is_loaned = True
            else:
                book.is_loaned = False
            