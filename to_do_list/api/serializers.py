from datetime import datetime

from rest_framework import serializers
from django.utils import timezone

from tasks.models import Task, CustomUser


UNKNOWN_FIELDS_IN_REQUEST = 'Неизвестные поля: {unknown_fields}'


class CustomUserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']
        read_only_fields = fields


class CustomUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'bio']


class CustomUserReadSerializer(CustomUserCreateSerializer):
    pass


class TaskSerializerReadSerializer(serializers.ModelSerializer):
    deadline_status = serializers.SerializerMethodField()
    author = CustomUserShortSerializer(read_only=True)
    time_to_deadline = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = [
            'id', 'name', 'text', 'slug', 'done_status', 'start_date',
            'end_date', 'author', 'deadline_status'
        ]
        read_only_fields = fields

    def get_deadline_status(self, task):
        return task.end_date <= timezone.make_aware(datetime.now())

    def get_time_to_deadline(self, task):
        return task.end_date - datetime.now()

class TaskSerializerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['name', 'text', 'slug', 'end_date']

    def create(self, validated_data):
        return Task.objects.create(
            author=self.context['request'].user, **validated_data
        )

    def update(self, instance, validated_data):
        validated_data.pop('author', None)
        instance.name = validated_data.pop('name', instance.name)
        instance.text = validated_data.pop('text', instance.text)
        instance.end_date = validated_data.pop('end_date', instance.end_date)
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        return TaskSerializerReadSerializer(instance).data

    def to_internal_value(self, data):
        received_fields = set(data.keys())
        defined_fields = set(self.fields.keys())
        unknown_fields = received_fields - defined_fields
        if unknown_fields:
            raise serializers.ValidationError(
                {
                    'error': UNKNOWN_FIELDS_IN_REQUEST.format(
                        unknown_fields=unknown_fields
                    )
                }
            )
        return super().to_internal_value(data)

