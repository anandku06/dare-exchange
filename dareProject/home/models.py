from django.db import models


# Create your models here.
class DareExchange(models.Model):
    CATEGORY_CHOICES = [
        ("fun", "Fun"),
        ("adventure", "Adventure"),
        ("social", "Social"),
        ("skill", "Skill"),
    ]
    DIFFICULTY_CHOICES = [
        ("easy", "Easy"),
        ("medium", "Medium"),
        ("hard", "Hard"),
    ]
    title = models.CharField(max_length=30)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
