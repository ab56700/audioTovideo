
from django.urls import path
from .views import home, dashboard_view, result_view

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('result/<int:audio_id>/', result_view, name='result'),
]
