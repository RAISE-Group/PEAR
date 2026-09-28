@pytest.mark.parametrize('op, expected_col', [['max', 'a'], ['min', 'b']])
def test_same_tz_min_max_axis_1(self, op, expected_col):
    df = DataFrame(pd.date_range('2016-01-01 00:00:00', periods=3, tz='UTC'), columns=['a'])
    df['b'] = df.a.subtract(pd.Timedelta(seconds=3600))
    result = getattr(df, op)(axis=1)
    expected = df[expected_col].rename(None)
    tm.assert_series_equal(result, expected)