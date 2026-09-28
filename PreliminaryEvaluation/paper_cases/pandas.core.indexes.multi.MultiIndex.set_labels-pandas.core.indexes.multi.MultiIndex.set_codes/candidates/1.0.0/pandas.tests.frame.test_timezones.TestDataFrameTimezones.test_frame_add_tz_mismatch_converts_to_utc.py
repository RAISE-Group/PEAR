def test_frame_add_tz_mismatch_converts_to_utc(self):
    rng = date_range('1/1/2011', periods=10, freq='H', tz='US/Eastern')
    df = DataFrame(np.random.randn(len(rng)), index=rng, columns=['a'])
    df_moscow = df.tz_convert('Europe/Moscow')
    result = df + df_moscow
    assert result.index.tz is pytz.utc
    result = df_moscow + df
    assert result.index.tz is pytz.utc