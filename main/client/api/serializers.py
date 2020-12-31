from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from ..models import MemberAccount, Loan, Debit, Credit, Member


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

        return user

class MemberAccountSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MemberAccount
        fields = '__all__'

class DebitSerializer(serializers.ModelSerializer):
    pass

class CreditSerializer(serializers.ModelSerializer):
    pass

class LoanSerializer(serializers.ModelSerializer):
    pass