def test_bool_with_none(self, fp):
    df = pd.DataFrame({'a': [True, None, False]})
    expected = pd.DataFrame({'a': [1.0, np.nan, 0.0]}, dtype='float16')
    check_round_trip(df, fp, expected=expected)