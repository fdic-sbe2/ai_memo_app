from datetime import time

from django.core.exceptions import ValidationError
from django.db import models
from django.conf import settings
import uuid


class Event(models.Model):
    event_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    is_all_day = models.BooleanField(default=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        db_column="user_id",
        related_name="events",
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=models.Q(end_at__gt=models.F("start_at")),
                name="event_end_after_start",
            ),
        ]

    def clean(self):
        super().clean()
        if self.start_at and self.end_at and self.end_at <= self.start_at:
            raise ValidationError("end_at must be later than start_at.")

        if self.is_all_day and self.start_at and self.end_at:
            if self.start_at.time() != time(0, 0) or self.end_at.time() != time(0, 0):
                raise ValidationError(
                    "All-day events must use 00:00 boundaries for start_at and end_at."
                )

class Task(models.Model):
    task_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parent_event = models.ForeignKey(
        "Event",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        db_column="parent_event_id",
        related_name="tasks",
    )
    parent_task = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        db_column="parent_task_id",
        related_name="children",
    )
    due_at = models.DateTimeField()
    title = models.CharField(max_length=50)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        db_column="user_id",
        related_name="tasks",
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=models.Q(parent_event__isnull=True) | models.Q(parent_task__isnull=True),
                name="task_not_both_parent_event_and_parent_task",
            ),
        ]

