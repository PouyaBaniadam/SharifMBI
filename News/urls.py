from django.urls import path

from News import views

app_name = 'news'

urlpatterns = [
    path('list', views.AllNews.as_view(), name='all'),
    path('detail/<slug>', views.NewsDetail.as_view(), name='detail'),
    path('category/<slug>', views.NewsByCategory.as_view(), name='by_category'),
]
