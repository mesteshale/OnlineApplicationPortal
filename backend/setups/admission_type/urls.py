from django.urls import path
from setups.admission_type import views

urlpatterns = [
    path('admission-types/', views.AdmissionTypeList.as_view(), name='admission-type-list'),
    path('admission-types/<int:pk>/', views.AdmissionTypeDetail.as_view(), name='admission-type-detail'),
    path('admission-types/delete/<int:pk>/', views.AdmissionTypeDelete.as_view(), name='admission-type-delete'),
]