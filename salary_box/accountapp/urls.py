from django.urls import path
from django.conf.urls import url
from accountapp import views

app_name = 'accountapp'
urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout/$', views.log_out, name='logout'),
    url(r'^login/$', views.log_in, name='login'),
]