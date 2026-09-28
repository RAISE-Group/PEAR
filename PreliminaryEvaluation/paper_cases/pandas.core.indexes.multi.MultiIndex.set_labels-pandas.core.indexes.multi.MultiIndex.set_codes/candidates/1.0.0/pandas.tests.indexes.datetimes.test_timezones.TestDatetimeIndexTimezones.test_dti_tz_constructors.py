@pytest.mark.parametrize('tzstr', ['US/Eastern', 'dateutil/US/Eastern'])
def test_dti_tz_constructors(self, tzstr):
    """ Test different DatetimeIndex constructions with timezone
        Follow-up of GH#4229
        """
    arr = ['11/10/2005 08:00:00', '11/10/2005 09:00:00']
    idx1 = to_datetime(arr).tz_localize(tzstr)
    idx2 = pd.date_range(start='2005-11-10 08:00:00', freq='H', periods=2, tz=tzstr)
    idx3 = DatetimeIndex(arr, tz=tzstr)
    idx4 = DatetimeIndex(np.array(arr), tz=tzstr)
    for other in [idx2, idx3, idx4]:
        tm.assert_index_equal(idx1, other)