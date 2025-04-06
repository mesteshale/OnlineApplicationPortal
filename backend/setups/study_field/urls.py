from django.urls import path
from setups.study_field import views

urlpatterns = [
    path('study-fields/', views.StudyFieldList.as_view(), name='study-field-list'),
    path('study-fields/<int:pk>/', views.StudyFieldDetail.as_view(), name='study-field-detail'),
    path('study-fields/delete/<int:pk>/', views.StudyFieldDelete.as_view(), name='study-field-delete'),
]