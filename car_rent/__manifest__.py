{
    'name': "Car Rent",
    'version':'1.0',
    'depends': ['mail'],
    'author': "Tejas Modi(temo)",
    'category': 'Sales',
    'description': "This is Car Rental portal module",
    'summary':'hello',
    'installable': True,
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'views/car_info_menu.xml',
        'views/car_info_views.xml',
        'views/car_booking_views.xml',
        'views/car_type_views.xml',
        
    ]
}