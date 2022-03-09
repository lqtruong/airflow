import sys
from datetime import datetime

if __name__ == '__main__':
    eventValue = []
    payload = {
        "eventName": "af_first_deposit",
        "eventValue": eventValue
    }
    for i in range(100):
        eventValue.append({'id': i, 'r': 'a'})
        # payload[str(i)] = i
    payload['kkk_id'] = '123'
    payload['customer_user_id'] = '2fsds'
    payload['eventTime'] = datetime.now()
    payload['os'] = '1'

    print('payload', payload)
    print('size of', 'payload:', str(sys.getsizeof(payload)), 'bytes')
    print('size of', 'payload:', str(sys.getsizeof(payload) / 1024), 'kbytes')
