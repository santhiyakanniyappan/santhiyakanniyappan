from django.db import models

class TodoItem(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('WORKING', 'Working'),
        ('PENDING REVIEW', 'Pending Review'),
        ('COMPLETED', 'Completed'),
        ('OVERDUE', 'Overdue'),
        ('CANCELLED', 'Cancelled'),
    ]

    timestamp = models.DateTimeField(auto_now_add=True)  # Auto-set timestamp
    title = models.CharField(max_length=100)  # Mandatory, max 100 characters
    description = models.TextField(max_length=1000)  # Mandatory, max 1000 characters
    due_date = models.DateField(null=True, blank=True)  # Optional
    tags = models.ManyToManyField('Tag', blank=True)  # Optional
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='OPEN')  # Mandatory

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
