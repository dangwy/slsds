# -*- coding: utf-8 -*-
import time
from sds import app

@app.task
def multiply(x, y):
    time.sleep(2)
    return x * y