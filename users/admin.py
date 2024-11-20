from django.contrib import admin

# Register your models here.
from .models import User

class UserAdmin(admin.ModelAdmin):
    model = User
    search_fields = ['username','first_name', 'last_name', 'email','telefon']

admin.site.register(User, UserAdmin)
