def test_allow_exact_matches(self):
    result = merge_asof(self.trades, self.quotes, on='time', by='ticker', allow_exact_matches=False)
    expected = self.allow_exact_matches
    tm.assert_frame_equal(result, expected)