from django.contrib import admin
from users.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','user','image']

admin.site.register(Profile,ProfileAdmin)