from odoo import fields, models, api

class ResPartner(models.Model):
    _inherit = "res.partner"
    
    loan_ids = fields.One2many('library.loan', 'reader_id')
    pending_loan_ids = fields.One2many(compute='_compute_pending_loan')
    
    @api.depends('loan_ids.status')
    def _compute_pending_loan(self):
        for reader in self:
            pending_loans = reader.loan_ids.filtered(lambda loan: loan.status == 'pending')
            reader.pending_loan_ids = [(6, 0, pending_loans.ids)]
            
    def action_library_stat_button(self):
        self.ensure_one()
        xml_id = self.env.context.get('xml_id')
        if xml_id:
            res = self.env['ir.actions.act_window']._for_xml_id(xml_id)
            return res
        return False