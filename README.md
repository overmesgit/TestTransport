# TestTransport

## **Requirements:**

python2.7

## **Install:**

pip install django

add options in settings:

```python
SMS_TRANSPORTS = {
    'default': {
        'BACKEND': 'libsms.backends.sms.SmsTransport',
        'PARAMS': {
            'login': 'some_login',
            'password': 'some_password',
        }
    },
    'dummy': {
        'BACKEND': 'libsms.backends.dummy.SmsTransport',
    },
    'other': {
        'BACKEND': 'libsms.backends.other.SmsTransport',
        'PARAMS': {
            'login': 'some_login',
            'password': 'some_password',
            'var1': 'var1',
            'var2': 'var2',
        }
    }
}```

Where default, dummy, other some backend names

**default option is required**

BACKEND - path to transport module
PARAMS - options for transport constructor

## **Test:**

python manage.py test

python manage.py shell


`from libsms import sms_transport`

`from libsms import sms_transports`

`sms_transport.send(phone=’123123’, msg=’qweqwe’)`

`sms_transports[‘dummy’].send(phone=’123123’, msg=’qweqwe’)`
