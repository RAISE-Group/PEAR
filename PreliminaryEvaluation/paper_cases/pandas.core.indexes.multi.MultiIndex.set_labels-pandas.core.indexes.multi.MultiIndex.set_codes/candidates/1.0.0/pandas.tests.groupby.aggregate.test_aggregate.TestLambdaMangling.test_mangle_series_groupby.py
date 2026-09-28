def test_mangle_series_groupby(self):
    gr = pd.Series([1, 2, 3, 4]).groupby([0, 0, 1, 1])
    result = gr.agg([lambda x: 0, lambda x: 1])
    expected = pd.DataFrame({'<lambda_0>': [0, 0], '<lambda_1>': [1, 1]})
    tm.assert_frame_equal(result, expected)