from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from .models import Order, OrderItem

##-------------- Order Views --------------------------------------
class DetailOrder(DetailView):
    model = Order
    template_name='orders/detail_order.html'

class ListOrder(ListView):
    model = Order
    context_object_name = 'orders'
    template_name='orders/list_orders.html'

class CreateOrder(CreateView):
    model = Order
    template_name = 'orders/create_order.html'

class UpdateOrder(UpdateView):
    model = Order
    template_name = 'orders/update_order.html'

class DeleteOrder(DeleteView):
    model = Order
    template_name = 'orders/delete_order.html'


##-------------- OrderItem Views --------------------------------------
class DetailOrderItem(DetailView):
    model = OrderItem
    template_name='orders/detail_orderitem.html'

class ListOrderItem(ListView):
    model = OrderItem
    context_object_name = 'orderitems'
    template_name='orders/list_orderitems.html'

class CreateOrderItem(CreateView):
    model = OrderItem
    template_name = 'orders/create_orderitem.html'

class UpdateOrderItem(UpdateView):
    model = OrderItem
    template_name = 'orders/update_orderitem.html'

class DeleteOrderItem(DeleteView):
    model = OrderItem
    template_name = 'orders/delete_orderitem.html'
