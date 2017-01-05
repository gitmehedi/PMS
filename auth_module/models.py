from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import UserManager
# from gdata.data import SENDER


class Profile(models.Model):
    """
    UserInfo stores additional information
    which is not directly related to authentication
    system.
    """
    
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    #     @receiver(post_save,sender=User)
    #     def create_user_userinfo(sender,instance,created,**kwargs):
    #         if created:
    #             Userinfo.objects.create(user=instance)
    #
    #
    #     @receiver(post_save,sender=User)
    #     def save_user_userinfo(sender,instance,**kwargs):
    #         instance.userinfo.save()

class NavigationMenu(models.Model):
    """
    Create a menu lists which generates a custom munu
    """
    name = models.CharField(max_length=100, blank=False)
    slug= models.CharField(max_length=100, blank=True, null=True)
    level = models.IntegerField(default=0)
    parent = models.ForeignKey("self", blank=True, null=True)
    status = models.BooleanField(default=False)

    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Navigation Menu"


    def __str__(self):
            return self.name

    def save(self, *args, **kwargs):
        if self.parent:
            self.level = 1
        else:
            self.level = 0
        super(NavigationMenu, self).save(*args, **kwargs)




    



