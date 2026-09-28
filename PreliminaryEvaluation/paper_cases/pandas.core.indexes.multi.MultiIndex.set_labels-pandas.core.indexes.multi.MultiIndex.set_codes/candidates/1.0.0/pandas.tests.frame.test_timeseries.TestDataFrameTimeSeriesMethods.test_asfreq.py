def test_asfreq(self, datetime_frame):
    offset_monthly = datetime_frame.asfreq(offsets.BMonthEnd())
    rule_monthly = datetime_frame.asfreq('BM')
    tm.assert_almost_equal(offset_monthly['A'], rule_monthly['A'])
    filled = rule_monthly.asfreq('B', method='pad')
    filled_dep = rule_monthly.asfreq('B', method='pad')
    zero_length = datetime_frame.reindex([])
    result = zero_length.asfreq('BM')
    assert result is not zero_length