import time

from config.config import Config


def wait_conditions(predicate, timeout=None, period=0.25, *args, **kwargs):
    if not timeout:
        timeout = Config['explicit_wait_polling']

    end_time = time.time() + timeout
    while time.time() < end_time:
        if predicate(*args, **kwargs):
            return True
        time.sleep(period)
    return False
