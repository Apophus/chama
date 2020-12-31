from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from ..models import MemberAccount, Loan, Debit, Credit, Member


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Member
        fields = ('username', 'email', 'password', 'member_number', 'id_number')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Member(email=validated_data['email'], \
            username=validated_data['username'],
            id_number=validated_data['id_number'])

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