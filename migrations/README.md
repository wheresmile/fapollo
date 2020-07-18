# 迁移

* 生成数据库
```sql 
CREATE DATABASE `fapollo` DEFAULT CHARACTER SET = `utf8mb4`;
```

* 自动生成迁移文件
```bash
alembic revision --autogenerate -m "init"
```

* 自动迁移
```bash
alembic upgrade head
```