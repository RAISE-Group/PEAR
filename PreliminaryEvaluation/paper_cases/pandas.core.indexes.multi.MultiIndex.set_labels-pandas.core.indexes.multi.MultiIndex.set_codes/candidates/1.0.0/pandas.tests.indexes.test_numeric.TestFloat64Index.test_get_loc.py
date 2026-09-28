def test_get_loc(self):
    idx = Float64Index([0.0, 1.0, 2.0])
    for method in [None, 'pad', 'backfill', 'nearest']:
        assert idx.get_loc(1, method) == 1
        if method is not None:
            assert idx.get_loc(1, method, tolerance=0) == 1
    for method, loc in [('pad', 1), ('backfill', 2), ('nearest', 1)]:
        assert idx.get_loc(1.1, method) == loc
        assert idx.get_loc(1.1, method, tolerance=0.9) == loc
    with pytest.raises(KeyError, match="^'foo'$"):
        idx.get_loc('foo')
    with pytest.raises(KeyError, match='^1\\.5$'):
        idx.get_loc(1.5)
    with pytest.raises(KeyError, match='^1\\.5$'):
        idx.get_loc(1.5, method='pad', tolerance=0.1)
    with pytest.raises(KeyError, match='^True$'):
        idx.get_loc(True)
    with pytest.raises(KeyError, match='^False$'):
        idx.get_loc(False)
    with pytest.raises(ValueError, match='must be numeric'):
        idx.get_loc(1.4, method='nearest', tolerance='foo')
    with pytest.raises(ValueError, match='must contain numeric elements'):
        idx.get_loc(1.4, method='nearest', tolerance=np.array(['foo']))
    with pytest.raises(ValueError, match='tolerance size must match target index size'):
        idx.get_loc(1.4, method='nearest', tolerance=np.array([1, 2]))