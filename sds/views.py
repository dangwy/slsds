# -*- coding: utf-8 -*-
import datetime
import time

import pymysql
from flask import request, render_template, url_for, session, jsonify,flash,redirect

# from flask_mail import Message
from sds import app
from sds.tasks import startup_lscs, startup_lsss

def updateStatus(status, taskid):
    conn = pymysql.connect(host='192.168.13.44', port=3306, user='model', passwd='modelK$j$d1KDG', db='model')

    dtime = datetime.datetime.now()
    ans_time = time.mktime(dtime.timetuple())
    try:
        with conn.cursor() as cursor:
            sql = "UPDATE Strategy_Task SET Status = %s, EndTime = %s WHERE TaskID = '%s'" % (status, ans_time, taskid)
            cursor.execute(sql)
    finally:
        conn.commit()
        conn.close()

    return

# 通过浏览器手工提交taskid执行任务
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', task = session.get('task', ''))

    taskid1 = request.form['taskid1']
    taskid2 = request.form['taskid2']

    if request.form['submit'] == 'Execute':
        if taskid1.strip() != '':
            session['task'] = taskid1
            t1 = startup_lscs.delay(taskid1)
            flash('Executing LSCS, Task_ID: %s' % taskid1)
            while not t1.ready():
                if t1.get() != 'Finished':
                    updateStatus(3, taskid1)
                    flash('Excuting LSCS failed, Task_id: %s' % taskid1)
                else:
                    updateStatus(1, taskid1)
                    flash('Excuting LSCS sucess, Task_id: %s' % taskid1)

        if taskid2.strip() != '':
            session['task'] = taskid2
            t2 = startup_lsss.delay(taskid2)
            flash('Executing LSSS, Task_ID: %s' % taskid2)
            while not t2.ready():
                if t2.get() != 'Finished':
                    updateStatus(3,taskid2)
                    flash('Excuting LSCS failed, Task_id: %s' % taskid2)
                else:
                    updateStatus(1, taskid2)
                    flash('Excuting LSSS finished, Task_id: %s' % taskid2)

    return redirect(url_for('index'))

# 通过接口提交taskid执行LSCS计算任务
@app.route('/dispatch/<taskid>',methods=['GET'])
def startupApp(taskid):
    if request.method == 'GET':
        t1 = t2 = 0
        # 任务的运行状态，0表示未提交回测任务，1表示任务已成功，2表示运行中，3表示运行失败，4任务提交中
        t_status = 3

        # 提交执行LSCS
        task1 = startup_lscs.delay(taskid)
        while not task1.ready():
            if task1.get() != 'Finished':
                updateStatus(t_status, taskid)
                return 'Execute startup LSCS error ' + taskid
            t1 = 1

        # 提交执行LSSS
        if (t1 == 1):
            task2 = startup_lsss.delay(taskid)
            while not task2.ready():
                if task2.get() != 'Finished':
                    updateStatus(t_status, taskid)
                    return 'Execute startup LSSS error ' + taskid
                t2 = 1

        # 更新任务的运行状态为成功
        if (t1 == 1) and (t2 == 1):
            t_status = 1
            updateStatus(t_status, taskid)

        response = {
            'code': 8200,
            'msg': '',
            'task_id': task1.id,
            'TaskID': taskid
        }
        return jsonify(response)
