Redis pubsub router
~~~~~~~~~~~~~~~~~~~

Blocking subscribe implementation of pyredis is annoying for some case.
It is controllable with some technique, but here is a quick approach using
a python thread.

Note: This implementation is good only for few situation.

Example
-------

    >>> import redis
    >>> redisc = redis.Redis()
    >>> import redispubsub
    >>> pubsub = redispubsub.RedisPubsub(redisc.pubsub())
    >>> pubsub.subscribe('1') # You SHOULD subscribe before starting thread.
    >>> pubsub.start() # Start the router
    >>> pubsub.dequeue('1')
    {'pattern': None, 'type': 'subscribe', 'channel': '1', 'data': 1L}
    >>> redisc.publish('1', 'test')
    >>> pubsub.dequeue('1') # None returned
    >>> pubsub.dequeue('1')
    {'pattern': None, 'type': 'message', 'channel': '1', 'data': 'test'}
    >>> pubsub.dequeue('1') # None returned
