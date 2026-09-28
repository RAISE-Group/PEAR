@pytest.mark.parametrize('input_vals', ['2001', 'NaT'])
def test_to_period(self, input_vals):
    expected = Series([input_vals], dtype='Period[D]')
    result = Series([input_vals], dtype='datetime64[ns]').dt.to_period('D')
    tm.assert_series_equal(result, expected)