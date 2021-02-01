from hvlrpc.impl.ctor import Ctor
from hvlrpc.impl.registry import Registry


def reset():
    Ctor.reset()
    Registry.reset()