from django.urls import path ,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/',views.create,name='create'),
    path('portfolioPage/',views.portfolioPage,name='portfolioPage'),
    path('detail/<int:blog_id>', views.detail, name='detail'),
    path('postcreate/',views.postcreate,name='postcreate'),   
    path('update/<int:blog_id>/', views.update, name='update'),
    path('delete/<int:blog_id>/', views.delete, name='delete'),
    path('search/',views.search,name='search'),

]