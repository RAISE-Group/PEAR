@pytest.mark.parametrize('opname', ['eq', 'ne', 'gt', 'lt', 'ge', 'le'])
def test_ser_flex_cmp_return_dtypes(self, opname):
    ser = Series([1, 3, 2], index=range(3))
    const = 2
    result = getattr(ser, opname)(const).dtypes
    expected = np.dtype('bool')
    assert result == expected