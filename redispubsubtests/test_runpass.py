
import time
import redis
from redispubsub import RedisPubsub

def test_runpass():
    redisc = redis.Redis()
    pubsub = RedisPubsub(redisc.pubsub())
    pubsub.subscribe('1')
    pubsub.start()
    redisc.publish('1', 'test')
    time.sleep(0.1)
    msg = pubsub.dequeue('1')
    assert msg['type'] == 'subscribe'
    msg = pubsub.dequeue('1')
    assert msg['data'] == 'test'

    pubsub.subscribe('2')
    time.sleep(0.1)
    msg = pubsub.dequeue('2')
    assert msg['type'] == 'subscribe'

    redisc.publish('1', 'msg1')
    redisc.publish('2', 'msg2')
    time.sleep(0.1)

    msg = pubsub.dequeue('1')
    assert msg['data'] == 'msg1'
    msg = pubsub.dequeue('2')
    assert msg['data'] == 'msg2'

if __name__ == '__main__':
    test_runpass()