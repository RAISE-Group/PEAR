@pytest.mark.parametrize('data_constructor', [list, np.array], ids=['list', 'ndarray[object]'])
def test_constructor_infer_interval(self, data_constructor):
    data = [pd.Interval(0, 1), pd.Interval(0, 2), None]
    result = pd.Series(data_constructor(data))
    expected = pd.Series(IntervalArray(data))
    assert result.dtype == 'interval[float64]'
    tm.assert_series_equal(result, expected)