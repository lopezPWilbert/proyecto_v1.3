from django.conf.urls import include
from django.contrib import admin

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views


from django.contrib.auth.views import login, logout_then_login

#configuracion de media
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
##################3

from django.views.generic.base import RedirectView
from allauth.account.views import *


urlpatterns = [
    url(r'contador/', app.views.contador.as_view(), name='contador'),
    # Examples:
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$',RedirectView.as_view(url='accounts/login/')),
	url(r'^denuncia/$', app.views.Denuncia, name='denuncia_view'),
	url(r'^accounts/', include('allauth.urls')),
	url(r'^mapa/$',app.views.Mapa.as_view(),name='mapa_view'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)