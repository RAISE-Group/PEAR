@classmethod
def setup_class(cls):
    cls.engine = 'python'
    cls.parser = 'pandas'
    cls.unary_fns = _unary_math_ops
    cls.binary_fns = _binary_math_ops