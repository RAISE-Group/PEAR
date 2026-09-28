def test_join_on_singlekey_list(self):
    df = DataFrame({'key': ['a', 'a', 'b', 'b', 'c']})
    df2 = DataFrame({'value': [0, 1, 2]}, index=['a', 'b', 'c'])
    joined = df.join(df2, on=['key'])
    expected = df.join(df2, on='key')
    tm.assert_frame_equal(joined, expected)