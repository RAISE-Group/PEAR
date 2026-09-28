@pytest.mark.parametrize('prefix', ['', 'dateutil/'])
def test_field_access_localize(self, prefix):
    strdates = ['1/1/2012', '3/1/2012', '4/1/2012']
    rng = DatetimeIndex(strdates, tz=prefix + 'US/Eastern')
    assert (rng.hour == 0).all()
    dr = date_range('2011-10-02 00:00', freq='h', periods=10, tz=prefix + 'America/Atikokan')
    expected = Index(np.arange(10, dtype=np.int64))
    tm.assert_index_equal(dr.hour, expected)