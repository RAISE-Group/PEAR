def test_get_loc2(self):
    idx = pd.period_range('2000-01-01', periods=3)
    for method in [None, 'pad', 'backfill', 'nearest']:
        assert idx.get_loc(idx[1], method) == 1
        assert idx.get_loc(idx[1].asfreq('H', how='start'), method) == 1
        assert idx.get_loc(idx[1].to_timestamp(), method) == 1
        assert idx.get_loc(idx[1].to_timestamp().to_pydatetime(), method) == 1
        assert idx.get_loc(str(idx[1]), method) == 1
    idx = pd.period_range('2000-01-01', periods=5)[::2]
    assert idx.get_loc('2000-01-02T12', method='nearest', tolerance='1 day') == 1
    assert idx.get_loc('2000-01-02T12', method='nearest', tolerance=pd.Timedelta('1D')) == 1
    assert idx.get_loc('2000-01-02T12', method='nearest', tolerance=np.timedelta64(1, 'D')) == 1
    assert idx.get_loc('2000-01-02T12', method='nearest', tolerance=timedelta(1)) == 1
    msg = 'unit abbreviation w/o a number'
    with pytest.raises(ValueError, match=msg):
        idx.get_loc('2000-01-10', method='nearest', tolerance='foo')
    msg = 'Input has different freq=None from PeriodArray\\(freq=D\\)'
    with pytest.raises(ValueError, match=msg):
        idx.get_loc('2000-01-10', method='nearest', tolerance='1 hour')
    with pytest.raises(KeyError, match="^Period\\('2000-01-10', 'D'\\)$"):
        idx.get_loc('2000-01-10', method='nearest', tolerance='1 day')
    with pytest.raises(ValueError, match='list-like tolerance size must match target index size'):
        idx.get_loc('2000-01-10', method='nearest', tolerance=[pd.Timedelta('1 day').to_timedelta64(), pd.Timedelta('1 day').to_timedelta64()])