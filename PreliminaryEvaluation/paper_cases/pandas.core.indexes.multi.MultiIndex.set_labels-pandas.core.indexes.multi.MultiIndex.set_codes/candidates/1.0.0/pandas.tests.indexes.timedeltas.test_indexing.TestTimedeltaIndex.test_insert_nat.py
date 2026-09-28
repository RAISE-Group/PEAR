@pytest.mark.parametrize('null', [None, np.nan, np.timedelta64('NaT'), pd.NaT, pd.NA])
def test_insert_nat(self, null):
    idx = timedelta_range('1day', '3day')
    result = idx.insert(1, null)
    expected = TimedeltaIndex(['1day', pd.NaT, '2day', '3day'])
    tm.assert_index_equal(result, expected)