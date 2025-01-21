from django.shortcuts import render
from .models import Link
from rest_framework import status
from rest_framework.views import APIView 
from .serilizers import LinkSerializer
from rest_framework.response import Response
# Create your views here.

class ShorterUrlView(APIView):
    def post(self, request):
        srz_data = LinkSerializer(data=request.POST)
        if srz_data.is_valid():
            srz_data.save()
            return Response(data=srz_data.data)
        return Response(data=srz_data.errors)
