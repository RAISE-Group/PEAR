def test_iloc_getitem_neg_int_can_reach_first_index(self):
    df = DataFrame({'A': [2, 3, 5], 'B': [7, 11, 13]})
    s = df['A']
    expected = df.iloc[0]
    result = df.iloc[-3]
    tm.assert_series_equal(result, expected)
    expected = df.iloc[[0]]
    result = df.iloc[[-3]]
    tm.assert_frame_equal(result, expected)
    expected = s.iloc[0]
    result = s.iloc[-3]
    assert result == expected
    expected = s.iloc[[0]]
    result = s.iloc[[-3]]
    tm.assert_series_equal(result, expected)
    expected = Series(['a'], index=['A'])
    result = expected.iloc[[-1]]
    tm.assert_series_equal(result, expected)