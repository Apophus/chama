from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Group(models.Model):
    """
    Objects for members in the chama
    Inherits django's user model
    """
    name = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class MemberType(models.Model):
    """
    Object representation of type of members
    """

    name = models.CharField(max_length=250)
    code = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.code}'


class Member(User):
    """
    Objects for members in the chama
    Inherits django's user model

    """
    member_number = models.CharField(blank=True, null=True,
        max_length=100)
    member_type = models.ForeignKey(MemberType, blank=True,
        null=True, on_delete=models.PROTECT)
    id_number = models.CharField(max_length=60)

    def __str__(self):
        return f'{self.member_number} - {self.username}'

class MemberAccount(models.Model):
    """
    Account for members to transact
    """
    member = models.ForeignKey(Member, on_delete=models.PROTECT)
    account_number = models.CharField(max_length=50)
    date_joined = models.DateTimeField(auto_now=True)
    balance = models.FloatField(default=0.0)
    is_active = models.BooleanField(default=False)
    account_type = models.CharField(max_length=200)


class Debit(models.Model):
    
    reference = models.CharField(max_length=50)
    member_account = models.ForeignKey(MemberAccount, blank=True,\
        on_delete=models.CASCADE)
    date_debited = models.DateTimeField(auto_now_add=True)
    amount = models.CharField(max_length=50)

class Credit(models.Model):

    reference = models.CharField(max_length=50)
    member_account = models.ForeignKey(MemberAccount, blank=True, on_delete=models.CASCADE)
    date_credited = models.DateTimeField(auto_now_add=True)
    amount = models.CharField(max_length=50)

class Loan(models.Model):
    reference_number = models.CharField(max_length=200)
    member_account = models.ForeignKey(MemberAccount,
        on_delete=models.PROTECT)
    loan_type = models.CharField(max_length=200)
    loan_amount = models.FloatField()

    def __str__(self):
        return f'{self.member_account} - {self.reference_number}'
