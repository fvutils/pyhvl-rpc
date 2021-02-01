'''
Created on Jan 31, 2021

@author: mballance
'''
import hvlrpc
from unittest.case import TestCase
import ctypes

class TestApiDef(TestCase):
    
    def test_static_api(self):
        
        @hvlrpc.api
        class my_api(object):
            
            @hvlrpc.imp_func
            def my_func(self, 
                        a : ctypes.c_uint64,
                        b : ctypes.c_uint32) -> ctypes.c_uint32:
                pass
            
    def test_missing_ptype(self):
        try:        
            @hvlrpc.api
            class my_api(object):
            
                @hvlrpc.imp_func
                def my_func(self, 
                        a : ctypes.c_uint64,
                        b) -> ctypes.c_uint32:
                    pass
            self.fail("Failed to detect missing param type")
        except Exception as e:
            self.assertTrue("Type for parameter b unspecified" in str(e))

    def test_task_return(self):
        try:        
            @hvlrpc.api
            class my_api(object):
            
                @hvlrpc.imp_task
                def my_task(self, 
                        a : ctypes.c_uint64) -> ctypes.c_uint32:
                    pass
            self.fail("Failed to detect missing param type")
        except Exception as e:
            self.assertTrue("Cannot specify a return type for a task" in str(e))
                    
            
        
        