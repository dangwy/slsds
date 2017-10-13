import time
from notify_friends import notify_friends

def notify(userId, messageId):
    result = notify_friends.delay(userId, messageId)
    while not result.ready():
        time.sleep(1)
        print(result.get(timeout=1))

if __name__ == '__main__':
    notify('001', '001')
