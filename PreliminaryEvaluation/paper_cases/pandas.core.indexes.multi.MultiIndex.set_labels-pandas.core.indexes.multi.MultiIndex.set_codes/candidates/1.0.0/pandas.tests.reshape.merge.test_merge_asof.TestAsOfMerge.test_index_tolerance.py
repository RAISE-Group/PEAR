def test_index_tolerance(self):
    expected = self.tolerance.set_index('time')
    trades = self.trades.set_index('time')
    quotes = self.quotes.set_index('time')
    result = pd.merge_asof(trades, quotes, left_index=True, right_index=True, by='ticker', tolerance=pd.Timedelta('1day'))
    tm.assert_frame_equal(result, expected)