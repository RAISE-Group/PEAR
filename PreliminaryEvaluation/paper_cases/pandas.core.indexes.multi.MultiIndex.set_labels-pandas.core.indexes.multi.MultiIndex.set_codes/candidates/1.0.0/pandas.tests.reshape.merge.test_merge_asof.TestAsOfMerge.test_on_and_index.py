def test_on_and_index(self):
    trades = self.trades.set_index('time')
    quotes = self.quotes.set_index('time')
    with pytest.raises(MergeError):
        merge_asof(trades, quotes, left_on='price', left_index=True, right_index=True)
    trades = self.trades.set_index('time')
    quotes = self.quotes.set_index('time')
    with pytest.raises(MergeError):
        merge_asof(trades, quotes, right_on='bid', left_index=True, right_index=True)