from rest_framework import serializers
from .models import Link


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model=Link
        fields = '__all__'
        #fields=['shortener_url','origin_url', 'created']
        read_only_fields = ['shortener_url',]