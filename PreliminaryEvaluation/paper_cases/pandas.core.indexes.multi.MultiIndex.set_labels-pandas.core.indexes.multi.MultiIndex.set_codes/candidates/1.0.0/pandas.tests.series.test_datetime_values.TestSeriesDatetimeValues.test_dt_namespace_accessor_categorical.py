def test_dt_namespace_accessor_categorical(self):
    dti = DatetimeIndex(['20171111', '20181212']).repeat(2)
    s = Series(pd.Categorical(dti), name='foo')
    result = s.dt.year
    expected = Series([2017, 2017, 2018, 2018], name='foo')
    tm.assert_series_equal(result, expected)