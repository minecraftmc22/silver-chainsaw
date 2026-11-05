"""添加用户功能 —— 组长负责开发"""
from fastapi import APIRouter, HTTPException

from models import User, UserOut
from storage import add_user, username_exists, email_exists

router = APIRouter(prefix="/users", tags=["添加用户(组长)"])


@router.post("", response_model=UserOut, summary="添加用户")
def create_user(user: User):
    """
    添加用户接口：
    - 用户名不能重复
    - 邮箱不能重复
    - 添加成功返回用户信息（不含密码）
    """
    if username_exists(user.username):
        raise HTTPException(status_code=400, detail=f"用户名 '{user.username}' 已存在")
    if email_exists(user.email):
        raise HTTPException(status_code=400, detail=f"邮箱 '{user.email}' 已被注册")

    saved = add_user(user)
    return UserOut(
        id=saved.id,
        username=saved.username,
        email=saved.email,
        nickname=saved.nickname,
    )
