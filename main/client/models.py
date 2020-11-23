from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Member(User):
    """
    Objects for members in the chama
    Inherits django's user model

    """
    member_number = models.CharField(blank=True, null=True,
        max_length=100)
    member_type = models.ForeignKey(MemberType, blank=True,
        null=True)
    id_number = models.CharField(max_length=60)

    def __str__(self):
        return f'{self.member_number} - {self.username}'


class MemberType(models.Model):
    """
    Object representation of type of members
    """

    name = models.CharField(max_length=250)
    code = models.CharField(max_lenght=250)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.code}'
