@pytest.mark.parametrize('tzstr', ['US/Eastern', 'dateutil/US/Eastern'])
def test_dti_tz_nat(self, tzstr):
    idx = DatetimeIndex([Timestamp('2013-1-1', tz=tzstr), pd.NaT])
    assert isna(idx[1])
    assert idx[0].tzinfo is not None