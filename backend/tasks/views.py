from django.db import connections
from django.http import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .serializers import UserSerializer, TaskSerializer
from .models import User, Task
from rest_framework.decorators import api_view




# Create your views here.

# class UserView(viewsets.ModelViewSet):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()

# class TaskView(viewsets.ModelViewSet):
#     serializer_class = TaskSerializer
#     queryset = Task.objects.all()


@api_view(['GET'])
def userList(request):
    users = User.objects.order_by('first_name')
    serializer = UserSerializer(users,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def userCreate(request):
    serialize = UserSerializer(data=request.data)

    print(serialize)
    if serialize.is_valid():
        serialize.save()

    
    return Response(serialize.data)

@api_view(['PUT'])
def userUpdate(request,userId):
    print(userId)
    user = User.objects.get(id=userId)
    
    serializer = UserSerializer(instance=user,data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def userTasks(request,userId):
    tasks = Task.objects.filter(assign_to_id=userId)
    serializer = TaskSerializer(tasks,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)

    print(serializer)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def taskUpdate(request,taskId):
    task = Task.objects.get(id=taskId)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def taskDelete(request,taskId):
    task = Task.objects.get(id=taskId)
    task.delete()

    return Response('Deleted')
