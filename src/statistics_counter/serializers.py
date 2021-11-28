from rest_framework import serializers
from .models import ActivityCollection


class ActivityCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityCollection
        fields = ('date_at', 'views', 'clicks', 'cost', 'cpc', 'cpm')