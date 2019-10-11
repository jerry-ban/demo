from nlopt_examples import nlopt_examples

import logging
import time
from logging.handlers import RotatingFileHandler

def create_rotating_log(path):
    """
    Creates a rotating log
    """
    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.INFO)

    # add a rotating handler
    handler = RotatingFileHandler(path, maxBytes=5*1024,backupCount=5)
    logger.addHandler(handler)

    for i in range(10000):
        logger.info("This is test log line %s" % i)
        #time.sleep(1.5)


def test_logging():
    log_file = "test.log"
    create_rotating_log(log_file)

def test_run():
    a = nlopt_examples()
    result = a.run_offcial_example()

test_logging()
#test_run()