@classmethod
def teardown_class(cls):
    del cls.engine, cls.parser
    if hasattr(cls, 'ne'):
        del cls.ne