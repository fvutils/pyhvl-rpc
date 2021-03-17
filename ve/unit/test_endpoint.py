'''
Created on Mar 15, 2021

@author: mballance
'''

import hvlrpc
import ctypes
from hvlrpc.endpoint import Endpoint
from unittest.case import TestCase
from endpoint_mgr import EndpointMgr
from hvlrpc.packing_api_impl import PackingApiImpl

class TestEndpoint(TestCase):
    
    def test_call_import(self):
        
        @hvlrpc.api_imp
        class api_c(object):

            # Can probably come up with an introspection approach           
            @hvlrpc.func
            def my_f1(self, a : ctypes.c_uint32):
                pass
            
        class my_api(api_c):
            def __init__(self):
                self.val = 0
                
            def my_f1(self, a):
                self.val = a
                

        ep = Endpoint()
        EndpointMgr.inst().add_endpoint(ep)
        impl = my_api()
        ep.set_api_impl(api_c, impl)
        
        api_c.inst().my_f1(2)
        
        self.assertEqual(impl.val, 2)
        
    def test_packer_impl(self):
        
        @hvlrpc.api_imp
        class api_c(object):

            # Can probably come up with an introspection approach           
            @hvlrpc.func
            def my_f1(self, a : ctypes.c_uint32):
                pass

        impl = PackingApiImpl.create(api_c)
        impl.my_f1(4)


        