from django.db import models
from django.contrib.auth.models import User
import random
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.core import validators
from django.urls import reverse
from django import forms
from django.utils import timezone
from datetime import datetime
from django.utils.html import mark_safe
from django.utils.html import format_html
from s3direct.fields import S3DirectField

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(blank=True)
    photo = models.ImageField(upload_to="profile pic")
    gender = models.CharField(max_length=20)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    address = models.TextField()
    phone = models.CharField(max_length=13)
    aadhar = models.CharField(max_length=20)
    pannumber = models.CharField(max_length=20)
    total_viewcount = models.IntegerField(default=0)
    total_viewtime = models.IntegerField(default=0)
    creator = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
          return "Message from " + self.user.username
    
    def username(self):
        try:
            school_id = self.user.pk
            info = (self.user._meta.app_label, self.user._meta.model_name)
            url = reverse('admin:{}_{}_change'.format(*info), args=(school_id,))
            return format_html('<a href="{url}">{text}</a>'.format(url=url,text=self.user.username))
        except Exception as e:
            return "Not Available"
    
    def name(self):
        return self.user.get_full_name()

    def email(self):
        return self.user.email

class Bank(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    ifsc = models.CharField(max_length=13)
    accountname = models.CharField(max_length=14, blank=True)
    accountnumber= models.CharField(max_length=14)
    earning = models.IntegerField(default=0)
    balance = models.IntegerField(default=0)
    withdrawing = models.IntegerField(default=0)
    timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

class ChannelCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="category")
    active = models.BooleanField(default=True)

    def __str__(self):
          return self.name


class Channel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(ChannelCategory, on_delete=models.CASCADE)
    subscriber_count = models.IntegerField(default=0)
    total_viewcount = models.IntegerField(default=0)
    total_viewtime = models.IntegerField(default=0)
    description = models.TextField()
    monetized = models.BooleanField(default=False)
    strikes = models.IntegerField(default=0)
    theme = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
          return self.name

class Status(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="status/")
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
          return self.id + ") " + self.user.username


class Post(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    thumbnail = models.ImageField( upload_to="thumbnail", blank=True)
    video = S3DirectField(dest='primary_destination', blank=True)
    posted = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    posted = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
          return self.title

class Playlist(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    videos = models.ManyToManyField(Post)

    def __str__(self):
          return self.name
          
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name= models.CharField(max_length=255)
    phone= models.CharField(max_length=13)
    email= models.CharField(max_length=100)
    content= models.TextField()
    timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
          return "Message from " + self.name + ' - ' + self.email


class Award(models.Model):
    name = models.ForeignKey(Channel, on_delete=models.CASCADE)
    min_subscriber_count= models.IntegerField(default=10)
    min_watch_time = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    image = models.ImageField(upload_to="awards/")
    message = models.TextField()
    posted = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
          return self.id+ ") " + self.title



class Setting(models.Model):
    viewrs_pay = models.BooleanField(default=True)
    creators_pay = models.BooleanField(default=True)
    homepage_status = models.BooleanField(default=True)
    category_filter = models.BooleanField(default=True)
    def __str__(self):
          return self.id+ ") " + self.title

class Monetization(models.Model):
    subscribers = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    videos = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    strikes = models.IntegerField(default=0)
    watchtime = models.IntegerField(default=0)

    def __str__(self):
          return self.id+ ") " + self.title
