"""用户管理功能 —— 两人结对项目
组长：添加用户功能（feature/add-user）
组员：查询用户功能（feature/query-user）
"""
from fastapi import FastAPI

from routers import add_user, query_user

app = FastAPI(title="用户管理系统", description="结对开发：添加 + 查询", version="1.0.0")

# 注册两个功能模块的路由
app.include_router(add_user.router)
app.include_router(query_user.router)


@app.get("/")
def root():
    return {"msg": "用户管理系统运行中", "docs": "/docs"}
