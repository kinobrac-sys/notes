from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):

    STATUS_CHOISES = [
        ("To Do", "To Do"),
        ("In Progression", "In progression"),
        ("Done", "Done")
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

class Comment(models.Model):
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
