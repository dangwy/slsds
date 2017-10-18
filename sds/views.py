# -*- coding: utf-8 -*-

from flask import request, render_template, redirect, url_for, flash,jsonify
#from flask_mail import Message
from . import app
from sds.tasks import setup_lscs

# 通过浏览器手工提交taskid执行任务
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    taskid = request.form['taskid']

    if request.form['submit'] == 'Execute':
        setup_lscs.delay(taskid)
        flash('Execute taskid: %s' % taskid)

    return redirect(url_for('index'))

# 通过接口提交taskid执行任务
@app.route('/<taskid>',methods=['GET'])
def setupLSCS(taskid):
    if request.method == 'GET':
        setup_lscs.delay(taskid)
        response = {
            'taskid': taskid
        }

        return jsonify(response)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'GET':
#         return render_template('index.html')
#
#     address = request.form['address']
#     msg = Message('Hello Celery', recipients=[address])
#     msg.body = request.form['content']
#     send_email.delay(msg)
#
#     flash('Sending email to %s' % address)
#     return redirect(url_for('index'))