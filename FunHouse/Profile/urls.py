__author__ = 'Saleh'
from django.conf.urls import url,include
from .views import user_profile
from django.contrib.auth.decorators import login_required
app_name = 'profile'
urlpatterns = [
url(r'^(?P<pk>\d+)',user_profile,name='user')
]