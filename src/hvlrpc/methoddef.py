'''
Created on Jan 31, 2021

@author: mballance
'''
from typing import List
from hvlrpc.paramdef import ParamDef

class MethodDef(object):
    
    def __init__(
            self,
            parent,
            name,
            idx,
            is_task,
            rtype,
            params : List[ParamDef]):
        self.parent = parent
        self.name = name
        self.idx = idx
        self.is_task = is_task
        self.rtype = rtype
        self.params = params

        