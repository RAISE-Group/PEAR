def test_dt_accessor_updates_on_inplace(self):
    s = Series(pd.date_range('2018-01-01', periods=10))
    s[2] = None
    s.fillna(pd.Timestamp('2018-01-01'), inplace=True)
    result = s.dt.date
    assert result[0] == result[2]