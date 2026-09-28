def test_method_on_bytes(self):
    lhs = Series(np.array(list('abc'), 'S1').astype(object))
    rhs = Series(np.array(list('def'), 'S1').astype(object))
    with pytest.raises(TypeError, match='Cannot use .str.cat with values of.*'):
        lhs.str.cat(rhs)