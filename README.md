# capitals4py

安装依赖
```shell
pip install poetry
poetry install --without dev
```

启动
```shell
poetry run uvicorn app.main:app --reload
```

测试
```shell
poetry run pytest
```
