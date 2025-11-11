from django.db import models

class Product(models.Model):
    COMPATIBILITY_CHOICES = [
        ('quest', 'Quest'),
        ('pico', 'Pico'),
        ('universal', 'Универсальные'),
    ]

    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='catalog/')
    available = models.BooleanField(default=True)
    compatibility = models.CharField(
        max_length=20,
        choices=COMPATIBILITY_CHOICES,
        default='universal'
    )

    def __str__(self):
        return self.name