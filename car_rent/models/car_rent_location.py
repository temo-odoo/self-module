from odoo import models,fields

class CarLocation(models.Model):
    _name="car.rent.location"
    _description="Car Locations"

    name=fields.Char("Name",required=True)
    location_ids=fields.One2many('car.rent.info','loc_id')

