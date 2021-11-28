from .models import ActivityCollection
from .serializers import ActivityCollectionSerializer
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import datetime
from rest_framework.exceptions import ValidationError


def date_validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except:
        raise ValidationError(
            detail="Incorrect data format, should be YYYY-MM-DD")


class ActivityCollectionModelViewSet(ModelViewSet):
    """ Отдает список опросов по id пользователя """
    queryset = ActivityCollection.objects.all()
    serializer_class = ActivityCollectionSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['date_at', 'views', 'clicks', 'cost', 'cpc', 'cpm']
    filter_fields = ['date_at']
    http_method_names = ['get', 'post']

    def get_queryset(self):
        from_date = self.request.query_params.get('from')
        date_validate(from_date)
        to_date = self.request.query_params.get('to')
        date_validate(to_date)

        queryset = ActivityCollection.objects.filter(date_at__gte=from_date, date_at__lte=to_date).order_by(
            'date_at')

        return queryset

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_statistics(request):
    try:
        ActivityCollection.objects.all().delete()
        content = {'message': 'Statistics was deleted'}
        return Response(content, status=status.HTTP_200_OK,)
    except:
        content = {'message': 'Statistics was not deleted'}
        return Response(content, status=status.HTTP_409_CONFLICT,)
