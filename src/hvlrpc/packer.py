'''
Created on Mar 14, 2021

@author: mballance
'''
import ctypes

class Packer(object):
    """Used to pack arguments for method calls"""
    
    def __init__(self):
        pass

    def pack_int8(self, v : ctypes.c_int8):
        raise NotImplementedError("Class " + str(self) + " doesn't implement pack_int8")
    
    def pack_int16(self, v : ctypes.c_int16):
        raise NotImplementedError("Class " + str(self) + " doesn't implement pack_int16")
    
    def pack_int32(self, v : ctypes.c_int32):
        raise NotImplementedError("Class " + str(self) + " doesn't implement pack_int32")
    
    def pack_int64(self, v : ctypes.c_int64):
        raise NotImplementedError("Class " + str(self) + " doesn't implement pack_int32")
    
    def pack_uint8(self, v : ctypes.c_uint8):
        raise NotImplementedError("Class " + str(self) + " doesn't implement pack_uint8")
    
    def pack_uint16(self, v : ctypes.c_uint16):
        raise NotImplementedError("Class " + str(self) + " doesn't implement pack_uint16")
    
    def pack_uint32(self, v : ctypes.c_int32):
        raise NotImplementedError("Class " + str(self) + " doesn't implement pack_uint32")
    
    def pack_uint64(self, v : ctypes.c_int64):
        raise NotImplementedError("Class " + str(self) + " doesn't implement pack_uint32")

    def pack_str(self, v : str):
        raise NotImplementedError("Class " + str(self) + " doesn't implement pack_str")

    def pack_struct(self, v):
        """Packs a struct using the packer provided by the struct object"""
        raise NotImplementedError("Class " + str(self) + " doesn't implement pack_struct")

    # TODO: should have some support
#    def pack_vargs(self):
    