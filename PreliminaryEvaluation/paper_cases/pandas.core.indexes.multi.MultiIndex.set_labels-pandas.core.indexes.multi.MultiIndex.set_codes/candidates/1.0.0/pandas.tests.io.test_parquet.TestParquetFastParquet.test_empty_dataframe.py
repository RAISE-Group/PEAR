def test_empty_dataframe(self, fp):
    df = pd.DataFrame()
    expected = df.copy()
    expected.index.name = 'index'
    check_round_trip(df, fp, expected=expected)