@pytest.mark.parametrize('freq', ['A', '2A', '-2A', 'Q', '-1Q', 'M', '-1M', 'D', '3D', '-3D', 'W', '-1W', 'H', '2H', '-2H', 'T', '2T', 'S', '-3S'])
def test_infer_freq(self, freq):
    idx = pd.date_range('2011-01-01 09:00:00', freq=freq, periods=10)
    result = pd.DatetimeIndex(idx.asi8, freq='infer')
    tm.assert_index_equal(idx, result)
    assert result.freq == freq