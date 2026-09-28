def test_basic_categorical(self):
    expected = self.asof
    trades = self.trades.copy()
    trades.ticker = trades.ticker.astype('category')
    quotes = self.quotes.copy()
    quotes.ticker = quotes.ticker.astype('category')
    expected.ticker = expected.ticker.astype('category')
    result = merge_asof(trades, quotes, on='time', by='ticker')
    tm.assert_frame_equal(result, expected)