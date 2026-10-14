
from django.db import models
from django.urls import reverse


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def get_url(self):
        return reverse(
            'products_by_category',
            args=[self.slug]
        )

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    images = models.ImageField(
        upload_to='products/',
        blank=True
    )

    stock = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    def get_url(self):
        return reverse(
            'product_detail',
            args=[self.category.slug, self.slug]
        )

    @property
    def in_stock(self):
        return self.stock > 0 and self.is_available

    def __str__(self):
        return self.product_name
