import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Question(models.Model):
    CATEGORY_CHOICES = [
        ('A', 'General'),
        ('B', 'Technical'),
        ('C', 'Personal'),
    ]

    DAYS_RECENT = 7  # Configura el número de días para was_published_recently

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    created_at = models.DateTimeField("date created", default=timezone.now, editable=False)
    updated_at = models.DateTimeField("date updated", default=timezone.now)
    comment = models.TextField(blank=True, null=True)  # Campo opcional de tipo texto
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='A')
    pollster = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=self.DAYS_RECENT) <= self.pub_date <= now
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    created_at = models.DateTimeField("date created", default=timezone.now, editable=False)
    updated_at = models.DateTimeField("date updated", default=timezone.now)

    def __str__(self):
        return self.choice_text
