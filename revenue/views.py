from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
import random
from datetime import datetime, timedelta
from .models import RevenueStatistic
from spend.models import SpendStatistic
from .serializers import RevenueStatisticSerializer


class RevenueStatisticsView(APIView):

    def get(self, request):
        revenue_data = RevenueStatistic.objects.all().annotate(
            total_revenue=Sum('revenue'),
            total_spend=Sum('spend__spend'),
            total_impressions=Sum('spend__impressions'),
            total_clicks=Sum('spend__clicks'),
            total_conversion=Sum('spend__conversion')
        ).order_by('date', 'name')

        return Response(RevenueStatisticSerializer(revenue_data, many=True).data)


def create_db_data(request):
    SpendStatistic.objects.all().delete()
    RevenueStatistic.objects.all().delete()

    names = ["Shadow Ector", "Rhiana West", "John Silver", "Mike Lebigovich", "Stas Grand"]
    for name in names:
        SpendStatistic.objects.create(name=name,
                                      date=datetime.now() - timedelta(days=random.randint(1, 365)),
                                      spend=random.randint(10, 50),
                                      impressions=random.randint(0, 10),
                                      clicks=random.randint(1, 100),
                                      conversion=random.randint(1, 5))

    for i, spend_record in enumerate(SpendStatistic.objects.all()):
        RevenueStatistic.objects.create(
            name=spend_record.name,
            date=datetime.now() - timedelta(days=random.randint(1, 365)),
            revenue=random.randint(1000, 2000),
            spend=spend_record
        )
