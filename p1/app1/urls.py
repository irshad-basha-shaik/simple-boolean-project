from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('edit',views.edit,name='edit'),
    path('editform',views.editform,name='editform'),
]
