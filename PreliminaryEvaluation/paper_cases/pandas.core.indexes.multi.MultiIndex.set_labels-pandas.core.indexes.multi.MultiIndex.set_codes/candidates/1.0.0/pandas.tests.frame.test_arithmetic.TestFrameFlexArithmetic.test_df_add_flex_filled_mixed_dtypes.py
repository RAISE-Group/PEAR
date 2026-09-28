def test_df_add_flex_filled_mixed_dtypes(self):
    dti = pd.date_range('2016-01-01', periods=3)
    ser = pd.Series(['1 Day', 'NaT', '2 Days'], dtype='timedelta64[ns]')
    df = pd.DataFrame({'A': dti, 'B': ser})
    other = pd.DataFrame({'A': ser, 'B': ser})
    fill = pd.Timedelta(days=1).to_timedelta64()
    result = df.add(other, fill_value=fill)
    expected = pd.DataFrame({'A': pd.Series(['2016-01-02', '2016-01-03', '2016-01-05'], dtype='datetime64[ns]'), 'B': ser * 2})
    tm.assert_frame_equal(result, expected)