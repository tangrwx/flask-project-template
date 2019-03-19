# README

Flask 框架的项目模板

```
.
├── Pipfile
├── Pipfile.lock
├── README.md
├── config.py
├── project
│   ├── __init__.py
│   ├── ext.py
│   ├── models.py
│   └── views.py
└── wsgi.py

1 directory, 9 files
```

1. 项目目录

   - `__init__.py`：初始化 flask
   - `ext.py`：第三方扩展，不依赖项目的其他文件
   - `models.py`：数据库表的定义
   - `views.py`：路由与视图

2. 配置文件

   - `config.py`： 定义默认配置和非敏感的信息；
   - `config_local.py`：定义敏感信息，默认不上传到代码库；

3. 启动文件

   `gunicorn -w 4 -b 127.0.0.1:9090 --access-logfile wsgi.log wsgi:app -D`
