def test_basic_left_index_right_index(self):
    expected = self.asof.set_index('time')
    trades = self.trades.set_index('time')
    quotes = self.quotes.set_index('time')
    result = merge_asof(trades, quotes, left_index=True, right_index=True, by='ticker')
    tm.assert_frame_equal(result, expected)