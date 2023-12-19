# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.exceptions import ValidationError, UserError
from odoo.tools.translate import _


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'
    _description = "stock.move.line"

    warranty_exp_data = fields.Date(
        related="lot_id.warranty_exp_date"
    )
    