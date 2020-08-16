# 配置

在 fapollo 中，主要存在两大块配置，①运行时 flask、gunicorn 的配置，和②部署时 环境变量、nginx、supervisor 等的配置。

## 运行时配置

#### flask 的配置（项目核心配置）

整个 app 正常运行时，需要配置数据库、秘钥、定时任务等相关变量。在 fapollo 项目中，主要通过 `apollo/config.py` 文件对这些变量进行定制，使用的是**环境变量注入**（`os.getenv()`)的方式。

在实际部署时通过 Shell 脚本（`deploy/run.sh`）注入环境变量。


#### gunicorn 的配置（server的配置）

我们使用 flask 编写的属于 app 应用，若想向外提供服务需要一个 Http Server 的角色，Gunicorn 担任的就是这个角色。

gunicorn 的配置主要通过 `apollo/gunicorn_config.py` 进行注入。建议参考 [gunicorn](https://docs.gunicorn.org/en/stable/) 官方文档详细了解各个配置项。



