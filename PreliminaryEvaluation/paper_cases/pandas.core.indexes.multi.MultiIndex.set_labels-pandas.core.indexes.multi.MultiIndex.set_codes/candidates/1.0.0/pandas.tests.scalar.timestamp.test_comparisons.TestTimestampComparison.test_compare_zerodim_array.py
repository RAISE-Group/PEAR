def test_compare_zerodim_array(self):
    ts = Timestamp.now()
    dt64 = np.datetime64('2016-01-01', 'ns')
    arr = np.array(dt64)
    assert arr.ndim == 0
    result = arr < ts
    assert result is True
    result = arr > ts
    assert result is False