@pytest.mark.parametrize('extension_arr', [Categorical(list('aabbc')), SparseArray([1, np.nan, np.nan, np.nan]), IntervalArray([pd.Interval(0, 1), pd.Interval(1, 5)]), PeriodArray(pd.period_range(start='1/1/2017', end='1/1/2018', freq='M'))])
def test_constructor_with_extension_array(self, extension_arr):
    expected = DataFrame(Series(extension_arr))
    result = DataFrame(extension_arr)
    tm.assert_frame_equal(result, expected)