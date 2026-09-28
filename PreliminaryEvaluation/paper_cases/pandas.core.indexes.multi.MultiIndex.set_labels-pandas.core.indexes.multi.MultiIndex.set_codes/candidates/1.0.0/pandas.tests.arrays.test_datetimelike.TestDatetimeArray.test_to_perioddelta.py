@pytest.mark.parametrize('freqstr', ['D', 'B', 'W', 'M', 'Q', 'Y'])
def test_to_perioddelta(self, datetime_index, freqstr):
    dti = datetime_index
    arr = DatetimeArray(dti)
    expected = dti.to_perioddelta(freq=freqstr)
    result = arr.to_perioddelta(freq=freqstr)
    assert isinstance(result, TimedeltaArray)
    tm.assert_index_equal(pd.Index(result), pd.Index(expected))