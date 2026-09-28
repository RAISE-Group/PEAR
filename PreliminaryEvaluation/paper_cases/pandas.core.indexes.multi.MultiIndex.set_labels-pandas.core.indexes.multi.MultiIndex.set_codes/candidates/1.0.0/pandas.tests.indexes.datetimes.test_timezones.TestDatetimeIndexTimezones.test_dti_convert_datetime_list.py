@pytest.mark.parametrize('tzstr', ['US/Eastern', 'dateutil/US/Eastern'])
def test_dti_convert_datetime_list(self, tzstr):
    dr = date_range('2012-06-02', periods=10, tz=tzstr, name='foo')
    dr2 = DatetimeIndex(list(dr), name='foo')
    tm.assert_index_equal(dr, dr2)
    assert dr.tz == dr2.tz
    assert dr2.name == 'foo'