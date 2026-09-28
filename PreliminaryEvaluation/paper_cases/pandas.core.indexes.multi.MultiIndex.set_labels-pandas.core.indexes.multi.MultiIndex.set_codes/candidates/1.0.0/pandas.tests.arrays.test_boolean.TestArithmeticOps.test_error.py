def test_error(self, data, all_arithmetic_operators):
    op = all_arithmetic_operators
    s = pd.Series(data)
    ops = getattr(s, op)
    opa = getattr(data, op)
    with pytest.raises(TypeError):
        ops('foo')
    with pytest.raises(TypeError):
        ops(pd.Timestamp('20180101'))
    if op not in ('__mul__', '__rmul__'):
        with pytest.raises(TypeError):
            ops(pd.Series('foo', index=s.index))
    result = opa(pd.DataFrame({'A': s}))
    assert result is NotImplemented
    with pytest.raises(NotImplementedError):
        opa(np.arange(len(s)).reshape(-1, len(s)))