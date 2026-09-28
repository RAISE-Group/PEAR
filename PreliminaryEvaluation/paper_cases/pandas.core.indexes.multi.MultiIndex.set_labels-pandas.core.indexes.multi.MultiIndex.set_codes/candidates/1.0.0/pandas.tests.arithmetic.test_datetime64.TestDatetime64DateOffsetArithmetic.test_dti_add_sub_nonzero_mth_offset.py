@pytest.mark.parametrize('op, offset, exp, exp_freq', [('__add__', pd.DateOffset(months=3, days=10), [Timestamp('2014-04-11'), Timestamp('2015-04-11'), Timestamp('2016-04-11'), Timestamp('2017-04-11')], None), ('__add__', pd.DateOffset(months=3), [Timestamp('2014-04-01'), Timestamp('2015-04-01'), Timestamp('2016-04-01'), Timestamp('2017-04-01')], 'AS-APR'), ('__sub__', pd.DateOffset(months=3, days=10), [Timestamp('2013-09-21'), Timestamp('2014-09-21'), Timestamp('2015-09-21'), Timestamp('2016-09-21')], None), ('__sub__', pd.DateOffset(months=3), [Timestamp('2013-10-01'), Timestamp('2014-10-01'), Timestamp('2015-10-01'), Timestamp('2016-10-01')], 'AS-OCT')])
def test_dti_add_sub_nonzero_mth_offset(self, op, offset, exp, exp_freq, tz_aware_fixture, box_with_array):
    tz = tz_aware_fixture
    date = date_range(start='01 Jan 2014', end='01 Jan 2017', freq='AS', tz=tz)
    date = tm.box_expected(date, box_with_array, False)
    mth = getattr(date, op)
    result = mth(offset)
    expected = pd.DatetimeIndex(exp, tz=tz, freq=exp_freq)
    expected = tm.box_expected(expected, box_with_array, False)
    tm.assert_equal(result, expected)