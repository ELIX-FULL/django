from django.db import models

# models.py, admin.py, views.py, urls.py
class CategoryModel(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class ProductModel(models.Model):
    title = models.CharField(max_length=50, verbose_name='Назавание')
    price = models.IntegerField(default=0)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, null=True, blank=True)
    image = models.FileField(upload_to='products')
    descriptions = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'


class FormModel(models.Model):
    username = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    comment = models.TextField()

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Form'
        verbose_name_plural = 'Forms'
