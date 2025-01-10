from django.db import models

class User(models.Model):
    USER_TYPE_CHOICES = [
        ('candidate', 'Candidate'),
        ('interviewer', 'Interviewer'),
    ]
    name = models.CharField(max_length=255)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

class Availability(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='availabilities')
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.DateField()
