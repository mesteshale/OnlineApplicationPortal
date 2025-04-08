from rest_framework import generics
from .models import Sponsorship
from .serializers import SponsorshipSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

# Sponsorship List and Create View
class SponsorshipList(generics.ListCreateAPIView):
    queryset = Sponsorship.objects.all()
    serializer_class = SponsorshipSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsAdminUser()]

# Sponsorship Detail, Update, and Delete View
class SponsorshipDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sponsorship.objects.all()
    serializer_class = SponsorshipSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsAdminUser()]


# Public Sponsorship List View (no authentication required)
class PublicSponsorshipList(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        sponsorships = Sponsorship.objects.all()
        serializer = SponsorshipSerializer(sponsorships, many=True)
        return Response(serializer.data)