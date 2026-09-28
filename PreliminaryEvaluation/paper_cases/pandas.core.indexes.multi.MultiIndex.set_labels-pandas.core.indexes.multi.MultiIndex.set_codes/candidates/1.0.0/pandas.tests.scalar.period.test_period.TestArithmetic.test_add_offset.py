def test_add_offset(self):
    for freq in ['A', '2A', '3A']:
        p = Period('2011', freq=freq)
        exp = Period('2013', freq=freq)
        assert p + offsets.YearEnd(2) == exp
        assert offsets.YearEnd(2) + p == exp
        for o in [offsets.YearBegin(2), offsets.MonthBegin(1), offsets.Minute(), np.timedelta64(365, 'D'), timedelta(365)]:
            with pytest.raises(IncompatibleFrequency):
                p + o
            if isinstance(o, np.timedelta64):
                with pytest.raises(TypeError):
                    o + p
            else:
                with pytest.raises(IncompatibleFrequency):
                    o + p
    for freq in ['M', '2M', '3M']:
        p = Period('2011-03', freq=freq)
        exp = Period('2011-05', freq=freq)
        assert p + offsets.MonthEnd(2) == exp
        assert offsets.MonthEnd(2) + p == exp
        exp = Period('2012-03', freq=freq)
        assert p + offsets.MonthEnd(12) == exp
        assert offsets.MonthEnd(12) + p == exp
        for o in [offsets.YearBegin(2), offsets.MonthBegin(1), offsets.Minute(), np.timedelta64(365, 'D'), timedelta(365)]:
            with pytest.raises(IncompatibleFrequency):
                p + o
            if isinstance(o, np.timedelta64):
                with pytest.raises(TypeError):
                    o + p
            else:
                with pytest.raises(IncompatibleFrequency):
                    o + p
    for freq in ['D', '2D', '3D']:
        p = Period('2011-04-01', freq=freq)
        exp = Period('2011-04-06', freq=freq)
        assert p + offsets.Day(5) == exp
        assert offsets.Day(5) + p == exp
        exp = Period('2011-04-02', freq=freq)
        assert p + offsets.Hour(24) == exp
        assert offsets.Hour(24) + p == exp
        exp = Period('2011-04-03', freq=freq)
        assert p + np.timedelta64(2, 'D') == exp
        with pytest.raises(TypeError):
            np.timedelta64(2, 'D') + p
        exp = Period('2011-04-02', freq=freq)
        assert p + np.timedelta64(3600 * 24, 's') == exp
        with pytest.raises(TypeError):
            np.timedelta64(3600 * 24, 's') + p
        exp = Period('2011-03-30', freq=freq)
        assert p + timedelta(-2) == exp
        assert timedelta(-2) + p == exp
        exp = Period('2011-04-03', freq=freq)
        assert p + timedelta(hours=48) == exp
        assert timedelta(hours=48) + p == exp
        for o in [offsets.YearBegin(2), offsets.MonthBegin(1), offsets.Minute(), np.timedelta64(4, 'h'), timedelta(hours=23)]:
            with pytest.raises(IncompatibleFrequency):
                p + o
            if isinstance(o, np.timedelta64):
                with pytest.raises(TypeError):
                    o + p
            else:
                with pytest.raises(IncompatibleFrequency):
                    o + p
    for freq in ['H', '2H', '3H']:
        p = Period('2011-04-01 09:00', freq=freq)
        exp = Period('2011-04-03 09:00', freq=freq)
        assert p + offsets.Day(2) == exp
        assert offsets.Day(2) + p == exp
        exp = Period('2011-04-01 12:00', freq=freq)
        assert p + offsets.Hour(3) == exp
        assert offsets.Hour(3) + p == exp
        exp = Period('2011-04-01 12:00', freq=freq)
        assert p + np.timedelta64(3, 'h') == exp
        with pytest.raises(TypeError):
            np.timedelta64(3, 'h') + p
        exp = Period('2011-04-01 10:00', freq=freq)
        assert p + np.timedelta64(3600, 's') == exp
        with pytest.raises(TypeError):
            np.timedelta64(3600, 's') + p
        exp = Period('2011-04-01 11:00', freq=freq)
        assert p + timedelta(minutes=120) == exp
        assert timedelta(minutes=120) + p == exp
        exp = Period('2011-04-05 12:00', freq=freq)
        assert p + timedelta(days=4, minutes=180) == exp
        assert timedelta(days=4, minutes=180) + p == exp
        for o in [offsets.YearBegin(2), offsets.MonthBegin(1), offsets.Minute(), np.timedelta64(3200, 's'), timedelta(hours=23, minutes=30)]:
            with pytest.raises(IncompatibleFrequency):
                p + o
            if isinstance(o, np.timedelta64):
                with pytest.raises(TypeError):
                    o + p
            else:
                with pytest.raises(IncompatibleFrequency):
                    o + p