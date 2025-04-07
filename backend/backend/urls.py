from django.contrib import admin
from django.urls import path, include   
from setups.college.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/register/', CreateUserView.as_view(), name='user-register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls')), 
    path('api/', include('setups.college.urls')),
    path('api/', include('setups.department.urls')),
    path('api/', include('setups.admission_type.urls')),
    path('api/', include('setups.application_information.urls')),
    path('api/', include('setups.program.urls')),
    path('api/', include('setups.registration_period.urls')),
    path('api/', include('setups.study_field.urls')),
    path('api/', include('setups.study_program.urls')),
    path('api/', include('registration.urls')),
]

