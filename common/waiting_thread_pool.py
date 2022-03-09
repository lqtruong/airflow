import logging
import time
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED
from pprint import pprint

import requests

headers = {
    'Content-Type': 'application/json'
}

thread_pool_configs = {
    "max_workers": 10,
    "thread_name_prefix": "io_poll",
}

FORMAT = '%(asctime)-15s %(levelname)s [%(processName)s] [%(threadName)s] %(message)s'
logging.getLogger().setLevel('DEBUG')
logging.basicConfig(format=FORMAT)
logging.debug('Start thread pool: %s', 'connection reset', extra=thread_pool_configs)

URL = "http://localhost:8080/api/randomize"

MAX_IN_QUEUE = 1_000
futures = []
executor = ThreadPoolExecutor(
    max_workers=thread_pool_configs['max_workers'],
    thread_name_prefix=thread_pool_configs['thread_name_prefix']
)


def get_randomize(url, timeout=10):
    res = requests.get(url, headers=headers, timeout=timeout)
    logging.debug("res: %s %s", res.status_code, res.text)


def submit_request_to_queue():
    futures.append(executor.submit(get_randomize, url=URL))
    logging.info("futures size %s", len(futures))
    if len(futures) > MAX_IN_QUEUE:
        wait(futures, timeout=None, return_when=ALL_COMPLETED)
        futures[:] = []
        logging.info("futures size after clear %s", len(futures))


start = time.time()

pprint(vars(executor))

futures = []
for i in range(6_000):
    logging.info("index %s", i)
    submit_request_to_queue()
end = time.time()
logging.info("Total waiting times cost %s", end - start)

endAll = time.time()
logging.info("Total execution time: %s", endAll - start)
