"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Import from core app
from octofit_tracker.core import views as core_views

router = DefaultRouter()
router.register(r'users', core_views.UserViewSet)
router.register(r'teams', core_views.TeamViewSet)
router.register(r'activities', core_views.ActivityViewSet)
router.register(r'workouts', core_views.WorkoutViewSet)
router.register(r'leaderboard', core_views.LeaderboardViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.api_root, name='api-root'),
    path('', include(router.urls)),
]
