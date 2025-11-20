from django.contrib import admin
from . models import Profile,Lead,LeadHistory

# Register your models here.
admin.site.register(Profile)
admin.site.register(Lead)
admin.site.register(LeadHistory)