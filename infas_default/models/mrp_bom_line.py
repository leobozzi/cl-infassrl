# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.exceptions import ValidationError, UserError
from odoo.tools.translate import _


class MrpBomLine(models.Model):
    _inherit = 'mrp.bom.line'
    _description = "mrp.bom.line"

    tecnical_data = fields.Char(
        string="Detalle Técnico"
    )