from django.contrib import admin
from .models import Member, MemberAccount, MemberType, Loan, Debit, Credit,\
    Group
# Register your models here.


admin.site.register(Member)
admin.site.register(MemberAccount)
admin.site.register(MemberType)
admin.site.register(Loan)
admin.site.register(Debit)
admin.site.register(Credit)
admin.site.register(Group)