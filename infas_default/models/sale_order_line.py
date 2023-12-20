# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.exceptions import ValidationError, UserError
from odoo.tools.translate import _

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.onchange('price_unit')
    def onchange_custom_price(self):
        if self.product_id and not 'pricelist' in self.env.context and not self.env.user.has_group("infas_default.group_allow_price_change"):
            raise UserError(_('You are not allowed to change price'))