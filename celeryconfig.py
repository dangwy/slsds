# -*- coding: utf-8 -*-
BROKER_URL = 'redis://127.0.0.1:6379'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'
CELERY_TIMEZONE='Asia/Shanghai'                     # 指定时区，默认是 UTC
# CELERY_TIMEZONE='UTC'
CELERY_IMPORTS = (                                  # 指定导入的任务模块
    'sds.tasks',
)


# CELERY_TASK_SERIALIZER='pickle'
CELERY_TASK_RESULT_EXPIRES=3600