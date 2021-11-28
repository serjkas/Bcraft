

from .views import (
    ActivityCollectionModelViewSet, delete_statistics
)


from django.urls import path, include

from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register(r'activity', ActivityCollectionModelViewSet, basename='activity')

urlpatterns = [
    path('delete_statistics', delete_statistics),
]

urlpatterns += router.urls
