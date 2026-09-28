def _create_dtype_data(self, dtype):
    sr1 = Series(range(5), dtype=dtype)
    sr2 = Series(range(10, 0, -2), dtype=dtype)
    data = {'sr1': sr1, 'sr2': sr2}
    return data