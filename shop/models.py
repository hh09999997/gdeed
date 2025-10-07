from django.db import models
from cloudinary.models import CloudinaryField
from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.text import slugify


# 🏷️ نموذج التصنيفات
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم التصنيف")
    slug = models.SlugField(max_length=120, unique=True, blank=True, verbose_name="المعرف النصي")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "تصنيف"
        verbose_name_plural = "التصنيفات"
        ordering = ['name']

# 📦 نموذج المنتجات
class Product(models.Model):
    """منتج بسيط لعرضه في المتجر."""
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="التصنيف"
    )
    name = models.CharField(max_length=200, verbose_name="اسم المنتج")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")
    description = models.TextField(blank=True, null=True, verbose_name="الوصف")
    image = CloudinaryField(
        folder='products',
        null=True,
        blank=True,
        verbose_name="صورة المنتج"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"
        ordering = ['-created_at']
