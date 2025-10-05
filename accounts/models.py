from django.db import models
from django.contrib.auth.models import User

# 👤 نموذج ملف المستخدم الإضافي
class Profile(models.Model):
    """معلومات إضافية للمستخدمين المسجلين."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="رقم الجوال")
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name="العنوان")
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name="المدينة")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "ملف مستخدم"
        verbose_name_plural = "ملفات المستخدمين"
