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

# Todo
1. 添加日志
2. 工程部署
