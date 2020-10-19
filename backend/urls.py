from django.contrib import admin
from django.urls import path, include  
from dashboard.views import Tab1MapView, DashboardView, AreaView          
from rest_framework import routers                                    

router = routers.SimpleRouter()                     
router.register(r'tabs', DashboardView, basename='drop') 
router.register(r'tab1', Tab1MapView, basename='maps')    
router.register(r'areaList', AreaView, 'area')     # add this

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))               
]
