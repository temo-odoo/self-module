from odoo import models, fields
from datetime import date

class CarRentInfo(models.Model):
    _name="car.rent.info"
    _description="Car Information"

    name=fields.Char("Name",required=True)
    license_plate=fields.Char('License Plate')
    postcode=fields.Char('Postcode')
    loc_id=fields.Many2one('car.rent.location',string="Location")
    assignation_date=fields.Date('Assignation Date',copy=False,default=date.today())
    available=fields.Boolean('Available')
#Driver Details
    driver=fields.Boolean('Driver')
    driver_id=fields.Many2one('res.partner','Driver Name')
    
#Vehicle
    deposit=fields.Integer(string="Deposit")
    last_odometer=fields.Float('Last Odometer', required=True)
    chassis_number=fields.Integer('Chassis Number')
    purchase_value=fields.Integer('Purchase Value')
    # car_manager=fields.Many2one()

#Model
    type_id=fields.Many2one('car.rent.type',string='Car Type')
    seats_number=fields.Integer('Seats Number')
    colour=fields.Char('Colour')
    model_year=fields.Integer('Model Year')
    transmission_type=fields.Selection(selection=[('manual','Manual'),('automatic','Automatic')])

#Engine
    horse_power=fields.Integer('Horse Power')
    fuel_type=fields.Selection(selection=[('diesel','Diesel'),('petrol','Petrol'),('cng','Cng')])

   