# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.exceptions import ValidationError, UserError
from odoo.tools.translate import _


class Documents(models.Model):
    _inherit = 'documents.document'
    _description = "documents.document"

    product_template_id = fields.Many2one(
        comodel_name='product.template',
        string="Product Template",
        tracking=True
    )

   