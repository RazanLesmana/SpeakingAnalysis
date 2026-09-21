from django.db import models
import uuid

class Topic(models.Model):
    CATEGORY_CHOICES = [
        ('everyday', 'Everyday'),
        ('deep', 'Deep'),
        ('technical', 'Technical'),
        ('freestyle', 'Freestyle')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    category = models.TextField(max_length=100, blank=True, choices=CATEGORY_CHOICES)
    description = models.CharField(blank=True)

    def __str__(self):
        return self.title


