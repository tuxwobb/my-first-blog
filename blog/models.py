from django.db import models
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
import os

#def get_image_path(instance, filename):
#    return os.path.join('photos', str(instance.id), filename)

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    PRIORITIES = [
        (1, 'Nejvyšší'),
        (2, 'Vysoká'),
        (3, 'Střední'),
        (4, 'Nízká'),
        (5, 'Nejnižší'),
    ]
    priority = models.IntegerField(
        choices=PRIORITIES,
        default=3,
    )

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    title = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    photo = models.ImageField(upload_to='.')
    PRIORITIES = [
        (1, 'Nejvyšší'),
        (2, 'Vysoká'),
        (3, 'Střední'),
        (4, 'Nízká'),
        (5, 'Nejnižší'),
    ]
    priority = models.IntegerField(
        choices=PRIORITIES,
        default=3,
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def unpublish(self):
        self.published_date = timezone.deactivate()
        self.save()

    def __str__(self):
        return self.title