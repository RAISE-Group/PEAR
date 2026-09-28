def isna(self):
    dtype = SparseDtype(bool, self._null_fill_value)
    return type(self)._simple_new(isna(self.sp_values), self.sp_index, dtype)