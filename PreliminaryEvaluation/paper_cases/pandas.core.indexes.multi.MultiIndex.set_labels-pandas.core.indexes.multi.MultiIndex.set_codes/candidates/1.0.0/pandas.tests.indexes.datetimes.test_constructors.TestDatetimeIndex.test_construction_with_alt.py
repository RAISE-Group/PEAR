@pytest.mark.parametrize('kwargs', [{'tz': 'dtype.tz'}, {'dtype': 'dtype'}, {'dtype': 'dtype', 'tz': 'dtype.tz'}])
def test_construction_with_alt(self, kwargs, tz_aware_fixture):
    tz = tz_aware_fixture
    i = pd.date_range('20130101', periods=5, freq='H', tz=tz)
    kwargs = {key: attrgetter(val)(i) for key, val in kwargs.items()}
    result = DatetimeIndex(i, **kwargs)
    tm.assert_index_equal(i, result)