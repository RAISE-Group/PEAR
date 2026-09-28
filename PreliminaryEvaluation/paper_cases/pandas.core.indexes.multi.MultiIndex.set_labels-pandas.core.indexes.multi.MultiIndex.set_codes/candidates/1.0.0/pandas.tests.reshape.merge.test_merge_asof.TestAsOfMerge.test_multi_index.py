def test_multi_index(self):
    trades = self.trades.set_index(['time', 'price'])
    quotes = self.quotes.set_index('time')
    with pytest.raises(MergeError):
        merge_asof(trades, quotes, left_index=True, right_index=True)
    trades = self.trades.set_index('time')
    quotes = self.quotes.set_index(['time', 'bid'])
    with pytest.raises(MergeError):
        merge_asof(trades, quotes, left_index=True, right_index=True)