@classmethod
def setup_class(cls):
    super().setup_class()
    cls.engine = 'numexpr'
    cls.parser = 'python'
    cls.arith_ops = expr._arith_ops_syms + expr._cmp_ops_syms
    cls.arith_ops = filter(lambda x: x not in ('in', 'not in'), cls.arith_ops)