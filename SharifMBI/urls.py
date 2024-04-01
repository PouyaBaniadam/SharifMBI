"""
URL configuration for SharifMBI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from SharifMBI import settings

urlpatterns = ([
                   path('admin/', admin.site.urls),
                   path("", include("Home.urls")),
                   path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
                   path("account/", include("Account.urls")),
                   path("us/", include("Us.urls")),
                   path("weblog/", include("Weblog.urls")),
                   path("news/", include("News.urls")),
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
