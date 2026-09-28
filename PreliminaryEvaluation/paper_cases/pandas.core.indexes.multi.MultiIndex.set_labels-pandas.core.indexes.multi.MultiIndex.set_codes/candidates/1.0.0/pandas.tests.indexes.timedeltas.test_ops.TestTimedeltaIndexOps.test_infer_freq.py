@pytest.mark.parametrize('freq', ['D', '3D', '-3D', 'H', '2H', '-2H', 'T', '2T', 'S', '-3S'])
def test_infer_freq(self, freq):
    idx = pd.timedelta_range('1', freq=freq, periods=10)
    result = pd.TimedeltaIndex(idx.asi8, freq='infer')
    tm.assert_index_equal(idx, result)
    assert result.freq == freq