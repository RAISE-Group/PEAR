def test_allow_exact_matches_and_tolerance(self):
    result = merge_asof(self.trades, self.quotes, on='time', by='ticker', tolerance=Timedelta('100ms'), allow_exact_matches=False)
    expected = self.allow_exact_matches_and_tolerance
    tm.assert_frame_equal(result, expected)