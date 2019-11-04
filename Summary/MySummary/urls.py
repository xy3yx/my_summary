from django.conf.urls import url, include
from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^first_exp/', views.experience, name='first_exp'),
        url(r'^second_exp/', views.second_experience, name='second_exp'),
        url(r'^third_exp/', views.third_experience, name='third_exp'),
        url(r'^education/', views.education, name='education'),
        url(r'^skills/', views.skills, name='skills')
]