def test_describe_empty_object(self):
    df = pd.DataFrame({'A': [None, None]}, dtype=object)
    result = df.describe()
    expected = pd.DataFrame({'A': [0, 0, np.nan, np.nan]}, dtype=object, index=['count', 'unique', 'top', 'freq'])
    tm.assert_frame_equal(result, expected)
    result = df.iloc[:0].describe()
    tm.assert_frame_equal(result, expected)