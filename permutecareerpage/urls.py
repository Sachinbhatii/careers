from django.contrib import admin
from django.db import router
from django.urls import path,include
from rest_framework.routers import DefaultRouter
import careersapp
from careersapp.views import careersViewSet #, jobsViewset
from careersapp import views

# router = DefaultRouter()
# router.register('careers',careersViewSet)
# router.register('jobs',jobsViewset)
urlpatterns = [
    path('admin/',admin.site.urls),
    # path('api/', include(router.urls)),
    path('api/',include('careersapp.urls')),
    ]
