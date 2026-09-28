@pytest.mark.parametrize('breaks', [[1, 1, 2, 5, 15, 53, 217, 1014, 5335, 31240, 201608], [-np.inf, -100, -10, 0.5, 1, 1.5, 3.8, 101, 202, np.inf], pd.to_datetime(['20170101', '20170202', '20170303', '20170404']), pd.to_timedelta(['1ns', '2ms', '3s', '4M', '5H', '6D'])])
def test_length(self, closed, breaks):
    index = IntervalIndex.from_breaks(breaks, closed=closed)
    result = index.length
    expected = Index((iv.length for iv in index))
    tm.assert_index_equal(result, expected)
    index = index.insert(1, np.nan)
    result = index.length
    expected = Index((iv.length if notna(iv) else iv for iv in index))
    tm.assert_index_equal(result, expected)