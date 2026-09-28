def test_to_datetime_bijective(self):
    exp_warning = None if Timestamp.max.nanosecond == 0 else UserWarning
    with tm.assert_produces_warning(exp_warning, check_stacklevel=False):
        assert Timestamp(Timestamp.max.to_pydatetime()).value / 1000 == Timestamp.max.value / 1000
    exp_warning = None if Timestamp.min.nanosecond == 0 else UserWarning
    with tm.assert_produces_warning(exp_warning, check_stacklevel=False):
        assert Timestamp(Timestamp.min.to_pydatetime()).value / 1000 == Timestamp.min.value / 1000