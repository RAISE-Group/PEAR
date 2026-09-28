def test_pivot_empty(self):
    df = DataFrame(columns=['a', 'b', 'c'])
    result = df.pivot('a', 'b', 'c')
    expected = DataFrame()
    tm.assert_frame_equal(result, expected, check_names=False)