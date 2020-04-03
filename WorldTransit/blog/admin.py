from django.contrib import admin

from .models import Users, Questions, Response


admin.site.register(Users)
admin.site.register(Questions)
admin.site.register(Response)
