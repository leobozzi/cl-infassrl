# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.exceptions import ValidationError, UserError
from odoo.tools.translate import _


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    _description = "product.template"

    document_count = fields.Integer(compute='_compute_document_count')

    def _get_document_folder(self):
        return self.company_id.product_folder if self.company_id.documents_product_settings else False
        
    
    def _get_product_document_domain(self):
        self.ensure_one()
        product_template_domain = [('product_template_id', '=', self.id)]
        return product_template_domain

    def _compute_document_count(self):
        # Method not optimized for batches since it is only used in the form view.
        for rec in self:
            rec.document_count = self.env['documents.document'].search_count(rec._get_product_document_domain())
    
    def action_open_documents(self):
        self.ensure_one()
        product_template_folder = self._get_document_folder()
        action = self.env['ir.actions.act_window']._for_xml_id('documents.document_action')
        # Documents created within that action will be 'assigned' to the product template
        # Also makes sure that the views starts on the product_template_folder
        action['context'] = {
            'default_product_template_id': self.id,
            'searchpanel_default_folder_id': product_template_folder and product_template_folder.id,
        }
        action['domain'] = self._get_product_document_domain()
        return action
