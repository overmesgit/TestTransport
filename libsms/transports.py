from backends.base import BaseSMSTransport

base_transport = BaseSMSTransport()

sms_transport = base_transport['default']
sms_transports = base_transport