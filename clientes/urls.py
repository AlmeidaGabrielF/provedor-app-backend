from django.urls import path
from .views import ClienteListCreateView

urlpatterns = [
    path('clientes/', ClienteListCreateView.as_view()),
]

from .views import LoginView
urlpatterns = [ path('login/', LoginView.as_view()), ]
