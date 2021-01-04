from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

from .api_views import MemberDetails, MemberCreateView, MemberTypeView,\
    MemberListView, GroupView, LoanView, CreditView, DebitView

router = DefaultRouter()
router.register('create_membertype', MemberTypeView,\
     basename='create_membertype')
router.register('groups', GroupView,\
     basename='groups')
router.register('loan', LoanView,\
     basename='loans')
router.register('debit', DebitView,\
     basename='debit')
router.register('credit', CreditView,\
     basename='credit')
schema_view = get_swagger_view(title='Chama API')

urlpatterns = [
    path('create_member/', MemberCreateView.as_view(), name='create_member'),
    path('members_list/', MemberListView.as_view(), name='member_list')
]

urlpatterns += router.urls