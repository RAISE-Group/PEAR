def test_timegrouper_apply_return_type_value(self):
    df = pd.DataFrame({'date': ['10/10/2000', '11/10/2000'], 'value': [10, 13]})
    df_dt = df.copy()
    df_dt['date'] = pd.to_datetime(df_dt['date'])

    def sumfunc_value(x):
        return x.value.sum()
    expected = df.groupby(pd.Grouper(key='date')).apply(sumfunc_value)
    result = df_dt.groupby(Grouper(freq='M', key='date')).apply(sumfunc_value)
    tm.assert_series_equal(result.reset_index(drop=True), expected.reset_index(drop=True))