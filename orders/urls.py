from django.urls import path

from orders import views

app_name = 'orders'

urlpatterns = [
    path('order-create', views.OrderCreateView.as_view(), name='order_create'),
    path('order', views.OrderView.as_view(), name='order'),
    path('orders', views.OrdersView.as_view(), name='orders'),
    path('success', views.SuccessView.as_view(), name='success'),

]