@pytest.mark.parametrize('opname', ['eq', 'ne', 'gt', 'lt', 'ge', 'le'])
def test_ser_flex_cmp_return_dtypes_empty(self, opname):
    ser = Series([1, 3, 2], index=range(3))
    empty = ser.iloc[:0]
    const = 2
    result = getattr(empty, opname)(const).dtypes
    expected = np.dtype('bool')
    assert result == expected