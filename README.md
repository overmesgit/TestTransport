# TestTransport

**Requirement:**

python2.7

**Install:**

pip install django

**Test:**

python manage.py test

python manage.py shell


from libsms import sms_transport

from libsms import sms_transports

sms_transport.send(phone=’123123’, msg=’qweqwe’)

sms_transports[‘dummy’].send(phone=’123123’, msg=’qweqwe’)
