# 文档

* [api文档](./api)
* [部署配置](../deploy)

## 简介

记录设计原则、约定等内容。

更多内容请参考 [bass（贝斯）](https://github.com/wheresmile/bass) 项目。

### 本项目目录结构

* apollo：主要包含 flask 的构建、配置，以及 gunicorn 的配置
* controllers： **控制器文件目录（通过修饰器的方式进行路由注册，MVC中的C层）**
* deploy：线上实际部署时使用的相关文件
* docs：文档目录
* migrations：alembic 配置文件、数据库初始化配置
* migrations/versions：数据库迁移文件
* models：**数据库模型定义，CURD相关的逻辑（MVC中的M层）**
* requirements：依赖库文件
* scheduler：定时任务
* tests：测试用例文件夹
* utils：一些基础方法集，比如时间、字符串相关


