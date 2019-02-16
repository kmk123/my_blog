from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['id','auther','title','content','date_posted',]

admin.site.register(Post,PostAdmin)
#admin.site.register(Post)