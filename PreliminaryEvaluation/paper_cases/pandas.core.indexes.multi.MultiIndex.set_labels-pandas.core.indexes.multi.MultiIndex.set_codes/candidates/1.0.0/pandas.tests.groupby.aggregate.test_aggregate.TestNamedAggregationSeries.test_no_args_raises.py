def test_no_args_raises(self):
    gr = pd.Series([1, 2]).groupby([0, 1])
    with pytest.raises(TypeError, match='Must provide'):
        gr.agg()
    result = gr.agg([])
    expected = pd.DataFrame()
    tm.assert_frame_equal(result, expected)