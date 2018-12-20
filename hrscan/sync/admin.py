from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import *

admin.site.register(Degree)
admin.site.register(Institute)
admin.site.register(Course)
admin.site.register(Company)
admin.site.register(Exp)
admin.site.register(Quality)
admin.site.register(Artist)
admin.site.register(Cv)
admin.site.register(Requirement)