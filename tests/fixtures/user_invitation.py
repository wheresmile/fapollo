# -*- coding: utf-8 -*-
from models.user_invitaton import UserInvitation
from tests.fixtures.user import user_admin

user_invitation_1 = UserInvitation(
    id=1,
    user_id=user_admin.id,
    code="1234567",
    is_used=False,
)

user_invitation_used = UserInvitation(
    id=2,
    user_id=user_admin.id,
    code="12345678",
    is_used=True,
)


