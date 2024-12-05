from django.contrib import admin
from .models import TodoItem, Tag

@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'due_date', 'timestamp')
    list_filter = ('status', 'due_date', 'timestamp')
    search_fields = ('title', 'description')
    readonly_fields = ('timestamp',)
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'status')
        }),
        ('Optional Info', {
            'fields': ('due_date', 'tags')
        }),
        ('System Info', {
            'fields': ('timestamp',),
            'classes': ('collapse',),
        }),
    )

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
