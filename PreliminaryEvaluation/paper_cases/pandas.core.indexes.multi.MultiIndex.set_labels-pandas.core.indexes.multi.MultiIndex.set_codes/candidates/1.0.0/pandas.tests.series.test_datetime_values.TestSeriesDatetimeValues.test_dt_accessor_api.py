def test_dt_accessor_api(self):
    from pandas.core.indexes.accessors import CombinedDatetimelikeProperties, DatetimeProperties
    assert Series.dt is CombinedDatetimelikeProperties
    s = Series(date_range('2000-01-01', periods=3))
    assert isinstance(s.dt, DatetimeProperties)