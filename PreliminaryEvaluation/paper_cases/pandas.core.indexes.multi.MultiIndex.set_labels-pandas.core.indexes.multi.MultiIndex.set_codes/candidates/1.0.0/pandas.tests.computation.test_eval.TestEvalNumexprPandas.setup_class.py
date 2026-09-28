@classmethod
def setup_class(cls):
    import numexpr as ne
    cls.ne = ne
    cls.engine = 'numexpr'
    cls.parser = 'pandas'