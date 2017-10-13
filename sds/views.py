# -*- coding: utf-8 -*-

from flask import request, render_template, redirect, url_for, flash
from flask_mail import Message
from . import app
from sds.tasks import send_email

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    address = request.form['address']
    msg = Message('Hello Celery',
                  recipients=[address])
    msg.body = request.form['content']
    send_email.delay(msg)

    flash('Execute taskid: %s' % address)
    return redirect(url_for('index'))