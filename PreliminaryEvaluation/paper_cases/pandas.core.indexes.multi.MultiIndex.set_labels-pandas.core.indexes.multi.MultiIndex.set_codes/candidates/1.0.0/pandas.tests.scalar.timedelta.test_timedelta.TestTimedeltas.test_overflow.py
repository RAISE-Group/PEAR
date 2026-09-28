def test_overflow(self):
    s = Series(pd.date_range('20130101', periods=100000, freq='H'))
    s[0] += Timedelta('1s 1ms')
    result = (s - s.min()).mean()
    expected = Timedelta((TimedeltaIndex(s - s.min()).asi8 / len(s)).sum())
    assert np.allclose(result.value / 1000, expected.value / 1000)
    msg = 'overflow in timedelta operation'
    with pytest.raises(ValueError, match=msg):
        (s - s.min()).sum()
    s1 = s[0:10000]
    with pytest.raises(ValueError, match=msg):
        (s1 - s1.min()).sum()
    s2 = s[0:1000]
    result = (s2 - s2.min()).sum()