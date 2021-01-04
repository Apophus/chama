from rest_framework import generics, status, viewsets

from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404

from .serializers import MemberSerializer, MemberAccountSerializer,\
    MemberTypeSerializer, GroupSerializer, CreditSerializer, DebitSerializer,\
        LoanSerializer
from ..models import Member, MemberType, MemberAccount, Group, Debit, Credit,\
    Loan


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

class GroupView(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()

class MemberListView(APIView):

    def get(self, request):
    
        queryset = MemberAccount.objects.all()
        data = MemberAccountSerializer(queryset, many=True).data

        return Response(data)
class MemberCreateView(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = MemberSerializer

class MemberDetails(APIView):
    
    def get(self, request, pk):
        member = get_object_or_404(Member, pk=pk)
        data = MemberSerializer(member).data

        return Response(data)

class MemberTypeView(viewsets.ModelViewSet):

    queryset = MemberType.objects.all()
    serializer_class = MemberTypeSerializer


class DebitView(viewsets.ModelViewSet):
    
    queryset = Debit.objects.all()
    serializer_class = DebitSerializer


class CreditView(viewsets.ModelViewSet):
    
    queryset = Credit.objects.all()
    serializer_class = CreditSerializer
    

class LoanView(viewsets.ModelViewSet):

    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
