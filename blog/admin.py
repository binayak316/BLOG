from django.contrib import admin
from blog.models import BlogModel
# Register your models here.




#this is for displaying listview in admin panel
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','created_at')

admin.site.register(BlogModel, BlogModelAdmin)