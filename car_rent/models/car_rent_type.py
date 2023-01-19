from odoo import models, fields

class CarType(models.Model):
    _name="car.rent.type"
    _description="Car Rent Types"

    name=fields.Char("Name",required=True)
    description=fields.Text("Description")