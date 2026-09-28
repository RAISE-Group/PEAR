def test_series_map_box_timedelta(self):
    s = Series(timedelta_range('1 day 1 s', periods=5, freq='h'))

    def f(x):
        return x.total_seconds()
    s.map(f)
    s.apply(f)
    DataFrame(s).applymap(f)