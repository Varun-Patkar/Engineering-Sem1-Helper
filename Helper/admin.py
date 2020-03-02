from django.contrib import admin
from .models import MCQ,PDF,Announcement,Feedback
# Register your models here.
admin.site.register(MCQ)
admin.site.register(PDF)
admin.site.register(Announcement)
admin.site.register(Feedback)