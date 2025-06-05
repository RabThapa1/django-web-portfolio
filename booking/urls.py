from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name = 'homepage.html'),
    path('search', views.search, name='search.html'),
    path('manage', views.managebooking, name='manage.html'),
    path('invoice', views.invoice, name='invoice.html'),
    path('contactus', views.contactus, name='contactus.html')

]
