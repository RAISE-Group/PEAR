def _union(self, other, sort):
    needs_cast = is_integer_dtype(self.dtype) and is_float_dtype(other.dtype) or (is_integer_dtype(other.dtype) and is_float_dtype(self.dtype))
    if needs_cast:
        first = self.astype('float')
        second = other.astype('float')
        return first._union(second, sort)
    else:
        return super()._union(other, sort)