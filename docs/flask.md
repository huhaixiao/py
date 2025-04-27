## setup

```shell
python3 --version
python3 -m pip install flask flask-socketio -i https://mirrors.aliyun.com/pypi/simple/ --user
python3 app.py
```

## Setup Poetry

```shell
curl -sSL https://install.python-poetry.org | python3 -
```

- Add `export PATH="/Users/haixhu/.local/bin:$PATH"` to `~/.zshrc`

## Poetry usage

```shell
poetry init
poetry add flask flask-socketio
poetry run python3 app.py
poetry install
poetry env info
poetry env use python3
```

## Structure

```text
flask_project/
├── app/
│   ├── __init__.py          # 初始化 Flask 应用
│   ├── routes.py            # 定义路由和视图函数
│   ├── models.py            # 定义数据库模型
│   ├── forms.py             # 定义表单（如果使用 Flask-WTF）
│   ├── static/              # 静态文件（CSS、JS、图片等）
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   ├── templates/           # HTML 模板文件
│   │   ├── base.html        # 基础模板
│   │   └── index.html       # 主页模板
│   └── socketio_events.py   # 定义 Socket.IO 事件
├── migrations/              # 数据库迁移文件夹（由 Flask-Migrate 创建）
├── tests/                   # 单元测试文件夹
│   ├── __init__.py
│   └── test_app.py
├── config.py                # 配置文件
├── app.py                   # 应用入口文件
├── requirements.txt         # 项目依赖列表
├── pyproject.toml           # 如果使用 Poetry 管理依赖
└── README.md                # 项目说明文档
```

## Glossary

- `requirements.txt`
- `pyproject.toml`
