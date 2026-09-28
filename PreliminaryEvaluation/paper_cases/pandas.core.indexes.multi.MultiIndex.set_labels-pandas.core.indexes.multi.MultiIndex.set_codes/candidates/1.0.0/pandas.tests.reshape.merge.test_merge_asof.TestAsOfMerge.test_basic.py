def test_basic(self):
    expected = self.asof
    trades = self.trades
    quotes = self.quotes
    result = merge_asof(trades, quotes, on='time', by='ticker')
    tm.assert_frame_equal(result, expected)