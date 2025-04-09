from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from setups.college.views import CreateUserView, CurrentUserView
from rest_framework_simplejwt.views import TokenRefreshView
from setups.college.jwt_serializers import CustomTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/register/', CreateUserView.as_view(), name='user-register'),
    path('api/user/me/', CurrentUserView.as_view(), name='current-user'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
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
    path('api/sponsorships/', include('setups.sponsorship.urls')),
    path('api/', include('registration.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

