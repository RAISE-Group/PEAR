def test_frame_append_datetime64_column(self):
    rng = date_range('1/1/2000 00:00:00', '1/1/2000 1:59:50', freq='10s')
    df = DataFrame(index=np.arange(len(rng)))
    df['A'] = rng
    assert np.issubdtype(df['A'].dtype, np.dtype('M8[ns]'))