from django.urls import path

from . import views

app_name = 'consumers'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('list', views.ListView.as_view(), name='list'),
    path('add', views.AddView.as_view(), name='add'),
]
