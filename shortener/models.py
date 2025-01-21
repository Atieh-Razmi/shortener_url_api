from typing import Iterable
from django.db import models
from django.utils.crypto import get_random_string
# Create your models here.

class Link(models.Model):
    origin_url = models.URLField(max_length=2048)
    shortener_url = models.URLField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.shortener_url
    
    def generate_short_url(self):
        while True:
            short_code = get_random_string(length=6)
            if not Link.objects.filter(short_code=self.shortener_url).exists():
                return short_code

    def save(self, *args, **kwargs):
        if not self.shortener_url:
            self.shortener_url=self.get_random_string()
        super().save(*args,**kwargs)