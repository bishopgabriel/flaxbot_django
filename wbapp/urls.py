from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('user/<int:user_id>/', views.user_profile, name='user_profile'),
]
