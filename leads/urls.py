from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_view,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
    path('employee_dashboard',views.employee_dashboard,name='employee_dashboard'),
    path('add_lead/',views.add_lead,name='add_lead'),
    path('lead_list/',views.lead_list,name='lead_list'),
    path('edit_lead/<int:pk>',views.edit_lead,name='edit_lead'),
    path('delete_lead/<int:pk>',views.delete_lead,name='delete_lead'),
    path('lead_history/<int:pk>',views.lead_history,name='lead_history'),
]