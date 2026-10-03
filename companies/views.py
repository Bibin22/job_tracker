from django.shortcuts import render
from rest_framework.views import APIView
from .models import Company
from .serializers import CompanySerializer
from users.permissions import IsRecruiter
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .pagination import CompanyPagination
class CompanyManagementView(APIView):
    permission_classes = [IsRecruiter]

    def post(self, request):
        data = request.data
        serializer = CompanySerializer(data=data)
        if serializer.is_valid():
            serializer.save(recruiter=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def get(self, request, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            company = get_object_or_404(
                Company,
                id=pk,
                recruiter=request.user
            )
            serializer = CompanySerializer(company)
            return Response(serializer.data)

        else:
            companies = Company.objects.filter(recruiter_id=request.user.id)

            paginator = CompanyPagination()
            page = paginator.paginate_queryset(companies, request)

            serializer = CompanySerializer(page, many=True)

            return paginator.get_paginated_response(serializer.data)


    def patch(self, request, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            company = Company.objects.get(id=pk, recruiter=request.user)
            serializer = CompanySerializer(company, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
        return Response({"success":True}, status=status.HTTP_200_OK)

    def delete(self, request,  **kwargs):
        pk = kwargs.get('pk')
        if pk:
            company = get_object_or_404(
                Company,
                id=pk,
                recruiter=request.user
            )

            company.delete()

            return Response(
                status=status.HTTP_204_NO_CONTENT
            )



# Create your views here.
