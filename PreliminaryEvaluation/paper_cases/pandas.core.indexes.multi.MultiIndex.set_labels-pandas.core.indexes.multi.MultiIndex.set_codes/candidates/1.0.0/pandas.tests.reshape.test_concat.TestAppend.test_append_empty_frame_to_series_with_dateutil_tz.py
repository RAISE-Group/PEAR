def test_append_empty_frame_to_series_with_dateutil_tz(self):
    date = Timestamp('2018-10-24 07:30:00', tz=dateutil.tz.tzutc())
    s = Series({'date': date, 'a': 1.0, 'b': 2.0})
    df = DataFrame(columns=['c', 'd'])
    result = df.append(s, ignore_index=True)
    expected = DataFrame([[np.nan, np.nan, 1.0, 2.0, date]], columns=['c', 'd', 'a', 'b', 'date'], dtype=object)
    expected['a'] = expected['a'].astype(float)
    expected['b'] = expected['b'].astype(float)
    tm.assert_frame_equal(result, expected)