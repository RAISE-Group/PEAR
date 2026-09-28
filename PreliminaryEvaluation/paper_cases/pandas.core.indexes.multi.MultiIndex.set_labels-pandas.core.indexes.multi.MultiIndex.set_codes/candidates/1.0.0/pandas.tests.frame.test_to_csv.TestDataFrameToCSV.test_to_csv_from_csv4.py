def test_to_csv_from_csv4(self):
    with tm.ensure_clean('__tmp_to_csv_from_csv4__') as path:
        dt = pd.Timedelta(seconds=1)
        df = pd.DataFrame({'dt_data': [i * dt for i in range(3)]}, index=pd.Index([i * dt for i in range(3)], name='dt_index'))
        df.to_csv(path)
        result = pd.read_csv(path, index_col='dt_index')
        result.index = pd.to_timedelta(result.index)
        result.index = result.index.rename('dt_index')
        result['dt_data'] = pd.to_timedelta(result['dt_data'])
        tm.assert_frame_equal(df, result, check_index_type=True)