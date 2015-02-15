class AbstractSmsTransport(object):
    def __init__(self, *args, **kwargs):
        self.params = kwargs
        print('{0} class created with params {1}'.format(self.__module__, self.params))

    def send(self, phone, msg):
        print('{0} class send method call'.format(self.__module__))
        print('Sent message {1} to phone {0}'.format(phone, msg))