@pytest.mark.parametrize('data,expected', [([True, False], [True]), ([True, False, True, True], [True])])
def test_nlargest_boolean(self, data, expected):
    ser = Series(data)
    result = ser.nlargest(1)
    expected = Series(expected)
    tm.assert_series_equal(result, expected)