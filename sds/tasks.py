# -*- coding: utf-8 -*-
import os
import time
from sds import app, celery

@celery.task(bind=True)
def startup_lscs(self,taskid):
    with app.app_context():
        cmd = 'echo ' + taskid + ' ' + '>>' + 'd:\\result1.txt 2>&1'
        os.system(cmd)
        time.sleep(5)
        # i = 0
        # while i < 100:
        #     i += 1
        #     self.update_state(state = 'PROGRESS', meta = {'i',i})
        #     time.sleep(2)

        return 'finished'

@celery.task
def startup_lsss(taskid):
    with app.app_context():
        cmd = 'echo ' + taskid + ' ' + '>>' + 'd:\\result2.txt 2>&1'
        os.system(cmd)
        time.sleep(5)
        return 'finished'

# @celery.task
# def send_email(msg):
#     with app.app_context():
#         mail.send(msg)