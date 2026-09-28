def test_round(self, tz_naive_fixture):
    tz = tz_naive_fixture
    dti = pd.date_range('2016-01-01 01:01:00', periods=3, freq='H', tz=tz)
    result = dti.round(freq='2T')
    expected = dti - pd.Timedelta(minutes=1)
    tm.assert_index_equal(result, expected)