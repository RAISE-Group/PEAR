@pytest.mark.parametrize('n', range(1, 5))
def test_nlargest_n(self, n):
    ser = Series([1, 4, 3, 2], index=[0, 0, 1, 1])
    result = ser.nlargest(n)
    expected = ser.sort_values(ascending=False).head(n)
    tm.assert_series_equal(result, expected)
    result = ser.nsmallest(n)
    expected = ser.sort_values().head(n)
    tm.assert_series_equal(result, expected)