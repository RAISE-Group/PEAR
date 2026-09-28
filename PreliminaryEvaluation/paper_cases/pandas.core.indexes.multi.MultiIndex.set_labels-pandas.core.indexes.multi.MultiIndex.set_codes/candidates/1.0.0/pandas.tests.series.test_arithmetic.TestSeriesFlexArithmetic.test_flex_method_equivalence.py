@pytest.mark.parametrize('ts', [(lambda x: x, lambda x: x * 2, False), (lambda x: x, lambda x: x[::2], False), (lambda x: x, lambda x: 5, True), (lambda x: tm.makeFloatSeries(), lambda x: tm.makeFloatSeries(), True)])
@pytest.mark.parametrize('opname', ['add', 'sub', 'mul', 'floordiv', 'truediv', 'pow'])
def test_flex_method_equivalence(self, opname, ts):
    tser = tm.makeTimeSeries().rename('ts')
    series = ts[0](tser)
    other = ts[1](tser)
    check_reverse = ts[2]
    op = getattr(Series, opname)
    alt = getattr(operator, opname)
    result = op(series, other)
    expected = alt(series, other)
    tm.assert_almost_equal(result, expected)
    if check_reverse:
        rop = getattr(Series, 'r' + opname)
        result = rop(series, other)
        expected = alt(other, series)
        tm.assert_almost_equal(result, expected)