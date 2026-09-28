@classmethod
def setup_class(cls):
    from copy import deepcopy
    cls.cf = cf
    cls.gc = deepcopy(getattr(cls.cf, '_global_config'))
    cls.do = deepcopy(getattr(cls.cf, '_deprecated_options'))
    cls.ro = deepcopy(getattr(cls.cf, '_registered_options'))