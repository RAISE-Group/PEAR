@pytest.mark.parametrize('how', ['S', 'E'])
def test_to_timestamp(self, how, period_index):
    pi = period_index
    arr = PeriodArray(pi)
    expected = DatetimeArray(pi.to_timestamp(how=how))
    result = arr.to_timestamp(how=how)
    assert isinstance(result, DatetimeArray)
    tm.assert_index_equal(pd.Index(result), pd.Index(expected))