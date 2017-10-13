from celery import Celery
import time

broker = 'redis://127.0.0.1:6379'
backend = 'redis://127.0.0.1:6379/0'

app = Celery('notify_friends', backend = backend, broker = broker)

@app.task
def notify_friends(userId, newsId):
    print('Start to notify_friends task at {0}, userID:{1} newsID:{2}'.format(time.ctime(), userId, newsId))
    time.sleep(2)
    print('Task notify_friends succeed at {0}'.format(time.ctime()))
    return True