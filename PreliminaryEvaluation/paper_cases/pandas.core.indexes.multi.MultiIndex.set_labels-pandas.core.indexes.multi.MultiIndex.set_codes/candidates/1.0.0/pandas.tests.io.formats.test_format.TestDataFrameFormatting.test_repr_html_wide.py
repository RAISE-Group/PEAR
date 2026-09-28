def test_repr_html_wide(self):
    max_cols = 20
    df = DataFrame(tm.rands_array(25, size=(10, max_cols - 1)))
    with option_context('display.max_rows', 60, 'display.max_columns', 20):
        assert '...' not in df._repr_html_()
    wide_df = DataFrame(tm.rands_array(25, size=(10, max_cols + 1)))
    with option_context('display.max_rows', 60, 'display.max_columns', 20):
        assert '...' in wide_df._repr_html_()