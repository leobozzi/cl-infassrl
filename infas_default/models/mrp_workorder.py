# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.exceptions import ValidationError, UserError
from odoo.tools.translate import _


class MrpWorkOrder(models.Model):
    _inherit = 'mrp.workorder'
    _description = "mrp.workorder"
    _order = "sequence, id"

    sequence = fields.Integer(
        'Sequence', default=1,
        help="Gives the sequence order when displaying.")