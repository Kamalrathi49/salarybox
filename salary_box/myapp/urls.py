from django.urls import path
from django.conf.urls import url
from myapp import views

app_name = 'myapp'
urlpatterns = [
    url(r'^$', views.company, name='home'),
    url(r'^add-company/$', views.add_company, name='add-company'),
    url(r'^(?P<company_name>[\w\-\ ]+)delete-company/$', views.delete_company, name='delete-company'),
    url(r'^(?P<company_name>[\w\-\ ]+)/update-company/$', views.update_company, name='update-company'),
    url(r'^(?P<company_name>[\w\-\ ]+)/add-company/$', views.add_employee, name='add-employee'),
    url(r'^(?P<company_name>[\w\-\ ]+)/$', views.employee, name='employee'),
]