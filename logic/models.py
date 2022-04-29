from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


class Article(models.Model):
    date_created = models.DateTimeField("дата создания", auto_now_add=True)
    preview_link = models.URLField("Ссылка на превью")
    initial_link = models.URLField("Основная ссылка")
    name = models.CharField("Название", max_length=300)

    class Meta:
        ordering = ['-date_created']     


class Profile(models.Model):
    user = models.OneToOneField(Article, on_delete=models.CASCADE)
    reading_list = models.ManyToManyField(Article, related_name="in_reading_list")
    archive = models.ManyToManyField(Article, related_name="in_archive")
    deleted = models.ManyToManyField(Article, related_name="in_deleted")

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()