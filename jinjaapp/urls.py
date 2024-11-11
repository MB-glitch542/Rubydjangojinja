from django.urls import path
from jinjaapp import views

urlpatterns=[
    path('',views.home,name='my_home'),

    path('about/',views.about,name='my_about'),

    path('contact/',views.contact,name='my_contacts'),

    path('services/',views.services,name='my_services'),



]