from django.urls import path
from setups.department import views

urlpatterns = [

     path('departments/', views.DepartmentList.as_view(), name='department-list'),
     path('departments/<int:pk>/', views.DepartmentDetail.as_view(), name='department-detail'),
     path('departments/delete/<int:pk>/', views.DepartmentDelete.as_view(), name='department-delete'),
     path('departments/public/', views.PublicDepartmentList.as_view(), name='public-department-list'),

]