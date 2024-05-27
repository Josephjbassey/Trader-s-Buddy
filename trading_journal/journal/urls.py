from django.urls import path
from . import views

urlpatterns = [
    path('risk-calculator/', views.risk_calculator, name='risk_calculator'),
]