# -*- coding: utf-8 -*-
import time
from sds import app

@app.task
def add(x, y):
    time.sleep(5)     # 模拟耗时操作
    return x + y