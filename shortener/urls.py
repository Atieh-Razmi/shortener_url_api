from django.urls import path
from .views import ShorterUrlView
from . import views
from rest_framework import routers


app_name = 'shortener'

urlpatterns = [
    path('shorten/', views.ShorterUrlView.as_view()),
    path('<str:shortener_url>', views.RedirectUrlView.as_view())
]

router = routers.SimpleRouter()
router.register('links', views.LinkViewSet)
urlpatterns += router.urls