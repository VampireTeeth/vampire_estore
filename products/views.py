from django.shortcuts import render

# Create your views here.

def home(request):
  template = 'products/home.html'
  ctx = locals()
  return render(request, template, ctx)
