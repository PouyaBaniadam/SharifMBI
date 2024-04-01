from django.urls import path

from Diagnose import views

app_name = "diagnose"

urlpatterns = [
    path("form", views.DiagnoseFormView.as_view(), name="form"),
    path('download/', views.DownloadFileView.as_view(), name='download_file'),
]
