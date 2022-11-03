from django.urls import path, include
from rest_framework import routers
from .views import CompanyViewset, EmployeeViewset

router = routers.DefaultRouter()
router.register('company', CompanyViewset)
router.register('employee', EmployeeViewset)

urlpatterns = [
    path('api/', include(router.urls)),
]