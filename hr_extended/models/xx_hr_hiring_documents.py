from odoo import models, fields

class HrHiringDocument(models.Model):
    _name = 'hr.hiring.document'
    _description = 'HR Hiring Document'

    name = fields.Char(string='Name', required=True)
