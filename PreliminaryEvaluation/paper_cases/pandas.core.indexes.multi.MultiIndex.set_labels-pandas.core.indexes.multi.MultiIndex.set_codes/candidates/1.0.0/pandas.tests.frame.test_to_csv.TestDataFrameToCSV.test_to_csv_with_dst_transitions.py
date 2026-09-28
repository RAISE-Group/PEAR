def test_to_csv_with_dst_transitions(self):
    with tm.ensure_clean('csv_date_format_with_dst') as path:
        times = pd.date_range('2013-10-26 23:00', '2013-10-27 01:00', tz='Europe/London', freq='H', ambiguous='infer')
        for i in [times, times + pd.Timedelta('10s')]:
            time_range = np.array(range(len(i)), dtype='int64')
            df = DataFrame({'A': time_range}, index=i)
            df.to_csv(path, index=True)
            result = read_csv(path, index_col=0)
            result.index = to_datetime(result.index, utc=True).tz_convert('Europe/London')
            tm.assert_frame_equal(result, df)
    idx = pd.date_range('2015-01-01', '2015-12-31', freq='H', tz='Europe/Paris')
    df = DataFrame({'values': 1, 'idx': idx}, index=idx)
    with tm.ensure_clean('csv_date_format_with_dst') as path:
        df.to_csv(path, index=True)
        result = read_csv(path, index_col=0)
        result.index = to_datetime(result.index, utc=True).tz_convert('Europe/Paris')
        result['idx'] = to_datetime(result['idx'], utc=True).astype('datetime64[ns, Europe/Paris]')
        tm.assert_frame_equal(result, df)
    df.astype(str)
    with tm.ensure_clean('csv_date_format_with_dst') as path:
        df.to_pickle(path)
        result = pd.read_pickle(path)
        tm.assert_frame_equal(result, df)