@classmethod
def setup_class(cls):
    super().setup_class()
    cls.engine = 'python'
    cls.parser = 'pandas'
    cls.arith_ops = expr._arith_ops_syms + expr._cmp_ops_syms