def test_delete(self):
    idx = timedelta_range(start='1 Days', periods=5, freq='D', name='idx')
    expected_0 = timedelta_range(start='2 Days', periods=4, freq='D', name='idx')
    expected_4 = timedelta_range(start='1 Days', periods=4, freq='D', name='idx')
    expected_1 = TimedeltaIndex(['1 day', '3 day', '4 day', '5 day'], freq=None, name='idx')
    cases = {0: expected_0, -5: expected_0, -1: expected_4, 4: expected_4, 1: expected_1}
    for n, expected in cases.items():
        result = idx.delete(n)
        tm.assert_index_equal(result, expected)
        assert result.name == expected.name
        assert result.freq == expected.freq
    with pytest.raises((IndexError, ValueError)):
        idx.delete(5)