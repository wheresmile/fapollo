
# 本地运行
.PHONY: run_local
run_local: migrate
	export DEBUG=True \
	&& export FLASK_ENV=development \
	&& python main.py


# 测试
.PHONY: pytest
pytest:
	export SQLALCHEMY_DB_URI=mysql+pymysql://root:123456@localhost/fapollo_test?charset=utf8mb4 && \
	export SQLALCHEMY_ECHO=False \
	&& pytest .


# 迁移
.PHONY: migrate
migrate:
	alembic upgrade head