from django.contrib import admin

# Register your models here.
from .models import User, Branch, Customer, Booking

admin.site.register(User)
admin.site.register(Branch)
admin.site.register(Customer)
admin.site.register(Booking)