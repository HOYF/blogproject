from django.contrib import admin
from .models import Letter

class LetterAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'send_time']

admin.site.register(Letter, LetterAdmin)

