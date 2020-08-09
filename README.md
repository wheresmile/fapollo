# fapollo
基于 flask 的 apollo 后端。

努力向标准化（文档化、可测试、可参考）推进。

## 依赖的框架
* [flask](https://flask.palletsprojects.com/) web 开发框架
* [gunicorn](https://docs.gunicorn.org/en/stable/) WSGI http 服务器
* [SQLAlchemy](https://docs.sqlalchemy.org/en/13/orm/tutorial.html) ORM框架
* [alembic](https://alembic.sqlalchemy.org/en/latest/index.html) 数据库迁移方案
* [pytest](https://docs.pytest.org/en/stable/index.html) 测试框架
* [marshmallow](https://marshmallow.readthedocs.io/en/stable/) 数据转换（ex.序列化）框架


## 本地运行

1. 克隆本项目源码到本地
1. 准备数据库
    ```sql
    # 正式执行时的数据库
    CREATE DATABASE `fapollo` DEFAULT CHARACTER SET = `utf8mb4`;
   
    # 执行单元测试需要的数据库
    CREATE DATABASE `fapollo_test` DEFAULT CHARACTER SET = `utf8mb4`;
   
    # 创建用户
    CREATE USER `admin`@`%` IDENTIFIED BY '123456';
    GRANT Create, Drop, Delete, Index, Insert, Lock Tables, Select, Update ON *.* TO `admin`@`%`;
    ```
1. 安装依赖 `pip install -r requirements/requirements.txt` (建议使用 [virtualenv](https://virtualenv.pypa.io/en/latest/) 环境)
1. 迁移数据结构到数据库
    ```bash
    alembic upgrade head
    ```
1. 修改 Makefile 中的 `SQLALCHEMY_DB_URI` 变量，然后执行 `make pytest` 运行测试用例
1. 修改 Makefile 中的 `SQLALCHEMY_DB_URI` 变量，然后执行 `make` 启动服务

## todo
   
- [ ] 安装与部署方案