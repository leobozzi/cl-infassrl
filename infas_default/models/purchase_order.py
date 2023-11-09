# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.exceptions import ValidationError, UserError
from odoo.tools.translate import _


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    _description = "purchase.order"

    def write(self, vals):
        res = super(PurchaseOrder, self).write(vals)

        for rec in self:
            if 'state' in vals:
                if vals['state'] in ['done', 'purchase']:
                    for order_line in rec.order_line:
                        if order_line.product_id.categ_id.property_cost_method == 'standard' and order_line.price_unit != 0.0:
                            product_company_price = order_line.price_unit / rec.currency_id.rate 
                            order_line.product_id.standard_price = product_company_price * order_line.product_id.currency_id.rate
        return res