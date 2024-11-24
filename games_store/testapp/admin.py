from django.contrib import admin
from .models import Topic, News

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = "id", "name", "description"
    search_fields = "name",


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = "topic", "title", "created_at", "is_published",
    list_filter = "topic", "is_published",
    search_fields = "title", "content",
    list_per_page = 10