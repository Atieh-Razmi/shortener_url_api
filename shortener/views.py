from django.shortcuts import render
from .models import Link
from rest_framework import status
from rest_framework.views import APIView 
from .serilizers import LinkSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import get_object_or_404, redirect
# Create your views here.

class ShorterUrlView(APIView):
    def post(self, request):
        srz_data = LinkSerializer(data=request.data)
        if srz_data.is_valid():
            link = srz_data.save()
            return Response({
                "original_url" : link.origin_url,
                "short_url": f'{request.get_host()}/{link.shortener_url}'
            })
        return Response(data=srz_data.errors, status=status.HTTP_400_BAD_REQUEST)
    

class RedirectUrlView(APIView):
    def get(self, request, shortener_url):
        link = get_object_or_404(Link, shortener_url=shortener_url)
        return redirect(link.origin_url)

    

class LinkViewSet(viewsets.ViewSet):
    queryset = Link.objects.all()

    def list(self, request):
        srz_data = LinkSerializer(instance=self.queryset, many=True)
        return Response(data=srz_data.data)

    def create(self, request):
        srz_data = LinkSerializer(data=request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(data=srz_data.data)
        return Response(data=srz_data.errors)


