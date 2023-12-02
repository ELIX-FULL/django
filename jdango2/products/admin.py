from django.contrib import admin

from jdango2.products.models import ProductModel, FormModel, CategoryModel


# 1) python manage.py startapp products
# 2) products поставить в settings.py installed apps
@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'created_at']
    search_fields = ['title', 'price']
    list_filter = ['created_at']


@admin.register(FormModel)
class FormModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'age', 'comment']