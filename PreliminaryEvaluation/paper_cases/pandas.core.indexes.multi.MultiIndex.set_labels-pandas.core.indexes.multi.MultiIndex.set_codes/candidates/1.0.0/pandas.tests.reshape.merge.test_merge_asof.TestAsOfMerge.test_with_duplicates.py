def test_with_duplicates(self, datapath):
    q = pd.concat([self.quotes, self.quotes]).sort_values(['time', 'ticker']).reset_index(drop=True)
    result = merge_asof(self.trades, q, on='time', by='ticker')
    expected = self.read_data(datapath, 'asof.csv')
    tm.assert_frame_equal(result, expected)