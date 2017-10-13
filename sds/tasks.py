# -*- coding: utf-8 -*-
from . import app, mail, celery

@celery.task
def send_email(msg):
    with app.app_context():
        mail.send(msg)