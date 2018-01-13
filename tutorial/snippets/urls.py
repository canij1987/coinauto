from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('register/', views.register),
    path('profile/', views.ProfileList.as_view()),
    path('profile/<pk>/', views.ProfileDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)