@pytest.mark.parametrize('empty', [[], Series(dtype=object), np.array([])])
def test_isin_empty(self, empty):
    s = Series(['a', 'b'])
    expected = Series([False, False])
    result = s.isin(empty)
    tm.assert_series_equal(expected, result)