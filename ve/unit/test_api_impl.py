'''
Created on Feb 4, 2021

@author: mballance
'''
import hvlrpc
from unittest.case import TestCase
from hvlrpc.endpoint import Endpoint

class TestApiImpl(TestCase):
    
    def test_smoke(self):
        
        @hvlrpc.api
        class my_api_t(object):
            
            @hvlrpc.exp_func
            def vprintf(self,
                        fmt : str,
                        ap : hvlrpc.va_list):
                pass
            
        class my_api_impl(my_api_t):
            
            def vprintf(self, fmt, ap):
                print("vprintf")
                
        e = Endpoint("abc", None)
       
        impl = my_api_impl()
        e.set_api_impl(impl)

        
        