from django.urls import path
from . import views

urlpatterns=[
    path('username/', views.username_page, name='username_page'),
    path('password/', views.password_page, name='password_page'),
    path('signup/', views.signup_page, name='signup_page'),
    path('index/', views.index, name='index'),
    path('cart/', views.cart,name='cart'),
    path('contact/', views.contact, name='contact'),
    path('details/<int:car_id>', views.car_detail, name = 'car_detail'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart')
]
