from django.urls import path

from Home import views

app_name = "home"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
]
