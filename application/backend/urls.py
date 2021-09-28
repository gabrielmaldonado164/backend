# -*- coding: utf-8 -*-

# Python

# Django
from django.contrib                 import admin
from django.conf                    import settings
from django.urls                    import include
from django.urls                    import path
from rest_framework                 import routers
from rest_framework.authtoken.views import obtain_auth_token

# Custom

router = routers.DefaultRouter()

urlpatterns = [
    path('garmin/', admin.site.urls),

    # Django Rest
    path('api/base/', include(router.urls)),
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/auth/token/', obtain_auth_token),

    path('tickets/',include('tickets.urls'))

]

 # API V1
if settings.DEBUG:
    urlpatterns.append(path('api/v1/', include('v1.urls')))
else:
    urlpatterns.append(path('api/v1/', include('v1.urls')))