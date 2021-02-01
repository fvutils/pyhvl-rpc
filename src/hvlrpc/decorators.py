'''
Created on Jan 30, 2021

@author: mballance
'''
from hvlrpc.impl.ctor import Ctor

def api(T):
    """
    Identifies a static API (non-object)
    """
    Ctor.inst().add_api(T, False)

def obj(T):
    """
    Identifies an object API
    """
    Ctor.inst().add_api(T, False)

def struct(T):
    """
    Identifies a pure-data class that may be passed to the API
    """
    pass

def imp_func(T):
    Ctor.inst().add_method(T, True, False)

def imp_task(T):
    Ctor.inst().add_method(T, True, True)

def exp_func(T):
    Ctor.inst().add_method(T, False, False)

def exp_task(T):
    Ctor.inst().add_method(T, False, True)

