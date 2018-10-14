from django.contrib import admin
from .models import ItUser, Specialty
from django.contrib.auth.admin import UserAdmin


admin.site.register(ItUser, UserAdmin)
admin.site.register(Specialty)
