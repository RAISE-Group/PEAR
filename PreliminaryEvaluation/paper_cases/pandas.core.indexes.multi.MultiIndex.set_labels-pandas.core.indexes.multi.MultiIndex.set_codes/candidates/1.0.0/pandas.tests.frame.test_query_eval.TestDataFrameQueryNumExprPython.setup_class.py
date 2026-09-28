@classmethod
def setup_class(cls):
    super().setup_class()
    cls.engine = 'numexpr'
    cls.parser = 'python'