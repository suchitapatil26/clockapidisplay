from django.conf.urls import url
from clockapi import views


urlpatterns = [
url(r'^time/([\d]{1,2}:?[\d]{1,2})/$',views.currentDateTime),
]