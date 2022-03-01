from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
#for making a new profile for a new user automatically
@receiver(post_save, sender = User)
def create_profile(sender, instance,created, **kwargs):
    if created:
        Profile.objects.create(user = instance)
    

#for saving that profile

@receiver(post_save, sender = User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
# in order to work WE HAVE TO import signals in our apps file