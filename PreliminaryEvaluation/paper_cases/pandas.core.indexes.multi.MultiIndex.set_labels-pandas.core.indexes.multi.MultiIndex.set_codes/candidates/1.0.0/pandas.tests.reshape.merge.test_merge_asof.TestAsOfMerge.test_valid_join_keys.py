def test_valid_join_keys(self):
    trades = self.trades
    quotes = self.quotes
    with pytest.raises(MergeError):
        merge_asof(trades, quotes, left_on='time', right_on='bid', by='ticker')
    with pytest.raises(MergeError):
        merge_asof(trades, quotes, on=['time', 'ticker'], by='ticker')
    with pytest.raises(MergeError):
        merge_asof(trades, quotes, by='ticker')