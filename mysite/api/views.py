from django.shortcuts import render
from .serializers import TaskSerializer
from .serializers import ActivitySerializer
from .serializers import UserSerializer,UserUpdateSerializer
from .models import Activity, Task, UserProflie
from rest_framework import generics


class TaskList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    # return Response(queryset.data)

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class ActivityList(generics.ListAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class ActivityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = ActivitySerializer

class UserprofileList(generics.ListAPIView):
    queryset = UserProflie.objects.all()
    serializer_class = UserSerializer

class UserprofileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProflie.objects.all()
    serializer_class = UserSerializer
    def get_serializer_class(self):
        if self.request.method in  ['POST', 'PUT', 'PATCH']:
            return UserUpdateSerializer
        return UserSerializer
