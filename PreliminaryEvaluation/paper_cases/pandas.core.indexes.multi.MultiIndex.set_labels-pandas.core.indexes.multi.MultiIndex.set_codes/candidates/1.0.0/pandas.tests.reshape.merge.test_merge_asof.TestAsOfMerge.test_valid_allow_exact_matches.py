def test_valid_allow_exact_matches(self):
    trades = self.trades
    quotes = self.quotes
    with pytest.raises(MergeError):
        merge_asof(trades, quotes, on='time', by='ticker', allow_exact_matches='foo')