from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """إدارة ملفات المستخدمين الإضافية"""
    list_display = ('user', 'phone', 'city', 'created_at')
    search_fields = ('user__username', 'phone', 'city')
    list_filter = ('city', 'created_at')
    readonly_fields = ('created_at',)
