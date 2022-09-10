# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class SaleDetialsTaxReport(models.TransientModel):
    _name = "invoice.outstanding"
    _description = "Sale Details Tax Report"

    start_date = fields.Date(string='From Date', required='1', help='select start date')
    end_date = fields.Date(string='To Date', required='1', help='select end date')

    def check_report(self):
        data = {}
        data['form'] = self.read(['start_date', 'end_date'])[0]
        return self._print_report(data)

    def _print_report(self, data):
        data['form'].update(self.read(['start_date', 'end_date'])[0])
        return self.env.ref('hak_sales_details_report.action_sale_details_tax_report').report_action(self, data=data, config=False)


