from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'products.views.home', name='home'),
    url(r'all/$', 'products.views.all', name='all'),
]

