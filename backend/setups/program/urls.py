from django.urls import path
from setups.program import views

urlpatterns = [
    path('programs/', views.ProgramList.as_view(), name='program-list'),
    path('programs/<int:pk>/', views.ProgramDetail.as_view(), name='program-detail'),
    path('programs/delete/<int:pk>/', views.ProgramDelete.as_view(), name='program-delete'),
    path('programs/public/', views.PublicProgramList.as_view(), name='public-program-list'),
]