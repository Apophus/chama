import logging
from ..models import MemberAccount

logger = logging.getLogger(__name__)


def create_account(user):
    member_account = MemberAccount(
        member=user, account_number=user.member_number, is_active=True
    )

    member_account.save()
    logger.info(f'{member_account} created.')

    return member_account