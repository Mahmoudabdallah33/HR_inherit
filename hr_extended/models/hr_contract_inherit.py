from odoo import api, models, fields


class HrContractInherit(models.Model):
    _inherit = ['hr.contract.history']

    xx_hiring_documnet_ids = fields.Many2many('hr.hiring.document', string = 'Hiring Documents')
