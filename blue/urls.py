from django.urls import path
from . import views 


app_name='blue'

urlpatterns = [
    path('', views.app,name='app'),
    path('contact', views.contact,name='contact'),
    path('list', views.list,name='list'),
     path('product/<int:product_id>/details', views.details, name='product_detail'),
    path('success', views.success,name='success'),

    path('category/<int:category_id>/', views.category, name='category'),
]
