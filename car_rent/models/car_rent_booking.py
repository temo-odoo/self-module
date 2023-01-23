from odoo import models, fields
from datetime import date

class CarRentBooking(models.Model):
    _name="car.rent.booking"
    _description="Car Rent Booking Details"
    _rec_name="name"

    from_date=fields.Date('From Date',copy=False,default=date.today())
    to_date=fields.Date('To Date',copy=False)
    name=fields.Char(default="Booking")
    
    def action_check_availability(self):
        for record in self:
           pass

    def action_cancel(self):
        for record in self:
            pass