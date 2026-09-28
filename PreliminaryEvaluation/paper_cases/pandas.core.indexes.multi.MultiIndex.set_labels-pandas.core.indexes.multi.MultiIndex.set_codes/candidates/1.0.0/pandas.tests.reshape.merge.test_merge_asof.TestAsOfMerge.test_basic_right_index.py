def test_basic_right_index(self):
    expected = self.asof
    trades = self.trades
    quotes = self.quotes.set_index('time')
    result = merge_asof(trades, quotes, left_on='time', right_index=True, by='ticker')
    tm.assert_frame_equal(result, expected)