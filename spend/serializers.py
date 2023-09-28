from rest_framework import serializers


class SpendStatisticSerializer(serializers.Serializer):
    name = serializers.CharField()
    date = serializers.DateField()
    total_spend = serializers.DecimalField(max_digits=10, decimal_places=2)
    total_impressions = serializers.IntegerField()
    total_clicks = serializers.IntegerField()
    total_conversion = serializers.IntegerField()
    total_revenue = serializers.DecimalField(max_digits=9, decimal_places=2)
