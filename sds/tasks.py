# -*- coding: utf-8 -*-
import os

from celery.utils.log import get_task_logger

from sds import app, celery

logger = get_task_logger(__name__)

@celery.task(bind=True)
def startup_lscs(self,taskid):
    logger.info(('args: {0.args!r}, kwargs: {0.kwargs!r}').format(self.request))
    with app.app_context():
        #cmd = 'echo ' + taskid + ' ' + '>>' + 'd:\\result1.txt 2>&1'
        cmd = '/home/airflow/dags/scripts/STRATEGY-ENGINE/STRATEGY-ENGINE-DEMO.sh' + taskid
        n = os.system(cmd)
        if n != 0:
            logger.error('Executing task id {0.id} error!')
            return 'Failure'

        return 'Finished'

@celery.task(bind=True)
def startup_lsss(self, taskid):
    logger.info(('args: {0.args!r}, kwargs: {0.kwargs!r}').format(self.request))
    with app.app_context():
        #cmd = 'echo ' + taskid + ' ' + '>>' + 'd:\\result2.txt 2>&1'
        cmd = '/home/topcj/lsss/run.sh' + taskid
        n = os.system(cmd)
        if n != 0:
            logger.error('Executing task id {0.id} error!')
            return 'Failure'

        return 'finished'

# @celery.task
# def send_email(msg):
#     with sds.app_context():
#         mail.send(msg)