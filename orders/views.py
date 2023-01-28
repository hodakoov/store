from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from orders.forms import OrderForm
from common.view import TitleMixin


class OrderCreateView(TitleMixin, CreateView):
    template_name = 'orders/order-create.html'
    form_class = OrderForm
    success_url = reverse_lazy('orders:order_create')
    title = 'Магазин - Оформление заказа'

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super(OrderCreateView, self).form_valid(form)


class OrdersView(TemplateView):
    template_name = 'orders/orders.html'


class OrderView(TemplateView):
    template_name = 'orders/order.html'


class SuccessView(TemplateView):
    template_name = 'orders/success.html'
