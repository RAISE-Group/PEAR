def test_timegrouper_apply_return_type_series(self):
    df = pd.DataFrame({'date': ['10/10/2000', '11/10/2000'], 'value': [10, 13]})
    df_dt = df.copy()
    df_dt['date'] = pd.to_datetime(df_dt['date'])

    def sumfunc_series(x):
        return pd.Series([x['value'].sum()], ('sum',))
    expected = df.groupby(pd.Grouper(key='date')).apply(sumfunc_series)
    result = df_dt.groupby(pd.Grouper(freq='M', key='date')).apply(sumfunc_series)
    tm.assert_frame_equal(result.reset_index(drop=True), expected.reset_index(drop=True))