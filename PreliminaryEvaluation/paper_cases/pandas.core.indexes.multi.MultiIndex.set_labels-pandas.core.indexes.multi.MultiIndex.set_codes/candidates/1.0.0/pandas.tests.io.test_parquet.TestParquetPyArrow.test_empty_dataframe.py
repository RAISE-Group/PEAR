def test_empty_dataframe(self, pa):
    df = pd.DataFrame()
    check_round_trip(df, pa)