from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login, logout_then_login
from accounts.views import Index


urlpatterns = [
    #url(r'^admin/', admin.site.urls),
]
