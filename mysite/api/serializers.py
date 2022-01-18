from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Task,Activity,UserProflie,User


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id',
                  'title', 
                  'description', 
                  'date_created', 
                  'complete')

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('id',
                 'health', 
                 'heart_rate',
                 'walk_count',
                 'date_created')

class FriendsSerializer(serializers.ModelSerializer):

  
    class Meta:
        model = UserProflie
        fields = ('id','username')

    

# class UserProflie(models.Model):
class UserSerializer(serializers.ModelSerializer):
    activity = ActivitySerializer()
    username = serializers.SerializerMethodField()
    friends = FriendsSerializer( many=True)
    class Meta:
        model = UserProflie
        fields = ('id',
                  'user', 
                  'username',
                  'friends',
                  'activity')

    def get_username(self, obj):
        return obj.user.username

class UserUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserProflie
        fields = ('id',
                  'user', 
                  'friends',
                  'activity')

   