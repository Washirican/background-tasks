import os

import redis
from rq import Worker, Queue, Connection

listen = ['high', 'default', 'low']

redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
conn = redis.from_url(redis_url)
<<<<<<< HEAD

# conn = redis.Redis('localhost', 6379, 0)
=======
>>>>>>> e5ac0772f2188b7f024c4b2a81b24fba68417aa3

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()
