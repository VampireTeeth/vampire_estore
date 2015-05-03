from django.shortcuts import render
from products.models import Product

# Create your views here.
def home(request):
  products = Product.objects.all()
  template = 'products/home.html'
  ctx = {'products' : products}
  return render(request, template, ctx)


def all(request):
  products = Product.objects.all()
  ctx = {'products' : products}
  template = 'products/all.html'
  return render(request, template, ctx)
