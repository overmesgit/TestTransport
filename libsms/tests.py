from django.conf import settings
from django.test import TestCase


class SMSTest(TestCase):

    def test_sms(self):
        from libsms.transports import sms_transport
        from libsms.transports import sms_transports

        sms_transport.send('123', 'hello')

        for transport_name in settings.SMS_TRANSPORTS:
            sms_transports[transport_name].send('123', 'hello')
