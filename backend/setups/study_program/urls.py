from django.urls import path
from setups.study_program import views

urlpatterns = [
    path('study-programs/', views.StudyProgramList.as_view(), name='study-program-list'),    
    path('study-programs/<int:pk>/', views.StudyProgramDetail.as_view(), name='study-program-detail'),
    path('study-programs/delete/<int:pk>/', views.StudyProgramDelete.as_view(), name='study-program-delete'),
]