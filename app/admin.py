from django.contrib import admin
from app.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
