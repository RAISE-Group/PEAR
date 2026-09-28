def test_show_null_counts(self):
    df = DataFrame(1, columns=range(10), index=range(10))
    df.iloc[1, 1] = np.nan

    def check(null_counts, result):
        buf = StringIO()
        df.info(buf=buf, null_counts=null_counts)
        assert ('non-null' in buf.getvalue()) is result
    with option_context('display.max_info_rows', 20, 'display.max_info_columns', 20):
        check(None, True)
        check(True, True)
        check(False, False)
    with option_context('display.max_info_rows', 5, 'display.max_info_columns', 5):
        check(None, False)
        check(True, False)
        check(False, False)