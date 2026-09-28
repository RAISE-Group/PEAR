def test_contains_with_float_index(self):
    integer_index = pd.Int64Index([0, 1, 2, 3])
    uinteger_index = pd.UInt64Index([0, 1, 2, 3])
    float_index = pd.Float64Index([0.1, 1.1, 2.2, 3.3])
    for index in (integer_index, uinteger_index):
        assert 1.1 not in index
        assert 1.0 in index
        assert 1 in index
    assert 1.1 in float_index
    assert 1.0 not in float_index
    assert 1 not in float_index