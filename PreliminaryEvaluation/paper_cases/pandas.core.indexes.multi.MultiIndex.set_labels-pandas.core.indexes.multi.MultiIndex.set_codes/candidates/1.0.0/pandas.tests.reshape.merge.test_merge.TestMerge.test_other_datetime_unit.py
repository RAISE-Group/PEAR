def test_other_datetime_unit(self):
    df1 = pd.DataFrame({'entity_id': [101, 102]})
    s = pd.Series([None, None], index=[101, 102], name='days')
    for dtype in ['datetime64[D]', 'datetime64[h]', 'datetime64[m]', 'datetime64[s]', 'datetime64[ms]', 'datetime64[us]', 'datetime64[ns]']:
        df2 = s.astype(dtype).to_frame('days')
        assert df2['days'].dtype == 'datetime64[ns]'
        result = df1.merge(df2, left_on='entity_id', right_index=True)
        exp = pd.DataFrame({'entity_id': [101, 102], 'days': np.array(['nat', 'nat'], dtype='datetime64[ns]')}, columns=['entity_id', 'days'])
        tm.assert_frame_equal(result, exp)