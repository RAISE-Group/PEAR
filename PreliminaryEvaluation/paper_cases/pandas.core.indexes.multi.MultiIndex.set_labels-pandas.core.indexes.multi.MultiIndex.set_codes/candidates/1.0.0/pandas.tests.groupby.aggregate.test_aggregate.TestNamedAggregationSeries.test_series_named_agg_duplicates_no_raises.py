def test_series_named_agg_duplicates_no_raises(self):
    gr = pd.Series([1, 2, 3]).groupby([0, 0, 1])
    grouped = gr.agg(a='sum', b='sum')
    expected = pd.DataFrame({'a': [3, 3], 'b': [3, 3]})
    tm.assert_frame_equal(expected, grouped)