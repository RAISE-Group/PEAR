def test_series_with_name_not_matching_column(self):
    x = pd.Series(range(5), name=1)
    y = pd.Series(range(5), name=0)
    result = pd.DataFrame(x, columns=[0])
    expected = pd.DataFrame([], columns=[0])
    tm.assert_frame_equal(result, expected)
    result = pd.DataFrame(y, columns=[1])
    expected = pd.DataFrame([], columns=[1])
    tm.assert_frame_equal(result, expected)