from django.db import models

# Create your models here.
# post class. would contain title, slug,description,date created,date edited,author,image


class Post(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    slug = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(
        verbose_name=('creation date'), auto_now_add=True)
    created_at = models.DateTimeField(
        verbose_name=('last edited'), auto_now=True)
    author = models.ForeignKey(
        "users.CustomUser", on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='post_images')


def __str__(self):
    return self.name
