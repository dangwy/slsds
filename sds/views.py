# -*- coding: utf-8 -*-
import time
import datetime
from flask import request, render_template, redirect, url_for, session, flash, jsonify
#from flask_mail import Message
from sds import app
from sds.tasks import startup_lscs, startup_lsss
import pymysql


# 通过浏览器手工提交taskid执行任务
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'GET':
#         return render_template('index.html', task = session.get('task', ''))
#
#     taskid1 = request.form['taskid1']
#     taskid2 = request.form['taskid2']
#     if request.form['submit'] == 'Execute':
#         if taskid1.strip() != '':
#             session['task'] = taskid1
#             startup_lscs.delay(taskid1)
#             flash('Executing lscs, taskid: %s' % taskid1)
#         if taskid2.strip() != '':
#             session['task'] = taskid2
#             startup_lsss.delay(taskid2)
#             flash('Executing lsds, taskid: %s' % taskid2)
#
#     return redirect(url_for('index'))

# 通过浏览器手工提交taskid执行任务
@app.route('/startuplscs', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', task = session.get('task', ''))

    taskid1 = request.form['taskid1']
    # taskid2 = request.form['taskid2']
    if request.form['submit'] == 'Execute':
        if taskid1.strip() != '':
            session['task'] = taskid1
            task = startup_lscs.delay(taskid1)
            # flash('Executing lscs, taskid: %s' % taskid1)
            return jsonify({}), 202, {'Location': url_for('taskstatus', task_id = task.id)}
        # if taskid2.strip() != '':
        #     session['task'] = taskid2
        #     task = startup_lsss.delay(taskid2)
        #     #flash('Executing lsds, taskid: %s' % taskid2)
        #     return jsonify({}), 202, {'Location': url_for('taskstatus', task_id = task.id)}

    #return redirect(url_for('index'))

@app.route('/status/<task_id>')
def taskstatus(task_id):
    task = startup_lscs.AsyncResult(task_id)
    #print("任务：{0} 当前的 state 为：{1}".format(task_id, the_task.state))
    if task.state == 'PENDING':
        resp = {'state': task.state, 'status': 'Pending', 'progress': 0}
    if task.state != 'FAILURE':
        resp = {'state': task.state, 'status':task.info.get('i', 0), 'progress': 1}
        if 'finished' in task.info:
            resp['result'] = task.info['result']
    else:
        resp = {'state': task.state, 'status': str(task.info), 'progress': 100}

    return jsonify(resp)

# 通过接口提交taskid执行LSCS计算任务
@app.route('/dispatch/<taskid>',methods=['GET'])
def startupApp(taskid):
    if request.method == 'GET':
        # 提交执行LSCS
        task1 = startup_lscs.delay(taskid)
        while task1.ready() != True:
            time.sleep(1)
        # 提交执行LSSS
        task2 = startup_lsss.delay(taskid)
        while task2.ready() != True:
            time.sleep(1)
        # 更新任务的运行状态，0表示未提交回测任务，1表示任务已成功，2表示运行中，3表示运行失败，4任务提交中
        #DATABASE_URI = 'pymysql+mysql://model:modelK$j$d1KDG@192.168.13.44/model'
        conn = pymysql.connect(host = '192.168.13.44', port=3306, user = 'model', passwd='modelK$j$d1KDG',db='model')

        dtime = datetime.datetime.now()
        ans_time = time.mktime(dtime.timetuple())
        try:
            with conn.cursor() as cursor:
                sql = "UPDATE Strategy_Task SET Status = %s, EndTime = %s WHERE TaskID = '%s'" % (1, ans_time, taskid)
                cursor.execute(sql)
                conn.commit()
        finally:
            conn.close()

        response = {
            'code': 8200,
            'msg': '',
            'task_id': task1.id,
            'TaskID':taskid
        }
        return jsonify(response)
