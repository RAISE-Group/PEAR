def test_filter_regex_non_string(self):
    df = pd.DataFrame(np.random.random((3, 2)), columns=['STRING', 123])
    result = df.filter(regex='STRING')
    expected = df[['STRING']]
    tm.assert_frame_equal(result, expected)