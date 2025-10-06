"""
URL configuration for gdeed project.

The `urlpatterns` list routes URLs to views.
Documentation: https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# ----------------------------------------
# 🔹 تعريف المسارات العامة للتطبيقات
# ----------------------------------------
urlpatterns = [
    # لوحة التحكم الإدارية
    path('admin/', admin.site.urls),

    # التطبيق الأساسي (الصفحة الرئيسية، من نحن، تواصل معنا)
    path('', include('core.urls')),

    # المتجر (المنتجات، السلة، الطلبات)
    path('shop/', include('shop.urls')),

    # الحسابات (تسجيل الدخول، التسجيل، لوحة المستخدم)
    path('accounts/', include('accounts.urls')),
]

# ----------------------------------------
# 🖼️ إعداد عرض الملفات الثابتة والمرفوعة أثناء التطوير
# ----------------------------------------
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

# ----------------------------------------
# ⚙️ تخصيص عناوين لوحة الإدارة (اختياري)
# ----------------------------------------
admin.site.site_header = "لوحة إدارة مركز الديكور العصري"
admin.site.site_title = "إدارة الموقع"
admin.site.index_title = "مرحبًا بك في لوحة التحكم"
