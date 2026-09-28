def test_basic_left_index(self):
    expected = self.asof
    trades = self.trades.set_index('time')
    quotes = self.quotes
    result = merge_asof(trades, quotes, left_index=True, right_on='time', by='ticker')
    expected.index = result.index
    expected = expected[result.columns]
    tm.assert_frame_equal(result, expected)