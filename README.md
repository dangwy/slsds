# 功能说明
- 应用名称：调度系统(lsds)


# 运行方法
- 启动worker:
```
celery help
celery worker --help
celery worker -A sds -l info
celery worker -A sds --loglevel=info
celery worker -A sds --loglevel=info --concurrency=5 -指定最大并发数，默认为CPU核数
celery worker -A sds --loglevel=info -P gevent -c 100
```

# 备注
## Redis command
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

##

# Todo