def test_get_loc(self):
    idx = pd.to_timedelta(['0 days', '1 days', '2 days'])
    for method in [None, 'pad', 'backfill', 'nearest']:
        assert idx.get_loc(idx[1], method) == 1
        assert idx.get_loc(idx[1].to_pytimedelta(), method) == 1
        assert idx.get_loc(str(idx[1]), method) == 1
    assert idx.get_loc(idx[1], 'pad', tolerance=Timedelta(0)) == 1
    assert idx.get_loc(idx[1], 'pad', tolerance=np.timedelta64(0, 's')) == 1
    assert idx.get_loc(idx[1], 'pad', tolerance=timedelta(0)) == 1
    with pytest.raises(ValueError, match='unit abbreviation w/o a number'):
        idx.get_loc(idx[1], method='nearest', tolerance='foo')
    with pytest.raises(ValueError, match='tolerance size must match'):
        idx.get_loc(idx[1], method='nearest', tolerance=[Timedelta(0).to_timedelta64(), Timedelta(0).to_timedelta64()])
    for method, loc in [('pad', 1), ('backfill', 2), ('nearest', 1)]:
        assert idx.get_loc('1 day 1 hour', method) == loc
    assert idx.get_loc(idx[1].to_timedelta64()) == 1
    assert idx.get_loc('0 days') == 0