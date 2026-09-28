def test_apply_corner(self):
    msg = 'Only know how to combine trading day with datetime, datetime64 or timedelta'
    with pytest.raises(ApplyTypeError, match=msg):
        CDay().apply(BMonthEnd())