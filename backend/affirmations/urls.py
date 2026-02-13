from django.urls import path
from . import views
urlpatterns = [
    path('affirmation/', views.generate_affirmation, name='generate_affirmation'),
]
