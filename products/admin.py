from django.contrib import admin
from .models import *

# Register your models here.
admin.site.site_header = "BedGear Dashboard"

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(product_category)
admin.site.register(contact_us)
admin.site.register(OrderItem)
admin.site.register(DiliveryAddress)
admin.site.register(Type)


