def test_to_timestamp_mult(self):
    p = Period('2011-01', freq='M')
    assert p.to_timestamp(how='S') == Timestamp('2011-01-01')
    expected = Timestamp('2011-02-01') - Timedelta(1, 'ns')
    assert p.to_timestamp(how='E') == expected
    p = Period('2011-01', freq='3M')
    assert p.to_timestamp(how='S') == Timestamp('2011-01-01')
    expected = Timestamp('2011-04-01') - Timedelta(1, 'ns')
    assert p.to_timestamp(how='E') == expected