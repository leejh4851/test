from django.contrib import admin
from django.urls import path,include
from . import views

app_name ='ordersystem'
urlpatterns = [
    path('postal/', views.postal,name='postal'),
    path('postresult/', views.postresult,name='postresult'),
    path('orderwrite/', views.orderwrite,name='orderwrite'),
    path('orderlist/', views.orderlist,name='orderlist'),
    path('view/<int:id>/',views.orderdetail,name='orederdetail'),
    path('goodslist/',views.goodslist,name='goodslist'),
]

