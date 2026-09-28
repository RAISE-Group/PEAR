def test_unbox_scalar(self):
    data = np.arange(10, dtype='i8') * 24 * 3600 * 10 ** 9
    arr = self.array_cls(data, freq='D')
    result = arr._unbox_scalar(arr[0])
    assert isinstance(result, int)
    result = arr._unbox_scalar(pd.NaT)
    assert isinstance(result, int)
    with pytest.raises(ValueError):
        arr._unbox_scalar('foo')