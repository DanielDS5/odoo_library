from odoo import fields, models, api

class Book(models.Model):
    _name = 'library.book'
    
    name = fields.Char(required=True, string="Book name")
    isbn = fields.Char(required=True, string="ISBN", index=True)
    author = fields.Char()
    publication_date = fields.Date()
    
    _sql_constraints = [
        ('check_isbn', 'UNIQUE(isbn)', 'The ISBN must be unique')
    ]