def test_is_all_dates(self):
    year_2017 = pd.Interval(pd.Timestamp('2017-01-01 00:00:00'), pd.Timestamp('2018-01-01 00:00:00'))
    year_2017_index = pd.IntervalIndex([year_2017])
    assert not year_2017_index.is_all_dates