# silver-chainsaw —— 用户管理系统（Python + FastAPI 结对项目）

两人结对完成用户管理功能，组长负责**添加用户**，组员负责**查询用户**，
各自在独立分支开发，最终由组长合并到 `dev` 分支。

## 项目结构

```
main.py                # FastAPI 主应用，注册两个功能路由
models.py              # Pydantic 数据模型（组长维护）
storage.py             # 内存存储层，模拟数据库（组长维护）
routers/add_user.py    # 添加用户功能（组长开发）
routers/query_user.py  # 查询用户功能（组员开发）
requirements.txt       # 依赖清单
```

## 快速开始

```bash
pip install -r requirements.txt
uvicorn main:app --reload
# 浏览器打开 http://127.0.0.1:8000/docs 查看接口文档
```

## 接口说明

### 添加用户（组长）
| 方法 | 路径 | 说明 |
|------|------|------|
| POST | `/users` | 添加用户，用户名/邮箱重复返回 400 |

### 查询用户（组员）
| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/users` | 用户列表，支持 `keyword` 模糊搜索 + `page`/`page_size` 分页 |
| GET | `/users/{user_id}` | 按 id 查询，不存在返回 404 |
| GET | `/users/name/{username}` | 按用户名查询，不存在返回 404 |

## 接口测试示例

```bash
# 添加用户
curl -X POST http://127.0.0.1:8000/users \
  -H "Content-Type: application/json" \
  -d '{"username":"zhangsan","email":"zs@test.com","password":"123456","nickname":"张三"}'

# 查询列表（模糊搜索）
curl "http://127.0.0.1:8000/users?keyword=张"

# 按 id 查询
curl http://127.0.0.1:8000/users/1
```

## 结对开发流程（Git 工作流）

```bash
# 1. 组长：本地初始化 + 创建远程仓库 + dev 分支
git init && git remote add origin <远程地址>
git checkout -b dev && git push -u origin dev

# 2. 组长：开发添加功能
git checkout -b feature/add-user
# ... 编写 routers/add_user.py
git commit -m "组长: 实现添加用户功能"

# 3. 组员：克隆仓库后拉取 dev，开发查询功能
git checkout dev && git pull origin dev
git checkout -b feature/query-user
# ... 编写 routers/query_user.py
git commit -m "组员: 实现查询用户功能"

# 4. 组长：将两个功能分支依次合并到 dev
git checkout dev
git merge --no-ff feature/add-user
git merge --no-ff feature/query-user

# 5. 推送 dev 到远程
git push origin dev
```
