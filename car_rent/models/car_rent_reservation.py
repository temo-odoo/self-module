from odoo import models,fields

class CarReservation(models.Model):
    _name="car.rent.reservation"
    _description="Car Reservation"
    _rec_name="user_id"

    user_id=fields.Many2one('res.users',string='Customer Name',default=lambda self: self.env.user)
    rent_type=fields.Selection(selection=[('kilometers','Kilometers'),('hours','Hours'),('days','Days')],default='kilometers')
    state=fields.Selection(selection=
    [('draft','Draft'),('confirm','Confirm'),('deposit','Deposit'),('in progress','In Progress'),('finish','Finish'),('payment done','Payment Done')],default='draft')
    #Rent Details
    rent_per_km=fields.Float('Rent Per Km',default = 20.0)
    rent_per_hours=fields.Float('Rent Per Hours',default = 150.0)
    rent_per_day=fields.Float('Rent Per Day',default = 2000.0)