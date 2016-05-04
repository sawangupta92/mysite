from __future__ import absolute_import
# from config import huey # import the huey we instantiated in config.py
# import redis
# from appflux.huey.appflux_exception import AppfluxException

# r = redis.Redis()
# client = AppfluxException(r, 'huey')
# client.start()

# @huey.task()
# def count_beans(num):
#     print '-- counted %s beans --' % nm



from celery import shared_task

from appflux.celery.appflux_exception import AppfluxException
AppfluxException()
@shared_task
def add(x, y):
    print '111111111111111111111111111111111111111111111'
    return x + ys


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)
