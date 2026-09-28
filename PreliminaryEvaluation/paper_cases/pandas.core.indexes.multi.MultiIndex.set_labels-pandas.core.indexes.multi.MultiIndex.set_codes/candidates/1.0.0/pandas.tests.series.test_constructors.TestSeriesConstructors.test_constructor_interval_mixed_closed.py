@pytest.mark.parametrize('data_constructor', [list, np.array], ids=['list', 'ndarray[object]'])
def test_constructor_interval_mixed_closed(self, data_constructor):
    data = [pd.Interval(0, 1, closed='both'), pd.Interval(0, 2, closed='neither')]
    result = Series(data_constructor(data))
    assert result.dtype == object
    assert result.tolist() == data