# -*- coding: utf-8 -*-
# from flask_mail import Mail
from celery import Celery
from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

celery = Celery(app.name)
celery.config_from_object('celeryconfig')

from . import views

