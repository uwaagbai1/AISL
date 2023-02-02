from django.urls import path

from main.views import *

urlpatterns = [

    path('', index, name="index"),
    path('who-we-are/', about, name="about"),
    path('admissions/', admissions, name="admissions"),
    path('school-academics/', academics, name="academics"),
    path('gallery/', gallery, name="gallery"),
    path('our-news/', NewsView.as_view(), name="news"),
    path('contact-us/', contact, name="contact"),
    path('news/<slug>/<pk>/', news_single, name="single")

]