from odoo import models, fields,api
from odoo.exceptions import ValidationError as ve
import datetime
from datetime import *

class CarRentBooking(models.Model):
    _name="car.rent.booking"
    _description="Car Rent Booking Details"
    _rec_name="name"

    from_date=fields.Date('From Date',copy=False,default=date.today())
    to_date=fields.Date('To Date',copy=False,default=date.today())
    name=fields.Char(default="Booking")
    # user_id=fields.Many2one('res.users',string='Customer Name',default=lambda self: self.env.user)
    buyer_id = fields.Many2one('res.partner', string='Customer Name')
    rent_type=fields.Selection(selection=[('kilometers','Kilometers'),('hours','Hours'),('days','Days')],default='kilometers')
    info_id=fields.Many2one("car.rent.info")
    hours_days=fields.Integer(required=True,string="Hours/Km")
    total_rent=fields.Float(compute="_rent_calculation",default=0.0)
    status=fields.Selection(string="status", selection=[('accepted','Accepted'),('refused','Refused')],tracking=True)
    date=fields.Date(default=date.today(),required=True)



    @api.depends('hours_days','from_date','to_date')
    def _rent_calculation(self):
        for record in self:
            if record.rent_type=='kilometers':
                record.total_rent=record.info_id.rent_per_km * record.hours_days
            
            elif record.rent_type=='hours':
                record.total_rent=record.info_id.rent_per_hours * record.hours_days
            
            else:
                a=(record.to_date-record.from_date).days
                record.total_rent=record.info_id.rent_per_day*a
                # print("-----------------------",a)

            
    @api.model
    def create(self, vals_list):
        check=self.env['car.rent.info'].browse(vals_list['info_id'])
        from_date=check.mapped('booking_ids.from_date')
        to_date=check.mapped('booking_ids.to_date')
        check_list=from_date + to_date
        # print("--------------------------------------------",vals_list['from_date'],"------",check_list)
        
        # print(type(a))
        if datetime.strptime(vals_list['from_date'], '%Y-%m-%d').date() in check_list or datetime.strptime(vals_list['to_date'], '%Y-%m-%d').date() in check_list: 
            raise ve("Date is Unavailable")
        return super().create(vals_list)

    def action_accepted(self):
        for record in self:
            record.status='accepted'
            record.info_id.state='booked'

    def action_refused(self):
        for record in self:
            self.status='refused'
   
    