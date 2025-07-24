from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):

    STATUS_CHOISES = [
        ("todo", "To Do"),
        ("in_prog", "In progression"),
        ("done", "Done")
    ]

    PRIORITY = [
        ("low",'low'),
        ("med", "Medium"),
        ('high', 'High'),
        ('2high', 'PIZDA HIGH')
    ]
    title = models.CharField(max_length=200)
    desc = models.TextField()
    status = models.CharField(choices=STATUS_CHOISES, default="todo")
    prior = models.CharField(choices=PRIORITY, default='low')
    due = models.DateField(null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')