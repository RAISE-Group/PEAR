def test_ns_index(self):
    nsamples = 400
    ns = int(1000000000.0 / 24414)
    dtstart = np.datetime64('2012-09-20T00:00:00')
    dt = dtstart + np.arange(nsamples) * np.timedelta64(ns, 'ns')
    freq = ns * offsets.Nano()
    index = pd.DatetimeIndex(dt, freq=freq, name='time')
    self.assert_index_parameters(index)
    new_index = pd.date_range(start=index[0], end=index[-1], freq=index.freq)
    self.assert_index_parameters(new_index)