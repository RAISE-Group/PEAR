@pytest.mark.parametrize('freq', ['D', 'M', 'A'])
def test_pickle_round_trip(self, freq):
    idx = PeriodIndex(['2016-05-16', 'NaT', NaT, np.NaN], freq=freq)
    result = tm.round_trip_pickle(idx)
    tm.assert_index_equal(result, idx)