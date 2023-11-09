# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.exceptions import ValidationError, UserError
from odoo.tools.translate import _


class StockMove(models.Model):
    _inherit = 'stock.move'
    _description = "stock.move"

    tecnical_data = fields.Char(
        related="bom_line_id.tecnical_data"
    )
    