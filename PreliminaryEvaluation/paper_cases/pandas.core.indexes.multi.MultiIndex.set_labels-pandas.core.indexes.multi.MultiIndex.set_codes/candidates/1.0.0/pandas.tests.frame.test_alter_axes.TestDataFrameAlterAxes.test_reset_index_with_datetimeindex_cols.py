def test_reset_index_with_datetimeindex_cols(self):
    df = DataFrame([[1, 2], [3, 4]], columns=date_range('1/1/2013', '1/2/2013'), index=['A', 'B'])
    result = df.reset_index()
    expected = DataFrame([['A', 1, 2], ['B', 3, 4]], columns=['index', datetime(2013, 1, 1), datetime(2013, 1, 2)])
    tm.assert_frame_equal(result, expected)