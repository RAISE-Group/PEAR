@pytest.mark.parametrize('tolerance', [Timedelta('1day'), datetime.timedelta(days=1)], ids=['pd.Timedelta', 'datetime.timedelta'])
def test_tolerance(self, tolerance):
    trades = self.trades
    quotes = self.quotes
    result = merge_asof(trades, quotes, on='time', by='ticker', tolerance=tolerance)
    expected = self.tolerance
    tm.assert_frame_equal(result, expected)