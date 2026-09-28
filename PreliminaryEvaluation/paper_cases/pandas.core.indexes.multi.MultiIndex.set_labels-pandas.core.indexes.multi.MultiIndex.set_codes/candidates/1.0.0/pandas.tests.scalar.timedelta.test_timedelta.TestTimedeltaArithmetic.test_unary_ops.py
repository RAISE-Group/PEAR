def test_unary_ops(self):
    td = Timedelta(10, unit='d')
    assert -td == Timedelta(-10, unit='d')
    assert -td == Timedelta('-10d')
    assert +td == Timedelta(10, unit='d')
    assert abs(td) == td
    assert abs(-td) == td
    assert abs(-td) == Timedelta('10d')