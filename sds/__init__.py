# -*- coding: utf-8 -*-
from flask import Flask
from flask_mail import Mail
from celery import Celery
import config

app = Flask(__name__)
app.config.from_object('config')

mail = Mail(app)

celery = Celery(app.name)
celery.config_from_object('celeryconfig')

from . import views