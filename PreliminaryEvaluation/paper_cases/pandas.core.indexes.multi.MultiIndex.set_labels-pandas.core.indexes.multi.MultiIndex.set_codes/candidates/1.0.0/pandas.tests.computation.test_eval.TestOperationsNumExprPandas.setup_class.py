@classmethod
def setup_class(cls):
    cls.engine = 'numexpr'
    cls.parser = 'pandas'
    cls.arith_ops = expr._arith_ops_syms + expr._cmp_ops_syms