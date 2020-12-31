from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class MemberSerializer(serializers.ModelSerializer):
    pass

class MemberAccountSerializer(serializers.ModelSerializer):
    pass

class DebitSerializer(serializers.ModelSerializer):
    pass

class CreditSerializer(serializers.ModelSerializer):
    pass

class LoanSerializer(serializers.ModelSerializer):
    pass