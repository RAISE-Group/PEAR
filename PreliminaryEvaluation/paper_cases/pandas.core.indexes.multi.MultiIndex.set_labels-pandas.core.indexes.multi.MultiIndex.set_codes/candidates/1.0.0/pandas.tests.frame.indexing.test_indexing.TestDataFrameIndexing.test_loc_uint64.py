@pytest.mark.parametrize('val,expected', [(2 ** 63 - 1, Series([1])), (2 ** 63, Series([2]))])
def test_loc_uint64(self, val, expected):
    df = DataFrame([1, 2], index=[2 ** 63 - 1, 2 ** 63])
    result = df.loc[val]
    expected.name = val
    tm.assert_series_equal(result, expected)