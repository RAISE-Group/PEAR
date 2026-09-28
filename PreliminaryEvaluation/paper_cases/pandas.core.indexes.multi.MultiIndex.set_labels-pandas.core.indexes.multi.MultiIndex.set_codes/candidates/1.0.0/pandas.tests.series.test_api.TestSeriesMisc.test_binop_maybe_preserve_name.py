def test_binop_maybe_preserve_name(self, datetime_series):
    result = datetime_series * datetime_series
    assert result.name == datetime_series.name
    result = datetime_series.mul(datetime_series)
    assert result.name == datetime_series.name
    result = datetime_series * datetime_series[:-2]
    assert result.name == datetime_series.name
    cp = datetime_series.copy()
    cp.name = 'something else'
    result = datetime_series + cp
    assert result.name is None
    result = datetime_series.add(cp)
    assert result.name is None
    ops = ['add', 'sub', 'mul', 'div', 'truediv', 'floordiv', 'mod', 'pow']
    ops = ops + ['r' + op for op in ops]
    for op in ops:
        s = datetime_series.copy()
        result = getattr(s, op)(s)
        assert result.name == datetime_series.name
        cp = datetime_series.copy()
        cp.name = 'changed'
        result = getattr(s, op)(cp)
        assert result.name is None