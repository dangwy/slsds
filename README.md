lsds
=====
# 功能说明
- 应用名称：调度系统(lsds)


# 运行方法


# 调用方式
1.调用lsds接口启动lscs任务：
```
http://ip:7878/dispatch/<taskid>
```
2.通过手工分步提交lscs和lsss任务：
```
http://ip:7878/<taskid>
```

# 备注
## 1. Redis command
- 启动redis服务:
```
redis-server
```
- 启动redis client:
```
redis-cli
```
- 创建名为的redisChat频道:
```
SUBSCRIBE redisChat
```

## 2. celery command
- 启动worker
```
celery help
celery worker --help
celery worker -A sds -l info
celery worker -A sds --loglevel=info
celery worker -A sds --loglevel=info --concurrency=5 -指定最大并发数，默认为CPU核数
celery worker -A sds --loglevel=info -P gevent -c 100

celery worker -A sds.tasks.celery -l INFO
celery worker -A sds.tasks.celery -l INFO -c 100 - 开启了100个任务线程
```

# Deploy
1. 要先准备好Nginx+uWSGI的运行环境，然后编写uWSGI的启动文件”myapp.ini”：
```
[uwsgi]
socket=127.0.0.1:3031
callable=app
mount=/myapp=run.py
manage-script-name=true
master=true
processes=4
threads=2
stats=127.0.0.1:9191
virtualenv=/home/bjhee/virtualenv
```

2. 再修改Nginx的配置文件，Linux上默认是”/etc/nginx/sites-enabled/default”，加上目录配置：
```
location /myapp {
    include uwsgi_params;
    uwsgi_param SCRIPT_NAME /myapp;
    uwsgi_pass 127.0.0.1:3031;
}
```
重启Nginx和uWSGI后，就可以通过“http://example1.com/myapp”来访问应用了。

你也可以将我们的应用配置为虚拟服务器，只需要将上述uWSGI的配置移到虚拟服务器的配置文件中即可。

# Todo
服务器：192.168.13.43

LSCS策略引擎计算脚本：
```
/home/airflow/dags/scripts/STRATEGY-ENGINE/STRATEGY-ENGINE-DEMO.sh lt1_9999
```
LSSS统计程序脚本：
```
/home/topcj/lsss/run.sh lt1_9999
```