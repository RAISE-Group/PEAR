def _create_dtype_data(self, dtype):
    sr1 = Series(np.arange(5), dtype=dtype)
    sr2 = Series(np.arange(10, 0, -2), dtype=dtype)
    sr3 = sr1.copy()
    sr3[3] = np.NaN
    df = DataFrame(np.arange(10).reshape((5, 2)), dtype=dtype)
    data = {'sr1': sr1, 'sr2': sr2, 'sr3': sr3, 'df': df}
    return data