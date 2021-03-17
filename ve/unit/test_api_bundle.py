'''
Created on Mar 13, 2021

@author: mballance
'''
from unittest.case import TestCase
import hvlrpc

class TestApiBundle(TestCase):
    
    def test_smoke(self):
        
        @hvlrpc.api_imp
        class my_imp(object):
            
            @hvlrpc.task
            def call_out(self):
                pass
            
        @hvlrpc.api_exp
        class my_exp(object):
            
            @hvlrpc.task
            async def call_in(self):
                pass
            
        @hvlrpc.api_bundle
        class my_bundle(object):
            ext1 : my_imp
            ext2 : my_exp
            
            # Automation provides a 'create' class method
            # that accepts an implementation of 'my_imp'
            # 'create' also optionally accepts the endpoint
            # to use in creating an instance of this API

