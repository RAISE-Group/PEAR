def test_check_compatible_with(self):
    data = np.arange(10, dtype='i8') * 24 * 3600 * 10 ** 9
    arr = self.array_cls(data, freq='D')
    arr._check_compatible_with(arr[0])
    arr._check_compatible_with(arr[:1])
    arr._check_compatible_with(pd.NaT)