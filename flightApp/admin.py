from django.contrib import admin

from .models import Passenger

# Register your models here.
class PassengerAdmin(admin.ModelAdmin):
    list_display = ("firstName", "lastName", "middleName", "email", "phone")
    list_per_page = 20


admin.site.register(Passenger, PassengerAdmin)
