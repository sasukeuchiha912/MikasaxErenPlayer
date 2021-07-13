import asyncio
from typing import Callable, Coroutine, Dict, List, Tuple, Union

from pyrogram import Client as pbot
from pyrogram.types import Chat, Message, User


async def member_permissions(chat_id, user_id):
    perms = []
    member = await pbot.get_chat_member(chat_id, user_id)
    if member.can_post_messages:
        perms.append("can_post_messages")
    if member.can_edit_messages:
        perms.append("can_edit_messages")
    if member.can_delete_messages:
        perms.append("can_delete_messages")
    if member.can_restrict_members:
        perms.append("can_restrict_members")
    if member.can_promote_members:
        perms.append("can_promote_members")
    if member.can_change_info:
        perms.append("can_change_info")
    if member.can_invite_users:
        perms.append("can_invite_users")
    if member.can_pin_messages:
        perms.append("can_pin_messages")
    return perms
