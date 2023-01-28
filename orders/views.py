from django.views.generic.base import TemplateView


class OrderCreateView(TemplateView):
    template_name = 'orders/order-create.html'


class OrdersView(TemplateView):
    template_name = 'orders/orders.html'


class OrderView(TemplateView):
    template_name = 'orders/order.html'


class SuccessView(TemplateView):
    template_name = 'orders/success.html'
