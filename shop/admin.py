from django.contrib import admin
from .models import Category, Product

# فئة المنتج
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """إدارة فئات المنتجات"""
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}  # إنشاء slug تلقائي من الاسم
    search_fields = ('name',)

# المنتج
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """إدارة المنتجات"""
    list_display = ('name', 'category', 'price', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
