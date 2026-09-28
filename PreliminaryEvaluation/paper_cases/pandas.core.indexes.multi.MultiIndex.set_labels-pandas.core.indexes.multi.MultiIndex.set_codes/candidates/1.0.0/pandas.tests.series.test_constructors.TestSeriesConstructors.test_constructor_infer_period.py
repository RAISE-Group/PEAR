@pytest.mark.parametrize('data_constructor', [list, np.array], ids=['list', 'ndarray[object]'])
def test_constructor_infer_period(self, data_constructor):
    data = [pd.Period('2000', 'D'), pd.Period('2001', 'D'), None]
    result = pd.Series(data_constructor(data))
    expected = pd.Series(period_array(data))
    tm.assert_series_equal(result, expected)
    assert result.dtype == 'Period[D]'