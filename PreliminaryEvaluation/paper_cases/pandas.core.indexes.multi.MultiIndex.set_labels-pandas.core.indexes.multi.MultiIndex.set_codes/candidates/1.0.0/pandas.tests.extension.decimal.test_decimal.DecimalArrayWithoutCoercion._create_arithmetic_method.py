@classmethod
def _create_arithmetic_method(cls, op):
    return cls._create_method(op, coerce_to_dtype=False)