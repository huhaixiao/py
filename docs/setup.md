```shell
brew install python3

# first venv: 调用python 的venv 模块
# second venv: 指定虚拟环境的目录名称
python3 -m venv venv

# 激活虚拟环境
# 隔离项目依赖
# 避免与全局Python 包冲突
source venv/bin/activate

pip --version
```
