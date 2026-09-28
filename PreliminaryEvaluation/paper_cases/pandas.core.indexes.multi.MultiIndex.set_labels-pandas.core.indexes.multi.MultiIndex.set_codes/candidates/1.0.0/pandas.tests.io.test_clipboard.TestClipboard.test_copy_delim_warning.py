def test_copy_delim_warning(self, df):
    with tm.assert_produces_warning():
        df.to_clipboard(excel=False, sep='\t')