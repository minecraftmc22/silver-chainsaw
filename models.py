"""数据模型定义 —— 组长负责维护"""
from pydantic import BaseModel, Field
from typing import Optional


class User(BaseModel):
    """用户实体"""
    id: Optional[int] = None
    username: str = Field(..., min_length=2, max_length=20, description="用户名，2-20个字符")
    email: str = Field(..., description="邮箱")
    password: str = Field(..., min_length=6, description="密码，至少6位")
    nickname: Optional[str] = Field(None, description="昵称")


class UserOut(BaseModel):
    """对外返回的用户信息（不暴露密码）"""
    id: int
    username: str
    email: str
    nickname: Optional[str] = None
