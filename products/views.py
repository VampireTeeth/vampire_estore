from django.shortcuts import render
from products.models import Product

# Create your views here.

def home(request):
  template = 'products/home.html'
  ctx = locals()
  return render(request, template, ctx)


def all(request):
  products = Product.objects.all()
  ctx = {'products' : products}
  template = 'products/all.html'
  return render(request, template, ctx)
