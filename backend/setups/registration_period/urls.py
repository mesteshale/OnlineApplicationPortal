from django.urls import path
from setups.registration_period import views

urlpatterns = [
    path('registration-periods/', views.RegistrationPeriodList.as_view(), name='registration-period-list'),
    path('registration-periods/<int:pk>/', views.RegistrationPeriodDetail.as_view(), name='registration-period-detail'),
    path('registration-periods/delete/<int:pk>/', views.RegistrationPeriodDelete.as_view(), name='registration-period-delete'),
]