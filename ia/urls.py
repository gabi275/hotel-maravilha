from django.urls import path
from .views import AssistenteView

urlpatterns = [path("", AssistenteView.as_view(), name="assistente_ia")]
