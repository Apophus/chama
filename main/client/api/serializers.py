import logging
from rest_framework import serializers, filters
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
# from django_filters.rest_framework import DjangoFilterBackend   

from ..models import MemberAccount, Loan, Debit, Credit, Member, MemberType,\
    Group
from ..helpers.account_creation import create_account

logger = logging.getLogger(__name__)


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Group

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Member
        fields = ('first_name', 'last_name','username', 'email', 'password', 'member_number',\
             'id_number', 'group')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Member(first_name=validated_data['first_name'],\
            last_name=validated_data['last_name'],
            email=validated_data['email'], \
            username=validated_data['username'],
            id_number=validated_data['id_number'],
            group=validated_data['group'])

        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        logger.info(f'{user} token created. Creating account')
        account = create_account(user)
        logger.info('Account creation complete')
        return user

class MemberAccountSerializer(serializers.ModelSerializer):
    
    member_name = serializers.SerializerMethodField()
    class Meta:
        model = MemberAccount
        fields = '__all__'

    def get_member_name(self, obj):

        names = f'{obj.member.first_name} {obj.member.last_name}'

        return names
class MemberTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = MemberType
        fields = '__all__'


class DebitSerializer(serializers.ModelSerializer):
    pass

class CreditSerializer(serializers.ModelSerializer):
    pass

class LoanSerializer(serializers.ModelSerializer):
    pass