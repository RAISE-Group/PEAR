def test_frame_any_all_group(self):
    df = DataFrame({'data': [False, False, True, False, True, False, True]}, index=[['one', 'one', 'two', 'one', 'two', 'two', 'two'], [0, 1, 0, 2, 1, 2, 3]])
    result = df.any(level=0)
    ex = DataFrame({'data': [False, True]}, index=['one', 'two'])
    tm.assert_frame_equal(result, ex)
    result = df.all(level=0)
    ex = DataFrame({'data': [False, False]}, index=['one', 'two'])
    tm.assert_frame_equal(result, ex)