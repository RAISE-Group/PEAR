def test_excel_sep_warning(self, df):
    with tm.assert_produces_warning():
        df.to_clipboard(excel=True, sep='\\t')