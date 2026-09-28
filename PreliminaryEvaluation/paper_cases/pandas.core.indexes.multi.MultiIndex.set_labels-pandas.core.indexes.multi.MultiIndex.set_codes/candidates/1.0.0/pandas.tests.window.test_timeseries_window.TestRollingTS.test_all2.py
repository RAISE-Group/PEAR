def test_all2(self):
    df = DataFrame({'B': np.arange(50)}, index=date_range('20130101', periods=50, freq='H'))
    dft = df.between_time('09:00', '16:00')
    r = dft.rolling(window='5H')
    for f in ['sum', 'mean', 'count', 'median', 'std', 'var', 'kurt', 'skew', 'min', 'max']:
        result = getattr(r, f)()

        def agg_by_day(x):
            x = x.between_time('09:00', '16:00')
            return getattr(x.rolling(5, min_periods=1), f)()
        expected = df.groupby(df.index.day).apply(agg_by_day).reset_index(level=0, drop=True)
        tm.assert_frame_equal(result, expected)