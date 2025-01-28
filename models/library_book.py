from odoo import fields, models, api

class Book(models.Model):
    _name = 'library.book'
    
    name = fields.Char(required=True, string="Nombre del Libro")
    isbn = fields.Char(required=True, string="ISBN", index=True)
    author = fields.Char(string="Autor")
    publication_date = fields.Date(string="Fecha de Publicación")
    
    _sql_constraints = [
        ('check_isbn', 'UNIQUE(isbn)', 'The ISBN must be unique')
    ]