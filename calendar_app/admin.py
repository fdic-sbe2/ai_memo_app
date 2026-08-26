from django.contrib import admin
from .models import Event, Task


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
	list_display = ("title", "user", "start_at", "end_at", "is_all_day")
	list_filter = ("is_all_day", "start_at", "end_at", "user")
	search_fields = ("title", "description", "user__username")
	ordering = ("-start_at",)
	date_hierarchy = "start_at"


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
	list_display = ("title", "user", "due_at", "is_completed", "parent_event", "parent_task")
	list_filter = ("is_completed", "due_at", "user")
	search_fields = ("title", "user__username")
	ordering = ("due_at",)
	date_hierarchy = "due_at"