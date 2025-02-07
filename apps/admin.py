from django.contrib import admin
from .models import Feedbacks


class FeedbacksAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'email', 'rating', 'created_at']
    
admin.site.register(Feedbacks,FeedbacksAdmin)

