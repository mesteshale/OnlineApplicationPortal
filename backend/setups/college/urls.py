from django.urls import path 
from setups.college import views

urlpatterns = [
     path('colleges/', views.CollegeList.as_view(), name='college-list'),
     path('colleges/<int:pk>/', views.CollegeDetail.as_view(), name='college-detail'),
     path('colleges/delete/<int:pk>/', views.CollegeDelete.as_view(), name='college-delete'),
     
]
