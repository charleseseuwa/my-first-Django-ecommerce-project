from django.urls import path
from .views import product_page, about, contact


urlpatterns = [
    path("", product_page, name="product-page"),
    path("about/", about, name='about'),
    path('contact/', contact, name='contact')
]