def test_basic_left_by_right_by(self):
    expected = self.asof
    trades = self.trades
    quotes = self.quotes
    result = merge_asof(trades, quotes, on='time', left_by='ticker', right_by='ticker')
    tm.assert_frame_equal(result, expected)