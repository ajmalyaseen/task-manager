from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):

    STATUS_CHOICES = [
        ('To Do', 'To Do'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    
    PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    description = models.TextField(blank=True, null=True) 
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='To Do')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    due_date = models.DateField(null=True, blank=True)  
    created = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    def __str__(self):
        return self.title



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics', null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'