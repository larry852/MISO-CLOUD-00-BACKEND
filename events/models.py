import uuid
from django.db import models
from django.contrib.auth import get_user_model
from core.utils.file import get_path_class
from .choices import CATEGORIES, TYPES

User = get_user_model()


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_category = models.CharField(max_length=10, choices=CATEGORIES)
    event_name = models.CharField(max_length=100)
    event_place = models.CharField(max_length=100)
    event_address = models.CharField(max_length=100)
    event_initial_date = models.DateTimeField()
    event_final_date = models.DateTimeField()
    event_type = models.CharField(max_length=10, choices=TYPES)
    datetime = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(
        upload_to=get_path_class, default='default-event-thumb.jpg')

    class Meta:
        ordering = ['-datetime']
