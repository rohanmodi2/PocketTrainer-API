from django.urls import path
from .views import GeminiAPIView

urlpatterns = [
    path('generate/', GeminiAPIView.as_view(), name='gemini-api'),
]
