from odoo import fields, models, api

class ResPartner(models.Model):
    _inherit = "res.partner"
    
    loan_ids = fields.One2many('library.loan', 'reader_id', string='Properties', domain="[('status', '=', 'pending')]")
    loan_count = fields.Integer(compute='_compute_loan_count')
    
    @api.depends('loan_ids')
    def _compute_loan_count(self):
        for reader in self:
            reader.loan_count = len(reader.loan_ids)
            
    def action_library_stat_button(self):
        self.ensure_one()
        xml_id = self.env.context.get('xml_id')
        if xml_id:
            res = self.env['ir.actions.act_window']._for_xml_id(xml_id)
            return res
        return False