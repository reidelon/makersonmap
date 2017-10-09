from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^save_coord/$', views.save_coordinates, name='save_coord'),
    url(r'^reset_data/$', views.reset_data, name='reset_data'),
]
