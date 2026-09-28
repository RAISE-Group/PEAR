def test_mangled(self):
    gr = pd.Series([1, 2, 3]).groupby([0, 0, 1])
    result = gr.agg(a=lambda x: 0, b=lambda x: 1)
    expected = pd.DataFrame({'a': [0, 0], 'b': [1, 1]})
    tm.assert_frame_equal(result, expected)