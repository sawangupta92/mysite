from config import huey # import the huey we instantiated in config.py
import redis
from appflux.huey.appflux_exception import AppfluxException

r = redis.Redis()
client = AppfluxException(r, 'huey')
client.start()

@huey.task()
def count_beans(num):
    print '-- counted %s beans --' % nm
