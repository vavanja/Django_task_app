from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from .models import SpendStatistic
from .serializers import SpendStatisticSerializer


class SpendStatisticsView(APIView):
    def get(self, request):
        spend_data = SpendStatistic.objects.all().annotate(
            total_spend=Sum('spend'),
            total_impressions=Sum('impressions'),
            total_clicks=Sum('clicks'),
            total_conversion=Sum('conversion'),
            total_revenue=Sum('revenuestatistic__revenue')
        ).order_by('date', 'name')

        serializer = SpendStatisticSerializer(spend_data, many=True)
        return Response(serializer.data)
