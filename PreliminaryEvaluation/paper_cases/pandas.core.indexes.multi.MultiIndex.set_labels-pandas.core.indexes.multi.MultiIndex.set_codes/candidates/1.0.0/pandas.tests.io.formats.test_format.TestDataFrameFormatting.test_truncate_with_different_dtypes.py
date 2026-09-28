def test_truncate_with_different_dtypes(self):
    import datetime
    s = Series([datetime.datetime(2012, 1, 1)] * 10 + [datetime.datetime(1012, 1, 2)] + [datetime.datetime(2012, 1, 3)] * 10)
    with pd.option_context('display.max_rows', 8):
        result = str(s)
        assert 'object' in result
    df = DataFrame({'text': ['some words'] + [None] * 9})
    with pd.option_context('display.max_rows', 8, 'display.max_columns', 3):
        result = str(df)
        assert 'None' in result
        assert 'NaN' not in result