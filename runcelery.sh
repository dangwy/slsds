#!/bin/bash
LANG=en_US.UTF-8
LANGUAGE=zh_CN.GB18030:zh_CN.GB2312:zh_CN

source /root/.bashrc
. /etc/profile
. ~/.bash_profile

# 常量参数
BASE_HOME=/usr/local/bin/LSDS    						# 脚本主目录
logDir=$BASE_HOME/logs          						# 脚本运行日志目录

celery worker -A sds.tasks.celery -l info -c 50 >> $logDir/runcelery.log