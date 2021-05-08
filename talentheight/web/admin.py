from django.contrib import admin
from .models import *
from django.contrib.admin import SimpleListFilter
from django.db import models

admin.site.site_header = "Talent Height Admin"
admin.site.site_title = "Talent Height Admin Portal"
admin.site.index_title = "Welcome to Talent Height Admin Panel"

# Admin Styling
class UserProfileAdmin(admin.ModelAdmin):
    search_fields = ('phone',)
    list_filter = ['creator','active']
    list_display= ('name', 'email','username','phone','total_viewcount','total_viewtime','aadhar','pan','active')


# Register your models here.
admin.site.register(Playlist)
admin.site.register(UserProfile)
admin.site.register(Bank)
admin.site.register(ChannelCategory)
admin.site.register(Channel)
admin.site.register(Monetization)
admin.site.register(Post)
admin.site.register(Award)
admin.site.register(Status)
admin.site.register(Setting)