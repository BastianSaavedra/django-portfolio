from django.urls import path
from . import views
from django.views.static import serve
from django.conf.urls import url
from django.conf import settings

urlpatterns = [
    path('', views.index, name="index"),
    path('mail/', views.contact, name="contact"),

]
