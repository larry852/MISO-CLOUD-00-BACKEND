from django.db import models
from django.contrib.auth import get_user_model
import uuid
from core.utils.file import get_path_class
from .choices import CATEGORIES, TYPES

User = get_user_model()

class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.CharField(max_length=10, choices=CATEGORIES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    datetime = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=10, choices=TYPES)
    thumbnail = models.ImageField(upload_to=get_path_class, default='default-event-thumb.jpg')

    class Meta:
        ordering = ['datetime']