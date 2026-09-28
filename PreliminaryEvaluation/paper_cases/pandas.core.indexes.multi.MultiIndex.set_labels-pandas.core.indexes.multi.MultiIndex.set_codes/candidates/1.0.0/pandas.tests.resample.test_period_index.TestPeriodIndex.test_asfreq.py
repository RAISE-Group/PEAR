@pytest.mark.parametrize('freq', ['2D', '1H', '2H'])
@pytest.mark.parametrize('kind', ['period', None, 'timestamp'])
def test_asfreq(self, series_and_frame, freq, kind):
    obj = series_and_frame
    if kind == 'timestamp':
        expected = obj.to_timestamp().resample(freq).asfreq()
    else:
        start = obj.index[0].to_timestamp(how='start')
        end = (obj.index[-1] + obj.index.freq).to_timestamp(how='start')
        new_index = date_range(start=start, end=end, freq=freq, closed='left')
        expected = obj.to_timestamp().reindex(new_index).to_period(freq)
    result = obj.resample(freq, kind=kind).asfreq()
    tm.assert_almost_equal(result, expected)