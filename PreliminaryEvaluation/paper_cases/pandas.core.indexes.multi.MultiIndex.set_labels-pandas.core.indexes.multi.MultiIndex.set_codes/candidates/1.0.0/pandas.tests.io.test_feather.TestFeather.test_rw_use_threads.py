def test_rw_use_threads(self):
    df = pd.DataFrame({'A': np.arange(100000)})
    self.check_round_trip(df, use_threads=True)
    self.check_round_trip(df, use_threads=False)