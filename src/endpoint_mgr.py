'''
Created on Mar 16, 2021

@author: mballance
'''
from hvlrpc.endpoint import Endpoint

class EndpointMgr(object):
    
    _inst = None
    
    def __init__(self):
        self.endpoints = []
        
    async def init(self):
        for e in self.endpoints:
            await e.init()
        
    def add_endpoint(self, ep : Endpoint):
        self.endpoints.append(ep)
        
    def find_implementing_endpoints(self, api_t):
        ret = []
        for e in self.endpoints:
            if e.get_api_impl(api_t) is not None:
                ret.append(e)
        return ret
    
    @classmethod
    def inst(cls):
        if cls._inst is None:
            cls._inst = EndpointMgr()
        return cls._inst
    
    @classmethod
    def test_init(cls):
        cls._inst = None