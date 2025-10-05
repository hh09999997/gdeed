from django.db import models

# 🛍️ نموذج فئة المنتج
class Category(models.Model):
    """فئات المنتجات (مثل عطور، إلكترونيات، ملابس...)"""
    name = models.CharField(max_length=100, verbose_name="اسم الفئة")
    slug = models.SlugField(unique=True, verbose_name="المعرف النصي")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "فئة"
        verbose_name_plural = "الفئات"


# 📦 نموذج المنتج
class Product(models.Model):
    """منتج بسيط لعرضه في المتجر."""
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=200, verbose_name="اسم المنتج")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")
    description = models.TextField(blank=True, null=True, verbose_name="الوصف")
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="صورة المنتج")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"
        ordering = ['-created_at']
