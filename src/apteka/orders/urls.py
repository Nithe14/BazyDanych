from django.urls import path, include

from . import views

# Order Urls
urlpatterns = [
    path('order/', views.ListOrder, name='list-orders'),
    path('order/<int:pk>/', views.DetailOrder.as_view(), name='detail-order'),
    path('order/create/', views.CreateOrder.as_view(), name='create-order'),
    path('order/<int:pk>/update/', views.UpdateOrder.as_view(), name='update-order'),
    path('order/<int:pk>/delete/', views.DeleteOrder.as_view(), name='delete-order'),
]

# OrderItem Urls
urlpatterns += [
    path('orderitem/', views.ListOrderItem.as_view(), name='list-orderitem'),
    path('orderitem/<int:pk>/', views.DetailOrderItem.as_view(), name='detail-orderitem'),
    path('orderitem/create/', views.CreateOrderItem.as_view(), name='create-orderitem'),
    path('orderitem/<int:pk>/update/', views.UpdateOrderItem.as_view(), name='update-orderitem'),
    path('orderitem/<int:pk>/delete/', views.DeleteOrderItem.as_view(), name='delete-orderitem'),
]