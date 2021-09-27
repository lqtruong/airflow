import logging
import time
from concurrent.futures import ThreadPoolExecutor
from pprint import pprint

import requests

headers = {
    'Content-Type': 'application/json'
}

thread_pool_configs = {
    "max_workers": 200,
    "thread_name_prefix": "io_poll",
}

FORMAT = '%(asctime)-15s %(levelname)s [%(processName)s] [%(threadName)s] %(message)s'
logging.getLogger().setLevel('DEBUG')
logging.basicConfig(format=FORMAT)
logging.debug('Start thread pool: %s', 'connection reset', extra=thread_pool_configs)

URL = "http://localhost:8080/api/randomize"


def get_randomize(url, timeout=10):
    res = requests.get(url, headers=headers, timeout=timeout)
    logging.debug("res: %s %s", res.status_code, res.text)


start = time.time()

with ThreadPoolExecutor(max_workers=thread_pool_configs['max_workers'],
                        thread_name_prefix=thread_pool_configs['thread_name_prefix']) as executor:
    pprint(vars(executor))
    for i in range(60):
        executor.submit(get_randomize, url=URL)

end = time.time()
logging.info("Total execution time: %s", end - start)
