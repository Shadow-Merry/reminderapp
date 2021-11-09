from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class reminder(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    status = models.BooleanField(default = False)
    created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField("Due date")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('reminder:detail', kwargs={'pk':self.pk})