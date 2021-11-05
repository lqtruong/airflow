import logging

FORMAT = '%(asctime)-15s %(levelname)s [%(processName)s] [%(threadName)s] %(message)s'
logging.getLogger().setLevel('INFO')
logging.basicConfig(format=FORMAT)
logging.info('log INFO')
logging.debug('log DEBUG')
