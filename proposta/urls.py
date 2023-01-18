# -*- Mode: Python; coding: utf-8 -*-
from django.conf.urls import *
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.conf import settings
from . import views
#from rest_framework.urlpatterns import format_suffix_patterns

admin.site.site_header = 'Brasil Geradores'            # default: "Django Administration"
admin.site.index_title = 'ADMINISTRAÇÃO'               # default: "Site administration"
admin.site.site_title = 'BRG'                          # default: "Django site admin"

urlpatterns = [
	path('proposta/<int:id>/', views.proposta, name='proposta'),
    path('', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#urlpatterns = format_suffix_patterns(urlpatterns)