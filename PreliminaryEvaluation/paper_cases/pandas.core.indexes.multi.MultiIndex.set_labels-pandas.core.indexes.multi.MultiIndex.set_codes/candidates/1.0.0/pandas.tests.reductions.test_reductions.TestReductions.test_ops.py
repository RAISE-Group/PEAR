@pytest.mark.parametrize('opname', ['max', 'min'])
@pytest.mark.parametrize('obj', objs)
def test_ops(self, opname, obj):
    result = getattr(obj, opname)()
    if not isinstance(obj, PeriodIndex):
        expected = getattr(obj.values, opname)()
    else:
        expected = pd.Period(ordinal=getattr(obj._ndarray_values, opname)(), freq=obj.freq)
    try:
        assert result == expected
    except TypeError:
        expected = expected.astype('M8[ns]').astype('int64')
        assert result.value == expected