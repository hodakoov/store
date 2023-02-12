from django.urls import path

from orders import views

app_name = 'orders'

urlpatterns = [
    path('order-create', views.OrderCreateView.as_view(), name='order_create'),
    path('order', views.OrderView.as_view(), name='order'),
    path('', views.OrderListView.as_view(), name='orders_list'),
    path('success', views.SuccessTemplateView.as_view(), name='success'),
    path('canceled', views.CanceledTemplateView.as_view(), name='canceled'),

]
