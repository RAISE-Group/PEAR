def test_basic_no_by(self):
    f = lambda x: x[x.ticker == 'MSFT'].drop('ticker', axis=1).reset_index(drop=True)
    expected = f(self.asof)
    trades = f(self.trades)
    quotes = f(self.quotes)
    result = merge_asof(trades, quotes, on='time')
    tm.assert_frame_equal(result, expected)