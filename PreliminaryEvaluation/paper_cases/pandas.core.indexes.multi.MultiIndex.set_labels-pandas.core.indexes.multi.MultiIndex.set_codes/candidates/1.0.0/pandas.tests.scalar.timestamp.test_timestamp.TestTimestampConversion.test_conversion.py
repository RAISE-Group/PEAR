def test_conversion(self):
    ts = Timestamp('2000-01-01')
    result = ts.to_pydatetime()
    expected = datetime(2000, 1, 1)
    assert result == expected
    assert type(result) == type(expected)
    result = ts.to_datetime64()
    expected = np.datetime64(ts.value, 'ns')
    assert result == expected
    assert type(result) == type(expected)
    assert result.dtype == expected.dtype