from libsms.backends.abstract import AbstractSmsTransport


class SmsTransport(AbstractSmsTransport):
    def __init__(self, *args, **kwargs):
        super(SmsTransport, self).__init__(*args, **kwargs)

    def send(self, phone, msg):
        super(SmsTransport, self).send(phone, msg)