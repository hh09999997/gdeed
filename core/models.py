from django.db import models

# 🏠 النماذج الأساسية للواجهة العامة (Home, Contact, About)
class ContactMessage(models.Model):
    """نموذج بسيط لتخزين رسائل التواصل من المستخدمين."""
    name = models.CharField(max_length=100, verbose_name="الاسم")
    email = models.EmailField(verbose_name="البريد الإلكتروني")
    subject = models.CharField(max_length=200, verbose_name="الموضوع")
    message = models.TextField(verbose_name="الرسالة")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإرسال")

    def __str__(self):
        return f"{self.name} - {self.subject}"

    class Meta:
        verbose_name = "رسالة تواصل"
        verbose_name_plural = "رسائل التواصل"
        ordering = ['-created_at']
