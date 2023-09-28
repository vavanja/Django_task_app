from django.urls import path
from .views import SpendStatisticsView

urlpatterns = [
    path('', SpendStatisticsView.as_view())
]