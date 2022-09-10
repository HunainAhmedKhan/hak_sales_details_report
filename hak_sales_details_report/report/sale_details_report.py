# -*- coding: utf-8 -*-

import time
from odoo import api, models
from dateutil.parser import parse
from odoo.exceptions import UserError

class ReportInvoices(models.AbstractModel):
    _name = 'report.hak_sales_details_report.sale_details_tax_report'
    _description = 'Sales Details Tax Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        active_model = self.env.context.get('active_model')
        docs = self.env[active_model].browse(self.env.context.get('active_id'))
        orders = self.env['pos.order'].search([('date_order', '>=', docs.start_date),('date_order', '<=', docs.end_date),('state','not in',['draft','cancel'])])
        if orders:
            return {
                'docs': docs,
                'orders': orders,
            }
        else:
            raise UserError("No Orders Found")
