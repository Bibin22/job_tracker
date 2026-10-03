from rest_framework import routers
from django.urls import path
from . import views


urlpatterns = [
    path('company-management/', views.CompanyManagementView.as_view(), name='company-management'),
    path('company-management/<int:pk>/', views.CompanyManagementView.as_view(), name='company-management'),

]