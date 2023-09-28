from django.urls import path

from revenue.views import RevenueStatisticsView, create_db_data

urlpatterns = [
    path('', RevenueStatisticsView.as_view()),
    path('create/', create_db_data)
]