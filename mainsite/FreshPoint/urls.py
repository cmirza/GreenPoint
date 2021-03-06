from django.conf.urls import url
from . import views

app_name = 'FreshPoint'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^results/$', views.results, name='results'),
    url(r'^detail/(?P<url_key>\d+)/$', views.detail, name='detail'),
]
