from django.contrib import admin
from .models import Ad, AdImage

class AdImageInline(admin.TabularInline):
    model = AdImage
    extra = 1

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'category', 'price', 'is_urgent', 'author', 'created_at')
    list_filter = ('city', 'category', 'is_urgent')
    search_fields = ('title', 'description', 'city')
    inlines = [AdImageInline]
