# capitals4py

安装依赖
```shell
pip install poetry
poetry install --without dev
```

启动
```shell
poetry run uvicorn capitals4py.main:capitals4py --reload --host 0.0.0.0 --port 8080
```

测试
```shell
poetry run pytest
```
