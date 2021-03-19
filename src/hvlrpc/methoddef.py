'''
Created on Jan 31, 2021

@author: mballance
'''
from typing import List
from hvlrpc.paramdef import ParamDef
from hvlrpc.apidef import ApiDef

class MethodDef(object):
    
    def __init__(
            self,
            parent,
            name,
            idx,
            is_task,
            rtype,
            params : List[ParamDef]):
        self.parent : ApiDef = parent
        self.name = name
        self.idx = idx
        self.is_task = is_task
        self.rtype = rtype
        self.params : List[ParamDef] = params

        