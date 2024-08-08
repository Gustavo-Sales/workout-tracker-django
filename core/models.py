from uuid import uuid4
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Workout(models.Model):
    TYPE_WORKOUT_CHOICES = (
        ("CA", "Cardio"),
        ("ST", "Strength Training"),
    )
    id = models.UUIDField(primary_key=True, unique=True, default=uuid4, editable=False)
    name = models.CharField(max_length=30, null=False, blank=False)
    type_workout = models.CharField(
        max_length=2, choices=TYPE_WORKOUT_CHOICES, null=False, blank=False
    )
    exercises = models.JSONField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("core:detail", kwargs={"id": self.id})

    def __str__(self):
        return self.name
