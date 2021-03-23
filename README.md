<center>
    <h2>
        FLASK-API 项目结构搭建
    </h2>
</center>


### FLASK-API 项目结构

- `flask-restful`：api
- `flask-script`：命令
- `flask-sqlalchemy`：数据库

### 快速开始

- 配置 venv
```
python3 -m venv ./venv
```

- 安装需求文件 `requirements.txt`

```
pip install -r requirements.txt
```

- 初始化数据库命令

```
python manager.py initdb
```

- 运行 `run.py`
```
export FLASK_ENV=development
python manager.py runserver
```