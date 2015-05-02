from django.db import models

# Create your models here.
class Product(models.Model):
  title = models.CharField(max_length=120)
  description = models.TextField(null=True, blank=True)
  price = models.DecimalField(max_digits=100, decimal_places=2, default=29.99)
  sale_price = models.DecimalField(max_digits=100, decimal_places=2, null=True)
  slug = models.SlugField()
  created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
  updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)
  active = models.BooleanField(default=True)

  def __unicode__(self):
    return self.title

  def get_price(self):
    return self.price
