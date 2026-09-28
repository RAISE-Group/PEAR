@pytest.mark.parametrize('accessor', ['year', 'month', 'day'])
def test_dt_other_accessors_categorical(self, accessor):
    datetimes = pd.Series(['2018-01-01', '2018-01-01', '2019-01-02'], dtype='datetime64[ns]')
    categorical = datetimes.astype('category')
    result = getattr(categorical.dt, accessor)
    expected = getattr(datetimes.dt, accessor)
    tm.assert_series_equal(result, expected)