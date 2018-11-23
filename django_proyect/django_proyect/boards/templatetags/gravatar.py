import hashlib
from urllib.parse import urlencode

from django import template
from django.conf import settings

register = template.Library()

@register.filter
def gravatar(user):
    email = user.email.lower().encode('utf-8')
    default = '1b93799d7d6eb08d26b4e4922a2afb13'
    size = 256
    url = 'http://1.gravatar.com/avatar/{md5}?{params}'.format(
        md5 = hashlib.md5(email).hexdigest(),
        params=urlencode({'d':default, 's':str(size) })
    )
    return url