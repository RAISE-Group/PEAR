def test_lookup_raises(self, float_frame):
    with pytest.raises(KeyError, match="'One or more row labels was not found'"):
        float_frame.lookup(['xyz'], ['A'])
    with pytest.raises(KeyError, match="'One or more column labels was not found'"):
        float_frame.lookup([float_frame.index[0]], ['xyz'])
    with pytest.raises(ValueError, match='same size'):
        float_frame.lookup(['a', 'b', 'c'], ['a'])