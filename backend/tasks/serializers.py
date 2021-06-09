from django.db.models import fields
from rest_framework import serializers
from rest_framework.fields import URLField
from .models import User, Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title')
        
        