@classmethod
def classmethod(cls):
    raise AbstractMethodError(cls, methodtype='classmethod')