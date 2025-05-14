from django.contrib import admin

from .models import Inflow


@admin.register(Inflow)
class InflowAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'quantity', 'created_at')
    search_fields = ('product',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)
