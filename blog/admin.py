from django.contrib import admin
from blog.models import BlogModel, ProfileModel
from blog.models import Comments
# Register your models here.




#this is for displaying listview in admin panel
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','created_at')

admin.site.register(BlogModel, BlogModelAdmin)
admin.site.register(ProfileModel)
admin.site.register(Comments) 