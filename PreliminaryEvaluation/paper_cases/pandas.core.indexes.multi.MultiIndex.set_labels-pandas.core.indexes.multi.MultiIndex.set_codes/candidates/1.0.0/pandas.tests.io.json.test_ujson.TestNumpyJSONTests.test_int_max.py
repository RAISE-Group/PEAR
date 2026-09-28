def test_int_max(self, any_int_dtype):
    if any_int_dtype in ('int64', 'uint64') and compat.is_platform_32bit():
        pytest.skip('Cannot test 64-bit integer on 32-bit platform')
    klass = np.dtype(any_int_dtype).type
    if any_int_dtype == 'uint64':
        num = np.iinfo('int64').max
    else:
        num = np.iinfo(any_int_dtype).max
    assert klass(ujson.decode(ujson.encode(num))) == num