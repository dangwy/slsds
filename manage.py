# -*- coding: utf-8 -*-
# from __future__ import absolute_import
# from flask-script import Manager
# from flask_celery import install_commands as install_celery_commands
#
# from myapp import create_app
#
# app = create_app()
# manager = Manager(app)
# install_celery_commands(manager)
#
# if __name__ == "__main__":
#     manager.run()


# -*- coding:utf-8 -*-
# __author__ = 'good'
# __create__ = '2014-11-13'
# from golsee.appcreators import createapp
# from flask_script import Manager
# from flask.ext.migrate import MigrateCommand
# from golsee.manager_script.LogManager import LogManager
# from golsee.manager_script.InitManager import InitManager
# from golsee.manager_script.BackupManager import BackupManager
# from golsee.manager_script.server_info import ServerInfoManager
#
# manager = Manager(createapp())
# manager.add_command('migrate', MigrateCommand)
# manager.add_command('log', LogManager)
# manager.add_command('init', InitManager)
# manager.add_command('backup', BackupManager)
# manager.add_command('monitor', ServerInfoManager)
#
# if __name__ == '__main__':
#     manager.run()