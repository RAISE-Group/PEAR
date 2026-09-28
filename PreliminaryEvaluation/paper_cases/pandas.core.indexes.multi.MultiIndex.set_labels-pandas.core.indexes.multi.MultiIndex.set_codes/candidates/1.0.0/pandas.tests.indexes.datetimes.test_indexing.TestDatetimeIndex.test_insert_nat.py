@pytest.mark.parametrize('null', [None, np.nan, np.datetime64('NaT'), pd.NaT, pd.NA])
@pytest.mark.parametrize('tz', [None, 'UTC', 'US/Eastern'])
def test_insert_nat(self, tz, null):
    idx = pd.DatetimeIndex(['2017-01-01'], tz=tz)
    expected = pd.DatetimeIndex(['NaT', '2017-01-01'], tz=tz)
    res = idx.insert(0, null)
    tm.assert_index_equal(res, expected)