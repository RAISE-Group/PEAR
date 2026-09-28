def test_map_datetimetz(self):
    values = pd.date_range('2011-01-01', '2011-01-02', freq='H').tz_localize('Asia/Tokyo')
    s = pd.Series(values, name='XX')
    result = s.map(lambda x: x + pd.offsets.Day())
    exp_values = pd.date_range('2011-01-02', '2011-01-03', freq='H').tz_localize('Asia/Tokyo')
    exp = pd.Series(exp_values, name='XX')
    tm.assert_series_equal(result, exp)
    result = s.map(lambda x: x.hour)
    exp = pd.Series(list(range(24)) + [0], name='XX', dtype=np.int64)
    tm.assert_series_equal(result, exp)
    with pytest.raises(NotImplementedError):
        s.map(lambda x: x, na_action='ignore')

    def f(x):
        if not isinstance(x, pd.Timestamp):
            raise ValueError
        return str(x.tz)
    result = s.map(f)
    exp = pd.Series(['Asia/Tokyo'] * 25, name='XX')
    tm.assert_series_equal(result, exp)