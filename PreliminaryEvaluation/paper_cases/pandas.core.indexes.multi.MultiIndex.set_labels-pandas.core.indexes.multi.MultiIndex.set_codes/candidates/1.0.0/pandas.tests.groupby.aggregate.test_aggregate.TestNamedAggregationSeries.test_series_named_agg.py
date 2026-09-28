def test_series_named_agg(self):
    df = pd.Series([1, 2, 3, 4])
    gr = df.groupby([0, 0, 1, 1])
    result = gr.agg(a='sum', b='min')
    expected = pd.DataFrame({'a': [3, 7], 'b': [1, 3]}, columns=['a', 'b'], index=[0, 1])
    tm.assert_frame_equal(result, expected)
    result = gr.agg(b='min', a='sum')
    expected = expected[['b', 'a']]
    tm.assert_frame_equal(result, expected)