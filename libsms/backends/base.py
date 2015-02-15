from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.module_loading import import_string


class BaseSMSTransport(object):
    def __getitem__(self, key):
        return self.transports[key]

    def __init__(self, *args, **kwargs):
        self.transports = {}
        if self.valid_settings():
            self.load_transports()
        else:
            raise ImproperlyConfigured

    def load_transports(self):
        for transport_name, data in settings.SMS_TRANSPORTS.items():
            transport_class = import_string(data['BACKEND'])
            self.transports[transport_name] = transport_class(**data.get('PARAMS', {}))

    def valid_settings(self):
        return hasattr(settings, 'SMS_TRANSPORTS') and settings.SMS_TRANSPORTS.get('default')