from django.urls import path
from .views import citations_view

urlpatterns = [
    path('citations/', citations_view, name='citations'),
]
