# 服务器端

```
├── README.md
├── api # 接口
│   ├── __init__.py
│   └── v1.py
├── config
│   ├── gconfig.py # 全局配置
│   └── gunicorn_cnf.py # gunicorn配置
├── core # 通用组件
├── log
├── main.py # 主入口
├── pages # 前端页面逻辑
├── requirements.txt
├── static # 静态文件
├── templates # html模版
└── utils # 工具
```

## 部署

1.  `在src/server`目录下
1.  `gunicorn -c config/gunicorn_cnf.py main:app`
