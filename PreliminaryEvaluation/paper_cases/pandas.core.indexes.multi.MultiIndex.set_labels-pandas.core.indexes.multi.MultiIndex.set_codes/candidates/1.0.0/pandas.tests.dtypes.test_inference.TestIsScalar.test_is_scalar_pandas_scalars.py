def test_is_scalar_pandas_scalars(self):
    assert is_scalar(Timestamp('2014-01-01'))
    assert is_scalar(Timedelta(hours=1))
    assert is_scalar(Period('2014-01-01'))
    assert is_scalar(Interval(left=0, right=1))
    assert is_scalar(DateOffset(days=1))