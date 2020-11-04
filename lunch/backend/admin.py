from django.contrib import admin

# Register your models here.
from .models import User, Test


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    pass
