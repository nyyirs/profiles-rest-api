from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('hello/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]
