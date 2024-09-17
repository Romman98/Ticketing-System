from django.urls import path, include
from .views import TicketView, add_sample, create_ticket,submit_samples, viewTickets, ticket_detail, ticket_delete, signup
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('', TicketView.as_view(), name='ticket-home'),
    path('create-ticket/', create_ticket, name='create_ticket'),
    path('add-sample/', add_sample, name='add_sample'),
    path('submit-samples/', submit_samples, name='submit_samples'),
    path('', viewTickets, name='view_tickets'),
    path('ticket/<int:ticket_id>/', ticket_detail, name='ticket_detail'),
    path('ticket_delete/<int:ticket_id>/', ticket_delete, name='ticket_delete'),
    path('login/', auth_views.LoginView.as_view(template_name='userauth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/',signup, name='signup'),
]
