from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, status, exceptions
from rest_framework.decorators import action
from rest_framework.response import Response

from tasks.models import Task, CustomUser
from .serializers import (
    TaskSerializerReadSerializer, TaskSerializerCreateSerializer
)
from .permissions import TaskPermission
from .paginators import TaskPageNumberLimitPagination


TASK_DONE_STATUS_ERROR = 'Эта задача уже выполнена!'


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.filter(done_status=False)
    permission_classes = [TaskPermission]
    lookup_field = 'slug'
    pagination_class = TaskPageNumberLimitPagination

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return TaskSerializerReadSerializer
        return TaskSerializerCreateSerializer

    @action(
        detail=False,
        url_path='done'
    )
    def get_not_done_tasks(self, request):
        return Task.objects.filter(done_status=True)

    @action(
        methods=['post'],
        detail=True,
        url_path='complete'
    )
    def add_complete_status(self, request, slug):
        task = get_object_or_404(
            Task,
            slug=slug
        )
        if task.done_status:
            raise exceptions.ValidationError(
                {'error': TASK_DONE_STATUS_ERROR}
            )
        task.done_status = True
        task.save()
        serialized_data = TaskSerializerReadSerializer(task).data
        return Response(
            serialized_data,
            status=status.HTTP_200_OK
        )
