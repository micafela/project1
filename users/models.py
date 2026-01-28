from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):

    # custom user field
    POS_LECTURER1 = 'lecture_1'
    POS_LECTURER2 = 'lecture2'
    POS_DOCTOR = 'doctor'
    POS_ASSOC_PROF = 'assocaiate professor'
    POS_PROFESSOR = 'professsor'

    POSTION_CHOICES = (
        (POS_LECTURER1, 'Lecture 1'),
        (POS_LECTURER2, 'Lecture 2'),
        (POS_DOCTOR, 'Doctor'),
        (POS_ASSOC_PROF, 'Assocaiate Professor'),
        (POS_PROFESSOR, 'Professsor')
    )
    position = models.CharField(
        choices=POSTION_CHOICES, max_length=30, blank=False)
    keywords = models.TextField(max_length=100)
