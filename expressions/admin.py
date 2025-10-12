from django.contrib import admin
from .models import Expression

@admin.register(Expression)
class ExpressionAdmin(admin.ModelAdmin):
    list_display = ('text', 'owner', 'region', 'register', 'created')
    list_filter = ('register',)
    search_fields = ('text', 'meaning', 'region', 'usage_notes')
