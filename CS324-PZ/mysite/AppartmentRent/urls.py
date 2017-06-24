from django.conf.urls import url

from . import views

app_name = 'AppartmentRent'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/reservation/$', views.ReservationView.as_view(), name='reservation'),
    url(r'^success/$', views.SuccessView.as_view(), name='success'),
    url(r'^error/$', views.ErrorView.as_view(), name='error'),
    url(r'^destinations/$', views.DestinationsView.as_view(), name='destinations'),
    url(r'^reserve/(?P<appartmentId>\d+)/$', views.reserve, name='reserve'),
]