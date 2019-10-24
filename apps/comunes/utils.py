# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import threading

_thread_locals = threading.local()


def set_current_user(user):
    _thread_locals.user=user


def get_current_user():
    # return getattr(_thread_locals, 'user', None)
    import pdb; pdb.set_trace()
    return getattr(_thread_locals, 'user', None)


def remove_current_user():
    _thread_locals.user = None
