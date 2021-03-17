'''
Created on Jan 30, 2021

@author: mballance
'''
from hvlrpc.impl.ctor import Ctor
from hvlrpc.impl.method_wrapper import MethodWrapper

def api_bundle(T):
    
    Ctor.inst().add_bundle(T)
    
    return T

def api_imp(T):
    """
    Identifies an imported API -- one that Python will call
    """
    Ctor.inst().add_api(T, True)
    return T

def api_exp(T):
    """
    Identifies an exported API -- one that will call Python
    """
    Ctor.inst().add_api(T, False)
    return T

def struct(T):
    """
    Identifies a pure-data class that may be passed to the API
    """
    return T

def func(T):
    Ctor.inst().add_method(T, False)
    return T

def task(T):
    Ctor.inst().add_method(T, True)
    return T

