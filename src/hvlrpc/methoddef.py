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
            is_import,
            is_task,
            rtype,
            params : List[ParamDef]):
        self.parent = parent
        self.name = name
        self.is_import = is_import
        self.is_task = is_task
        self.rtype = rtype
        self.params = params

        