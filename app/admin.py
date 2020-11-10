from django.contrib import admin
from .models import *


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'check')


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'dt')


admin.site.register(Post, PostAdmin)
admin.site.register(Feedback, FeedbackAdmin)
