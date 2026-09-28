def test_non_sorted(self):
    trades = self.trades.sort_values('time', ascending=False)
    quotes = self.quotes.sort_values('time', ascending=False)
    assert not trades.time.is_monotonic
    assert not quotes.time.is_monotonic
    with pytest.raises(ValueError):
        merge_asof(trades, quotes, on='time', by='ticker')
    trades = self.trades.sort_values('time')
    assert trades.time.is_monotonic
    assert not quotes.time.is_monotonic
    with pytest.raises(ValueError):
        merge_asof(trades, quotes, on='time', by='ticker')
    quotes = self.quotes.sort_values('time')
    assert trades.time.is_monotonic
    assert quotes.time.is_monotonic
    merge_asof(trades, self.quotes, on='time', by='ticker')