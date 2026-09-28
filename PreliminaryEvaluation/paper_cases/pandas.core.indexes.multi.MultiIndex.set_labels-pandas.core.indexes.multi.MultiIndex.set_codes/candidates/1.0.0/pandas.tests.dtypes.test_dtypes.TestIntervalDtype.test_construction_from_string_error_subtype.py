@pytest.mark.parametrize('string', ['foo', 'foo[int64]', 'IntervalA'])
def test_construction_from_string_error_subtype(self, string):
    msg = 'Incorrectly formatted string passed to constructor. Valid formats include Interval or Interval\\[dtype\\] where dtype is numeric, datetime, or timedelta'
    with pytest.raises(TypeError, match=msg):
        IntervalDtype.construct_from_string(string)