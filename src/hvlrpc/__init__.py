
from .decorators import *
from .endpoint import *

from typing import List, TypeVar, Generic
from hvlrpc import impl
from builtins import iter
from numpy.core._internal import ctypes

_endpoints = []

def endpoints() -> List:
    return _endpoints

class va_list(object):
    """
    Represents a va_list parameter type, supported
    by some backends.
    """
    
    def __init__(self):
        pass
    
    def uint8(self) -> ctypes.c_uint8:
        raise NotImplementedError()
    
    def uint16(self) -> ctypes.c_uint16:
        raise NotImplementedError()
    
    def uint32(self) -> ctypes.c_uint32:
        raise NotImplementedError()

    def uint64(self) -> ctypes.c_uint64:
        raise NotImplementedError()
    
    def str(self) -> str:
        raise NotImplementedError()
    
T = TypeVar('T')
class input(Generic[T]):
    pass

class output(Generic[T]):
    pass

class inout(Generic[T]):
    pass


# Example:
# Simulator registers as an endpoint with all
# APIs 

def register_endpoint(ep : Endpoint):
    _endpoints.append(ep)
    pass

def reset():
    impl.reset()
    _endpoints.clear()
