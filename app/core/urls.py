from django.urls import include, path
from . import views

urlpatterns = [
    path('hello/', views.HelloApiView.as_view()),
]
