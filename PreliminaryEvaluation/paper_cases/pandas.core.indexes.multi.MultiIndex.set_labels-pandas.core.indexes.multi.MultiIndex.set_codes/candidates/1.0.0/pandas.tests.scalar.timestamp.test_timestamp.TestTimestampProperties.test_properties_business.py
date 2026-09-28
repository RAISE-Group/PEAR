def test_properties_business(self):
    ts = Timestamp('2017-10-01', freq='B')
    control = Timestamp('2017-10-01')
    assert ts.dayofweek == 6
    assert not ts.is_month_start
    assert not ts.is_quarter_start
    assert control.is_month_start
    assert control.is_quarter_start
    ts = Timestamp('2017-09-30', freq='B')
    control = Timestamp('2017-09-30')
    assert ts.dayofweek == 5
    assert not ts.is_month_end
    assert not ts.is_quarter_end
    assert control.is_month_end
    assert control.is_quarter_end