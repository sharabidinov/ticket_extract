from django.urls import path
from .views import TicketList, TicketCreate, TicketUpdate, delete_ticket

urlpatterns = [
    path('tickets/', TicketList.as_view(), name='list_tickets'),
    path('create/', TicketCreate.as_view(), name='create_ticket'),
    path('update/<int:pk>/', TicketUpdate.as_view(), name='update_ticket'),
    path('delete-flight/<int:pk>/', delete_ticket, name='delete_ticket'),
]
