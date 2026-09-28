@classmethod
def setup_class(cls):
    super().setup_class()
    import numexpr as ne
    cls.ne = ne
    cls.engine = 'numexpr'
    cls.parser = 'python'