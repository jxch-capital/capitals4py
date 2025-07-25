# capitals4py

安装依赖
```shell
pip install poetry
poetry install --without dev
```

启动
```shell
poetry run uvicorn capitals4py.main:app --reload --host 127.0.0.1 --port 8080
```

测试
```shell
poetry run pytest
```

导出项目依赖
```shell
poetry self add poetry-plugin-export
poetry export -f requirements.txt --output requirements.txt --without-hashes
```
