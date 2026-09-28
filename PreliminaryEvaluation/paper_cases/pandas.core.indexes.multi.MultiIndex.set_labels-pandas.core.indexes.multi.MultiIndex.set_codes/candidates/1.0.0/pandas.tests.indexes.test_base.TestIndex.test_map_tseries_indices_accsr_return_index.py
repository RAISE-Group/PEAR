def test_map_tseries_indices_accsr_return_index(self):
    date_index = tm.makeDateIndex(24, freq='h', name='hourly')
    expected = Index(range(24), name='hourly')
    tm.assert_index_equal(expected, date_index.map(lambda x: x.hour))