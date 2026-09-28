@pytest.mark.parametrize('start,end,start_freq,end_freq,base', [('19910905', '19910909 03:00', 'H', '24H', 10), ('19910905', '19910909 12:00', 'H', '24H', 10), ('19910905', '19910909 23:00', 'H', '24H', 10), ('19910905 10:00', '19910909', 'H', '24H', 10), ('19910905 10:00', '19910909 10:00', 'H', '24H', 10), ('19910905', '19910909 10:00', 'H', '24H', 10), ('19910905 12:00', '19910909', 'H', '24H', 10), ('19910905 12:00', '19910909 03:00', 'H', '24H', 10), ('19910905 12:00', '19910909 12:00', 'H', '24H', 10), ('19910905 12:00', '19910909 12:00', 'H', '24H', 34), ('19910905 12:00', '19910909 12:00', 'H', '17H', 10), ('19910905 12:00', '19910909 12:00', 'H', '17H', 3), ('19910905 12:00', '19910909 1:00', 'H', 'M', 3), ('19910905', '19910913 06:00', '2H', '24H', 10), ('19910905', '19910905 01:39', 'Min', '5Min', 3), ('19910905', '19910905 03:18', '2Min', '5Min', 3)])
def test_resample_with_non_zero_base(self, start, end, start_freq, end_freq, base):
    s = pd.Series(0, index=pd.period_range(start, end, freq=start_freq))
    s = s + np.arange(len(s))
    result = s.resample(end_freq, base=base).mean()
    result = result.to_timestamp(end_freq)
    result = result.asfreq(end_freq) if end_freq == '24H' else result
    expected = s.to_timestamp().resample(end_freq, base=base).mean()
    tm.assert_series_equal(result, expected)