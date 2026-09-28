@pytest.mark.parametrize('freq', ['AS', 'YS'])
def test_begin_year_alias(self, freq):
    rng = date_range('1/1/2013', '7/1/2017', freq=freq)
    exp = pd.DatetimeIndex(['2013-01-01', '2014-01-01', '2015-01-01', '2016-01-01', '2017-01-01'], freq=freq)
    tm.assert_index_equal(rng, exp)