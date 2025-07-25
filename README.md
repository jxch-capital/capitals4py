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

编译
```shell
pip install nuitka
nuitka --standalone --onefile --jobs=4 --lto=yes capitals4py/main.py -o capitals4py.bin
```
注意
1. 编译后的二进制文件不能使用 `strip` 命令进行瘦身，因为它会破环数据结构导致启动报错：`Error, couldn't find attached data header.`
2. nuitka编译时不能使用多个虚拟环境（比如同时使用conda和poetry），否则会产生元数据混乱的问题，可以导出依赖文件都装进conda中再编译。

导出项目依赖
```shell
poetry self add poetry-plugin-export
poetry export -f requirements.txt --output requirements.txt --without-hashes
```
