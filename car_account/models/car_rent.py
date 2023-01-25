from odoo import  models,Command

class CarRent(models.Model):
    _inherit ="car.rent.booking"

    def action_accepted(self):
        for record in self:
            self.env["account.move"].create(
            {
                "partner_id":record.buyer_id.id,
                "move_type":'out_invoice',
                "invoice_line_ids":[
                    Command.create({
                        'name':record.name,
                        # 'quantity':0.06,
                        'price_unit':record.total_rent   

                      }),
                    Command.create( {
                        'name':'Administrative fees',
                        'price_unit':100
                    })],
            }
        )
            return super().action_accepted()