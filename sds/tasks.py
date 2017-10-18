# -*- coding: utf-8 -*-
import os
# import time
from . import app, celery

@celery.task
def setup_lscs(taskid):
    with app.app_context():
        cmd = 'echo ' + taskid + ' ' + '>>' + 'd:\\result.txt 2>&1'
        os.system(cmd)

        return taskid

# @celery.task
# def send_email(msg):
#     with app.app_context():
#         mail.send(msg)