def test_valid_tolerance(self):
    trades = self.trades
    quotes = self.quotes
    merge_asof(trades, quotes, on='time', by='ticker', tolerance=Timedelta('1s'))
    merge_asof(trades.reset_index(), quotes.reset_index(), on='index', by='ticker', tolerance=1)
    with pytest.raises(MergeError):
        merge_asof(trades, quotes, on='time', by='ticker', tolerance=1)
    with pytest.raises(MergeError):
        merge_asof(trades.reset_index(), quotes.reset_index(), on='index', by='ticker', tolerance=1.0)
    with pytest.raises(MergeError):
        merge_asof(trades, quotes, on='time', by='ticker', tolerance=-Timedelta('1s'))
    with pytest.raises(MergeError):
        merge_asof(trades.reset_index(), quotes.reset_index(), on='index', by='ticker', tolerance=-1)