from typing import Iterable
from django.db import models
from django.utils.crypto import get_random_string
# Create your models here.

class Link(models.Model):
    origin_url = models.URLField(max_length=2048)
    shortener_url = models.URLField(max_length=20, blank=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.shortener_url
    
    def generate_short_url(self):
        while True:
            short_code = get_random_string(length=6)
            if not Link.objects.filter(shortener_url=short_code).exists():
                return short_code

    def save(self, *args, **kwargs):
        if not self.shortener_url:
            self.shortener_url=self.generate_short_url()
        super().save(*args,**kwargs)