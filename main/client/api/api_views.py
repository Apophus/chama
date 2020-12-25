from rest_framework import generics, status, viewsets

from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404

from ..models import Member


class LoginView(APIView):
    permission_classes = ()

    def post(self, request):
        user_name = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=user_name, password=password)

        if user:
            return Response({'token': user.auth_token.key}, \
                status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Wrong credentials'}, \
                status=status.HTTP_400_BAD_REQUEST)

class MemberDetails(APIView):
    
    def get(self, request, pk):
        member = get_object_or_404(Member, pk=pk)
        data = PollSerializer(member).data

        return Response(data)

class DebitView(APIView):
    
    def get(self, request):
        pass


class CreditView(APIView):
    
    def get(self, request):
        pass

    def post(self, request):
        pass
    

class LoanView(APIView):

    def get(self, request):
        pass

    def post(self, request):
        pass
