def test_get_numeric_data_extension_dtype(self):
    df = DataFrame({'A': integer_array([-10, np.nan, 0, 10, 20, 30], dtype='Int64'), 'B': Categorical(list('abcabc')), 'C': integer_array([0, 1, 2, 3, np.nan, 5], dtype='UInt8'), 'D': IntervalArray.from_breaks(range(7))})
    result = df._get_numeric_data()
    expected = df.loc[:, ['A', 'C']]
    tm.assert_frame_equal(result, expected)