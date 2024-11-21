from django.contrib import admin
from . models import Service, Slider, Featured

# Register your models here.
admin.site.register(Slider)
admin.site.register(Service)
admin.site.register(Featured)

