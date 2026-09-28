@pytest.mark.parametrize('freq', ['BA', 'BY'])
def test_business_end_year_alias(self, freq):
    rng = date_range('1/1/2013', '7/1/2017', freq=freq)
    exp = pd.DatetimeIndex(['2013-12-31', '2014-12-31', '2015-12-31', '2016-12-30'], freq=freq)
    tm.assert_index_equal(rng, exp)