def test_apply_corner(self):
    msg = 'Only know how to combine business day with datetime or timedelta'
    with pytest.raises(ApplyTypeError, match=msg):
        BDay().apply(BMonthEnd())