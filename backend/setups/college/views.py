# Django imports
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, CollegeSerializer, UserDetailSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from setups.college.models import College

# List and Create view for College (GET, POST)
class CollegeList(generics.ListCreateAPIView):
    serializer_class = CollegeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return College.objects.all()

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)

# Delete view for College (DELETE)
class CollegeDelete(generics.DestroyAPIView):
    serializer_class = CollegeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return College.objects.all()

# Retrieve and Update view for a single College (GET, PUT)
class CollegeDetail(generics.RetrieveUpdateAPIView):
    serializer_class = CollegeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return College.objects.all()

# Public list view for College (GET)
class PublicCollegeList(generics.ListAPIView):
    serializer_class = CollegeSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return College.objects.all()

# #####################################################################################################
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class CheckUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')

        if not username and not email:
            return Response(
                {'error': 'Please provide either username or email'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if username:
            user = User.objects.filter(username=username).first()
        else:
            user = User.objects.filter(email=email).first()

        if user:
            return Response({
                'exists': True,
                'username': user.username,
                'email': user.email
            })
        else:
            return Response({'exists': False})


class CurrentUserView(APIView):
    """View to retrieve the current authenticated user's details"""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserDetailSerializer(request.user)
        return Response(serializer.data)
