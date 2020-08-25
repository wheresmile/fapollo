
# 本地运行
.PHONY: run_local
run_local: migrate
	export DEBUG=True \
	&& export FLASK_ENV=development \
	&& export SQLALCHEMY_DB_URI=mysql+pymysql://root:123456@localhost/fapollo?charset=utf8mb4 \
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


.PHONY: fabric
fabric:
	fab -H ubuntu@122.51.176.214  -i ~/.ssh/id_rsa  deploy


# 使用 gunicorn 运行（仅参考）
.PHONY: run_gunicorn
run_gunicorn:
	export SQLALCHEMY_DB_URI=mysql+pymysql://root:123456@localhost/fapollo?charset=utf8mb4 \
	&& gunicorn -c apollo/gunicorn_config.py main:app