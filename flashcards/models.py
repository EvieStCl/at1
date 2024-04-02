from django.db import models

class Flashcard(models.Model):
    front_side = models.CharField(max_length=100)
    back_side = models.TextField()