from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'products.views.home', name='home'),
]
