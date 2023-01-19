from odoo import models,fields

class CarReservation(models.Model):
    _name="car.rent.reservation"
    _description="Car Reservation"


    user_id=fields.Many2one('res.users',string='Customer Name',default=lambda self: self.env.user)
    rent_type=fields.Selection(selection=[('kilometers','Kilometers'),('hours','Hours'),('days','Days')],default='kilometers')
  