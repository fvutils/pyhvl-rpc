'''
Created on Mar 14, 2021

@author: mballance
'''
import ctypes

class Unpacker(object):
    
    def __init__(self):
        pass
    
    def unpack_int8(self) -> ctypes.c_int8:
        raise NotImplementedError("Class " + str(self) + " doesn't implement unpack_int8")
    
    def unpack_int16(self) -> ctypes.c_int16:
        raise NotImplementedError("Class " + str(self) + " doesn't implement unpack_int16")
    
    def unpack_int32(self) -> ctypes.c_int32:
        raise NotImplementedError("Class " + str(self) + " doesn't implement unpack_int32")
    
    def unpack_int64(self) -> ctypes.c_int64:
        raise NotImplementedError("Class " + str(self) + " doesn't implement unpack_int32")
    
    def unpack_uint8(self) -> ctypes.c_uint8:
        raise NotImplementedError("Class " + str(self) + " doesn't implement unpack_uint8")
    
    def unpack_uint16(self) -> ctypes.c_uint16:
        raise NotImplementedError("Class " + str(self) + " doesn't implement unpack_uint16")
    
    def unpack_uint32(self) -> ctypes.c_int32:
        raise NotImplementedError("Class " + str(self) + " doesn't implement unpack_uint32")
    
    def unpack_uint64(self) -> ctypes.c_int64:
        raise NotImplementedError("Class " + str(self) + " doesn't implement unpack_uint32")

    def unpack_str(self) -> str:
        raise NotImplementedError("Class " + str(self) + " doesn't implement unpack_str")

    def unpack_struct(self, t):
        """Unpacks a struct using the unpacker provided by the struct type"""
        raise NotImplementedError("Class " + str(self) + " doesn't implement unpack_struct")
    
    def unpack_vargs(self) -> 'Unpacker':
        """Unpacks variadic arguments, which must be last"""
        raise NotImplementedError("Class " + str(self) + " doesn't implement unpack_vargs")
