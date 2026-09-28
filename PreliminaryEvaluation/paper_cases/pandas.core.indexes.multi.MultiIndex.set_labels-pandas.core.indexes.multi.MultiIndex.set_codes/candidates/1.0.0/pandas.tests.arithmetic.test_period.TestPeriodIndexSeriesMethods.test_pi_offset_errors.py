def test_pi_offset_errors(self):
    idx = PeriodIndex(['2011-01-01', '2011-02-01', '2011-03-01', '2011-04-01'], freq='D', name='idx')
    ser = pd.Series(idx)
    for obj in [idx, ser]:
        msg = 'Input has different freq=2H from Period.*?\\(freq=D\\)'
        with pytest.raises(IncompatibleFrequency, match=msg):
            obj + pd.offsets.Hour(2)
        with pytest.raises(IncompatibleFrequency, match=msg):
            pd.offsets.Hour(2) + obj
        msg = 'Input has different freq=-2H from Period.*?\\(freq=D\\)'
        with pytest.raises(IncompatibleFrequency, match=msg):
            obj - pd.offsets.Hour(2)