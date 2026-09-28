def test_sub_offset_nat(self):
    for freq in ['A', '2A', '3A']:
        p = Period('NaT', freq=freq)
        assert p is NaT
        for o in [offsets.YearEnd(2)]:
            assert p - o is NaT
        for o in [offsets.YearBegin(2), offsets.MonthBegin(1), offsets.Minute(), np.timedelta64(365, 'D'), timedelta(365)]:
            assert p - o is NaT
    for freq in ['M', '2M', '3M']:
        p = Period('NaT', freq=freq)
        assert p is NaT
        for o in [offsets.MonthEnd(2), offsets.MonthEnd(12)]:
            assert p - o is NaT
        for o in [offsets.YearBegin(2), offsets.MonthBegin(1), offsets.Minute(), np.timedelta64(365, 'D'), timedelta(365)]:
            assert p - o is NaT
    for freq in ['D', '2D', '3D']:
        p = Period('NaT', freq=freq)
        assert p is NaT
        for o in [offsets.Day(5), offsets.Hour(24), np.timedelta64(2, 'D'), np.timedelta64(3600 * 24, 's'), timedelta(-2), timedelta(hours=48)]:
            assert p - o is NaT
        for o in [offsets.YearBegin(2), offsets.MonthBegin(1), offsets.Minute(), np.timedelta64(4, 'h'), timedelta(hours=23)]:
            assert p - o is NaT
    for freq in ['H', '2H', '3H']:
        p = Period('NaT', freq=freq)
        assert p is NaT
        for o in [offsets.Day(2), offsets.Hour(3), np.timedelta64(3, 'h'), np.timedelta64(3600, 's'), timedelta(minutes=120), timedelta(days=4, minutes=180)]:
            assert p - o is NaT
        for o in [offsets.YearBegin(2), offsets.MonthBegin(1), offsets.Minute(), np.timedelta64(3200, 's'), timedelta(hours=23, minutes=30)]:
            assert p - o is NaT