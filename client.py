# -*- coding: utf-8 -*-
from sds import task_lscs
from sds import task_lsss

# task_lscs.add.apply_async(args=[2, 8])        # 也可用 task1.add.delay(2, 8)
# task_lsss.multiply.apply_async(args=[3, 7])   # 也可用 task2.multiply.delay(3, 7)
task_lscs.add.delay(2, 8)
task_lsss.multiply.delay(3, 7)
print('hello world')


# def notify(userId, messageId):
#     result = notify_friends.delay(userId, messageId)
#     while not result.ready():
#         time.sleep(1)
#         print(result.get(timeout=1))
#
# if __name__ == '__main__':
#     notify('001', '001')
