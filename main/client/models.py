from django.db import models
from django.contrib.auth.models import User

from .helpers.generate_codes import get_unique_code

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
        return f'{self.name} - {self.location}'


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
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=60)

    def __str__(self):
        return f'{self.first_name}  {self.last_name} - {self.member_number}'

    def save(self, *args, **kwargs):

        if not self.member_number:

            self.member_number = get_unique_code()
        super(Member, self).save(* args, ** kwargs)

        

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


    def __str__(self):
        return f'{self.member.username} - {self.account_number}'
    

    def save(self, *args, **kwargs):
    
        if not self.account_number:

            self.account_number = get_unique_code()
        super(MemberAccount, self).save(* args, ** kwargs)


class Debit(models.Model):
    
    reference = models.CharField(max_length=50)
    member_account = models.ForeignKey(MemberAccount, blank=True,\
        on_delete=models.CASCADE)
    date_debited = models.DateTimeField(auto_now_add=True)
    amount = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.member_account} - {self.reference}'

    def save(self, *args, **kwargs):
        
        if not self.reference:

            self.reference = get_unique_code()
        super(MemberAccount, self).save(* args, ** kwargs)

class Credit(models.Model):

    reference = models.CharField(max_length=50)
    member_account = models.ForeignKey(MemberAccount, blank=True, on_delete=models.CASCADE)
    date_credited = models.DateTimeField(auto_now_add=True)
    amount = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.member_account} - {self.reference}'

class Loan(models.Model):
    reference_number = models.CharField(max_length=200)
    member_account = models.ForeignKey(MemberAccount,
        on_delete=models.PROTECT)
    loan_type = models.CharField(max_length=200)
    loan_amount = models.FloatField()

    def __str__(self):
        return f'{self.member_account} - {self.reference_number}'
