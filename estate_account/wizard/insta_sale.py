# installment
from odoo import api, fields, models, Command, _
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, ValidationError


class RealEstateInstallmentWizard(models.TransientModel):
    _name = 'estat.payment.wizard'
    _description = 'Create Automatic installment invoices'

    insta_periods = fields.Selection([
        ('1', ' instant'),
        ('6', ' 6 Months'),
        ('12', ' 12 Months'),
        ('24', '24 Months')
    ],
        string='installments periods',
        default='1',
    )

    def action_sold_insta(self):

        property_id = self.env.context.get('active_id')
        props = self.env['estate.property'].browse(property_id)
        if props.approval == 'approved':

            journal = self.env["account.journal"].search([("type", "=", "sale")], limit=1)
            # Another way to get the journal:
            # journal = self.env["account.move"].with_context(default_move_type="out_invoice")._get_default_journal()
            if self.insta_periods:
                no = int(self.insta_periods)
                for i in range(0, no):
                    for prop in props:
                        invoiced = self.env["account.move"].create(
                            {
                                "partner_id": prop.buyer_id.id,
                                "move_type": "out_invoice",
                                "invoice_date_due": date.today() + relativedelta(months=i + 1),
                                "journal_id": journal.id,
                                "invoice_line_ids": [
                                    Command.create({
                                        "name": prop.name,
                                        'product_id': prop.property_type_id.product_id.id,
                                        "quantity": 1.0,
                                        "price_unit": (prop.selling_price) / no,
                                    }),
                                    Command.create({
                                        "name": "Administrative fees",
                                        'product_id': 4,
                                        "quantity": 1.0,
                                        "price_unit": 100.0,
                                    }),
                                ],
                            }
                        )
                        prop.action_sold()
        else:
            raise UserError("Manager Must approve this .")
