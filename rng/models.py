from django.db import models
from djangae import fields

import random
import functools

_RINT = functools.partial(random.SystemRandom().randint, 0)
_PRIME = 2 ** 127 - 1

class UsedNumber(models.Model):
    number = fields.CharField()

    def __str__(self):
        return self.number

    @classmethod
    def new(cls):
        r = str(_RINT(_PRIME))
        x, c = cls.objects.get_or_create(
            number = r,
            defaults = {
                'number': r
            },
        )
        if c:
            x.save()
        return x
