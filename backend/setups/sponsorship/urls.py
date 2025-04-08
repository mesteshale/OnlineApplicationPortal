from django.urls import path
from .views import SponsorshipList, SponsorshipDetail, PublicSponsorshipList

urlpatterns = [
    path('', SponsorshipList.as_view(), name='sponsorship-list'),
    path('<int:pk>/', SponsorshipDetail.as_view(), name='sponsorship-detail'),
    path('public/', PublicSponsorshipList.as_view(), name='public-sponsorship-list'),
]
