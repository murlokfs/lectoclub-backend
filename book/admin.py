from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('isbn', 'user', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('isbn', 'user__username', 'comment')
    ordering = ('-created_at',)

    fieldsets = (
        (None, {'fields': ('isbn', 'user', 'rating')}),
        ('Comment', {'fields': ('comment',)}),
        ('Dates', {'fields': ('created_at',)}),
    )
    
    readonly_fields = ('created_at',)


# Register your models here.
