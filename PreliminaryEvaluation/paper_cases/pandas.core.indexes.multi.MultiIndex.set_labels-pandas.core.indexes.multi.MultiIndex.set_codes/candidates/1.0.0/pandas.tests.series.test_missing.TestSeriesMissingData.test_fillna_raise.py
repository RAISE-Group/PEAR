def test_fillna_raise(self):
    s = Series(np.random.randint(-100, 100, 50))
    msg = '"value" parameter must be a scalar or dict, but you passed a "list"'
    with pytest.raises(TypeError, match=msg):
        s.fillna([1, 2])
    msg = '"value" parameter must be a scalar or dict, but you passed a "tuple"'
    with pytest.raises(TypeError, match=msg):
        s.fillna((1, 2))
    s = Series([1, 2, 3, None])
    msg = "Cannot specify both 'value' and 'method'\\.|Limit must be greater than 0|Limit must be an integer"
    for limit in [-1, 0, 1.0, 2.0]:
        for method in ['backfill', 'bfill', 'pad', 'ffill', None]:
            with pytest.raises(ValueError, match=msg):
                s.fillna(1, limit=limit, method=method)