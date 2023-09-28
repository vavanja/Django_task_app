from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from .models import RevenueStatistic
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
