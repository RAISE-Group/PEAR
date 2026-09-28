def test_frame_ctor_datetime64_column(self):
    rng = date_range('1/1/2000 00:00:00', '1/1/2000 1:59:50', freq='10s')
    dates = np.asarray(rng)
    df = DataFrame({'A': np.random.randn(len(rng)), 'B': dates})
    assert np.issubdtype(df['B'].dtype, np.dtype('M8[ns]'))