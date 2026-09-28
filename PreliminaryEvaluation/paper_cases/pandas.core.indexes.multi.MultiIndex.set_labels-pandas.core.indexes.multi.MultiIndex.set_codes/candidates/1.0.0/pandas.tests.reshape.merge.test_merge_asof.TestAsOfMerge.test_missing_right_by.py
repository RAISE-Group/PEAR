def test_missing_right_by(self):
    expected = self.asof
    trades = self.trades
    quotes = self.quotes
    q = quotes[quotes.ticker != 'MSFT']
    result = merge_asof(trades, q, on='time', by='ticker')
    expected.loc[expected.ticker == 'MSFT', ['bid', 'ask']] = np.nan
    tm.assert_frame_equal(result, expected)