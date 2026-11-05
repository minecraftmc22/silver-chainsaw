"""内存存储层 —— 组长负责维护"""
from typing import Dict, Optional
from models import User

# 模拟数据库：用户名 -> User
_users: Dict[str, User] = {}
# 自增主键
_next_id: int = 1


def add_user(user: User) -> User:
    """新增用户，自动分配 id"""
    global _next_id
    user.id = _next_id
    _next_id += 1
    _users[user.username] = user
    return user


def get_by_username(username: str) -> Optional[User]:
    """按用户名精确查询"""
    return _users.get(username)


def get_by_id(user_id: int) -> Optional[User]:
    """按 id 查询"""
    for u in _users.values():
        if u.id == user_id:
            return u
    return None


def get_all() -> list:
    """返回全部用户"""
    return list(_users.values())


def username_exists(username: str) -> bool:
    return username in _users


def email_exists(email: str) -> bool:
    return any(u.email == email for u in _users.values())
