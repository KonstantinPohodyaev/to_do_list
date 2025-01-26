from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import TaskViewSet


TASK_VIEW_SET_PREFIX = 'tasks'
TASK_VIEW_SET_BASENAME = ''


app_name = 'api'


router = DefaultRouter()
router.register(
    TASK_VIEW_SET_PREFIX,
    TaskViewSet,
    basename=TASK_VIEW_SET_BASENAME
)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken'))
]
