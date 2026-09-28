@pytest.mark.parametrize('idxer', ['var', ['var']])
def test_setitem_datetimeindex_tz(self, idxer, tz_naive_fixture):
    tz = tz_naive_fixture
    idx = date_range(start='2015-07-12', periods=3, freq='H', tz=tz)
    expected = DataFrame(1.2, index=idx, columns=['var'])
    result = DataFrame(index=idx, columns=['var'])
    result.loc[:, idxer] = expected
    tm.assert_frame_equal(result, expected)