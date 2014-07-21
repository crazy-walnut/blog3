from django.contrib import admin

# Register your models here.
from blog.models import User
admin.site.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ('name', 'headImg')
	list_filter = ('name',)
	date_hierarchy = 'name'