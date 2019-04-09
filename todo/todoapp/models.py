from django.db import models
from datetime import datetime

class TodoList(models.Model):
    user = models.CharField(max_length=30, blank=True, null=True)
    task = models.CharField(max_length=100)
    Time = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    Accomplished = models.BooleanField(default = False)

    def __str__(self):
        return self.task
