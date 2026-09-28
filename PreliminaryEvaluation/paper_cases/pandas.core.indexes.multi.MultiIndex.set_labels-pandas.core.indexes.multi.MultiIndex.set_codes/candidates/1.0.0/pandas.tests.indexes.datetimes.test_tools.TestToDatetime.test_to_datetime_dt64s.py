@pytest.mark.parametrize('cache', [True, False])
def test_to_datetime_dt64s(self, cache):
    in_bound_dts = [np.datetime64('2000-01-01'), np.datetime64('2000-01-02')]
    for dt in in_bound_dts:
        assert pd.to_datetime(dt, cache=cache) == Timestamp(dt)