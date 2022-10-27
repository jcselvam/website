
from django.urls import path
from . import views

urlpatterns = [
    
    path('show',views.Get, name='Get'),
    path('post',views.Post, name='Post'),
    path('update/<int:id>', views.Update, name='Update'),
    path('delete/<int:id>', views.Delete, name='Delete')
]
