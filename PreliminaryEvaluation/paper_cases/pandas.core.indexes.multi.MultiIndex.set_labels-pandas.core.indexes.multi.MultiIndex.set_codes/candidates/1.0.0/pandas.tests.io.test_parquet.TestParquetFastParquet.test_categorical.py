def test_categorical(self, fp):
    df = pd.DataFrame({'a': pd.Categorical(list('abc'))})
    check_round_trip(df, fp)