from django.contrib import admin
from django.urls import path, include                 # add this
from rest_framework import routers                    # add this
from dashboard import views                            # add this

router = routers.DefaultRouter()                      # add this
router.register(r'utdata', views.DashboardView, 'dashboard')     # add this

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))                # add this
]
