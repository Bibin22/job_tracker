from rest_framework.viewsets import generics
from rest_framework.views import APIView
from django.shortcuts import render
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
# Create your views here.
from rest_framework.response import Response
from rest_framework import status


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = self.request.user
        full_name  = f"{user.first_name} {user.last_name}".strip()
        return Response({'user_id':user.id, 'name':full_name, 'email':user.email}, status=status.HTTP_200_OK)

    def patch(self, request):
        data = request.data
        first_name = data.get('first_name')
        last_name = data.get('last_name')

        user = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.save(update_fields=['first_name', 'last_name'])
        return Response({'msg':'user data successfully updated'}, status=status.HTTP_200_OK)


class PasswordChangeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        old_password = data.get('old_password')
        new_password = data.get('new_password')
        user = request.user
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return Response({'msg': 'user data successfully updated'}, status=status.HTTP_200_OK)

        return Response(
            {"error": "Old password is incorrect"},
            status=status.HTTP_400_BAD_REQUEST
        )



