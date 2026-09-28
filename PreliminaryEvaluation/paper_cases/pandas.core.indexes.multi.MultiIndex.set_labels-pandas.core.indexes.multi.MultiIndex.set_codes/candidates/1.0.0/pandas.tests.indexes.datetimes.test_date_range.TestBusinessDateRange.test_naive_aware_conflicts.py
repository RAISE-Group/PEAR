def test_naive_aware_conflicts(self):
    naive = bdate_range(START, END, freq=BDay(), tz=None)
    aware = bdate_range(START, END, freq=BDay(), tz='Asia/Hong_Kong')
    msg = 'tz-naive.*tz-aware'
    with pytest.raises(TypeError, match=msg):
        naive.join(aware)
    with pytest.raises(TypeError, match=msg):
        aware.join(naive)