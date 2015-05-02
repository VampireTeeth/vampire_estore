from django.contrib import admin

# Register your models here.
from products.models import Product


class ProductAdmin (admin.ModelAdmin):
  date_hierarchy = 'created_time'
  search_fields = ['title', 'description']
  list_display = ['title', 'price', 'active', 'updated_time', 'created_time']
  list_editable = ['price', 'active']
  list_filter = ['price', 'active']
  readonly_fields = ['created_time', 'updated_time']
  prepopulated_fields = {'slug' : ('title',)}
  class Meta:
    model = Product

admin.site.register(Product, ProductAdmin)
