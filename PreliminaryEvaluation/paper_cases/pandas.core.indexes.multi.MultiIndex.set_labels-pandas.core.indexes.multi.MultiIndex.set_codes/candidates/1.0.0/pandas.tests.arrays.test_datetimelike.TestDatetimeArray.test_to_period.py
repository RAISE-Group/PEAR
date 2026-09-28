@pytest.mark.parametrize('freqstr', ['D', 'B', 'W', 'M', 'Q', 'Y'])
def test_to_period(self, datetime_index, freqstr):
    dti = datetime_index
    arr = DatetimeArray(dti)
    expected = dti.to_period(freq=freqstr)
    result = arr.to_period(freq=freqstr)
    assert isinstance(result, PeriodArray)
    tm.assert_index_equal(pd.Index(result), pd.Index(expected))