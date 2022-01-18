from pyexpat import model
from django.db import models
from django.contrib.auth.models import User, Group

class Task(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField()

    class Meta:
        ordering = ['-date_created']
        db_table = 'task'
    
    def __str__(self):
        return self.title

class Activity(models.Model):
    health = models.IntegerField()
    heart_rate = models.IntegerField()
    walk_count = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']
        db_table = 'activity'

    def __str__(self):
        return str(self.health) + ',' + str(self.heart_rate)+ ',' + str(self.walk_count)

class UserProflie(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='user_profile')
    activity = models.ForeignKey(Activity,
                                null=True,
                                related_name='user_activity',
                                blank=True,
                                on_delete=models.SET_NULL)
    friends = models.ManyToManyField(User, related_name='friend_user', blank=True)
    
    def __str__(self):
        return self.user.username