from django.conf.urls import url, include
from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^first_exp/', views.experience, name='first_exp')
]