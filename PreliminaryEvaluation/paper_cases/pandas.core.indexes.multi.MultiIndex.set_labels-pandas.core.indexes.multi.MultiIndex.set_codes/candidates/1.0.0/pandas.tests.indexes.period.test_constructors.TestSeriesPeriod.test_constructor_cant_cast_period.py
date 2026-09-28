def test_constructor_cant_cast_period(self):
    msg = 'Cannot cast PeriodArray to dtype float64'
    with pytest.raises(TypeError, match=msg):
        Series(period_range('2000-01-01', periods=10, freq='D'), dtype=float)