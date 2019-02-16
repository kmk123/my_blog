from django.urls import path,include
from django.conf.urls import url
from . import views
from rest_framework import routers
router=routers.DefaultRouter()
router.register('',views.BlogAPI)
from rest_framework.authtoken import views
app_name='api'

urlpatterns = [
    path('',include(router.urls) ),
    url(r'^get-api-token',views.obtain_auth_token,name='get-api-token'),
]