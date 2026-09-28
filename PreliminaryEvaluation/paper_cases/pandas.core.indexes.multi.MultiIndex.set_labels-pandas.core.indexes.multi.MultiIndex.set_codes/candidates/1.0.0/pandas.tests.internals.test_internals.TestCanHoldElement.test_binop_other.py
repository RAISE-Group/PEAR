@pytest.mark.parametrize('value, dtype', [(1, 'i8'), (1.0, 'f8'), (2 ** 63, 'f8'), (1j, 'complex128'), (2 ** 63, 'complex128'), (True, 'bool'), (np.timedelta64(20, 'ns'), '<m8[ns]'), (np.datetime64(20, 'ns'), '<M8[ns]')])
@pytest.mark.parametrize('op', [operator.add, operator.sub, operator.mul, operator.truediv, operator.mod, operator.pow], ids=lambda x: x.__name__)
def test_binop_other(self, op, value, dtype):
    skip = {(operator.add, 'bool'), (operator.sub, 'bool'), (operator.mul, 'bool'), (operator.truediv, 'bool'), (operator.mod, 'i8'), (operator.mod, 'complex128'), (operator.pow, 'bool')}
    if (op, dtype) in skip:
        pytest.skip('Invalid combination {},{}'.format(op, dtype))
    e = DummyElement(value, dtype)
    s = pd.DataFrame({'A': [e.value, e.value]}, dtype=e.dtype)
    invalid = {(operator.pow, '<M8[ns]'), (operator.mod, '<M8[ns]'), (operator.truediv, '<M8[ns]'), (operator.mul, '<M8[ns]'), (operator.add, '<M8[ns]'), (operator.pow, '<m8[ns]'), (operator.mul, '<m8[ns]')}
    if (op, dtype) in invalid:
        with pytest.raises(TypeError):
            op(s, e.value)
    else:
        result = op(s, e.value).dtypes
        expected = op(s, value).dtypes
        tm.assert_series_equal(result, expected)