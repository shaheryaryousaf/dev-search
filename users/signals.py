from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from .models import Profile


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, name=instance.first_name,
                               email=instance.email, username=instance.username)


# def deleteUser(sender, instance, **kwargs):
#     user = instance.user
#     user.delete()


post_save.connect(create_profile, sender=User)
# post_delete.connect(deleteUser, sender=Profile)
