from django.db import models
from django_resized import ResizedImageField

# Create your models here.


class Pot(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True)
    price = models.FloatField(blank=False, default=0.0)
    height = models.IntegerField(blank=True, default=0)
    width = models.IntegerField(blank=True, default=0)
    photo = ResizedImageField(
        size=[500, 300], upload_to="products/", force_format="PNG")
    created_at = models.DateTimeField(
        verbose_name='creation date', auto_now_add=True)
    created_at = models.DateTimeField(
        verbose_name='last edited', auto_now=True)

    def __str__(self):
        return self.name
