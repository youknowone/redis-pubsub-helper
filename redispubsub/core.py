
import threading

class RedisPubsub(threading.Thread):
    def __init__(self, pubsub, start=True):
        self.pubsub = pubsub
        self.received = {}

        threading.Thread.__init__(self)

        self.daemon = True
        self.stop = False

    def subscribe(self, channel):
        self.received[channel] = []
        self.pubsub.subscribe(channel)

    def unsubscribe(self, channel):
        self.pubsub.unsubscribe(channel)
        del(self.received[channel])

    def enqueue(self, channel, message):
        self.received[channel].append(message)

    def dequeue(self, channel):
        try:
            return self.received[channel].pop(0)
        except IndexError:
            return None

    def run(self):
        listen = self.pubsub.listen()
        while True:
            message = listen.next()
            print 'msg:', message
            self.enqueue(message['channel'], message)
            if self.stop:
                break

    def stop(self):
        self.stop = True

