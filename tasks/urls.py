from tkinter.font import names

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_task/',views.add_task,name='add_task'),
    path('history/', views.history, name='history'),
path('register/', views.register, name='register'),
    path('edit/<int:id>/', views.edit_task, name='edit_task'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
path('complete/<int:id>/', views.complete_task, name='complete_task'),
path('profile/', views.profile, name='profile'),
]