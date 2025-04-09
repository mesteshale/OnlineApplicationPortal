from django.urls import path
from setups.application_information import views

urlpatterns = [
    path('application-information/', views.ApplicationInformationList.as_view(), name='application-information-list'),
    path('application-information/<int:pk>/', views.ApplicationInformationDetail.as_view(), name='application-information-detail'),
    path('application-information/delete/<int:pk>/', views.ApplicationInformationDelete.as_view(), name='application-information-delete'),
    path('application-information/filter/', views.ApplicationInformationFilter.as_view(), name='application-information-filter'),
]