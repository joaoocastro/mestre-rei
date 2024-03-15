from django.urls import path, include
from .views import BarbeiroCreateView

urlpatterns = [
    path('barbeiro-create/',BarbeiroCreateView),
]
