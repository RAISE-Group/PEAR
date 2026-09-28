def test_take_fill(self):
    data = np.arange(10, dtype='i8') * 24 * 3600 * 10 ** 9
    idx = self.index_cls._simple_new(data, freq='D')
    arr = self.array_cls(idx)
    result = arr.take([-1, 1], allow_fill=True, fill_value=None)
    assert result[0] is pd.NaT
    result = arr.take([-1, 1], allow_fill=True, fill_value=np.nan)
    assert result[0] is pd.NaT
    result = arr.take([-1, 1], allow_fill=True, fill_value=pd.NaT)
    assert result[0] is pd.NaT
    with pytest.raises(ValueError):
        arr.take([0, 1], allow_fill=True, fill_value=2)
    with pytest.raises(ValueError):
        arr.take([0, 1], allow_fill=True, fill_value=2.0)
    with pytest.raises(ValueError):
        arr.take([0, 1], allow_fill=True, fill_value=pd.Timestamp.now().time)