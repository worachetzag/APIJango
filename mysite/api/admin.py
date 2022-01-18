from django.contrib import admin
from .models import Task, UserProflie, Activity


# Register our model
admin.site.register(Task)
admin.site.register(Activity)
admin.site.register(UserProflie)
