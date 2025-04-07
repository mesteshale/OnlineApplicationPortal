from django.urls import path
from . import views  # Change this line - import views directly from the app

urlpatterns = [
    # ApplicantInformation URLs
    path('applicant-info/', views.ApplicantInformationList.as_view(), name='applicant-info-list'),
    path('applicant-info/<int:pk>/', views.ApplicantInformationDetail.as_view(), name='applicant-info-detail'),
    
    # ApplicantGAT URLs
    path('applicant-gat/', views.ApplicantGATList.as_view(), name='applicant-gat-list'),
    path('applicant-gat/<int:pk>/', views.ApplicantGATDetail.as_view(), name='applicant-gat-detail'),
    
    # ApplicantProgramSelection URLs
    path('program-selection/', views.ApplicantProgramSelectionList.as_view(), name='program-selection-list'),
    path('program-selection/<int:pk>/', views.ApplicantProgramSelectionDetail.as_view(), name='program-selection-detail'),
    
    # ApplicantDocumentation URLs
    path('documentation/', views.ApplicantDocumentationList.as_view(), name='documentation-list'),
    path('documentation/<int:pk>/', views.ApplicantDocumentationDetail.as_view(), name='documentation-detail'),
    
    # ApplicantPayment URLs
    path('payment/', views.ApplicantPaymentList.as_view(), name='payment-list'),
    path('payment/<int:pk>/', views.ApplicantPaymentDetail.as_view(), name='payment-detail'),
]
