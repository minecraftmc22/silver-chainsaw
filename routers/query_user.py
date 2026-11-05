"""查询用户功能 —— 组员负责开发"""
from typing import List, Optional

from fastapi import APIRouter, HTTPException, Query

from models import UserOut
from storage import get_all, get_by_id, get_by_username

router = APIRouter(prefix="/users", tags=["查询用户(组员)"])


@router.get("", response_model=List[UserOut], summary="查询用户列表")
def list_users(
    keyword: Optional[str] = Query(None, description="按用户名/昵称模糊搜索"),
    page: int = Query(1, ge=1, description="页码，从1开始"),
    page_size: int = Query(10, ge=1, le=100, description="每页条数"),
):
    """
    查询用户列表：
    - 支持 keyword 模糊搜索（匹配用户名或昵称）
    - 支持 page / page_size 分页
    """
    users = get_all()

    if keyword:
        users = [u for u in users if keyword in u.username or (u.nickname and keyword in u.nickname)]

    start = (page - 1) * page_size
    end = start + page_size

    return [
        UserOut(id=u.id, username=u.username, email=u.email, nickname=u.nickname)
        for u in users[start:end]
    ]


@router.get("/{user_id}", response_model=UserOut, summary="按ID查询用户")
def get_user_by_id(user_id: int):
    """按用户 id 精确查询，不存在返回 404"""
    user = get_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail=f"id 为 {user_id} 的用户不存在")
    return UserOut(id=user.id, username=user.username, email=user.email, nickname=user.nickname)


@router.get("/name/{username}", response_model=UserOut, summary="按用户名查询")
def get_user_by_name(username: str):
    """按用户名精确查询，不存在返回 404"""
    user = get_by_username(username)
    if user is None:
        raise HTTPException(status_code=404, detail=f"用户名 '{username}' 不存在")
    return UserOut(id=user.id, username=user.username, email=user.email, nickname=user.nickname)
