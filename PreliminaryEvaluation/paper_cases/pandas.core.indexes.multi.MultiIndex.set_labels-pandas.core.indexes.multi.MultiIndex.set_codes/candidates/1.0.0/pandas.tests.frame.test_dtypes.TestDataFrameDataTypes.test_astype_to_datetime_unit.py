@pytest.mark.parametrize('unit', ['ns', 'us', 'ms', 's', 'h', 'm', 'D'])
def test_astype_to_datetime_unit(self, unit):
    dtype = 'M8[{}]'.format(unit)
    arr = np.array([[1, 2, 3]], dtype=dtype)
    df = DataFrame(arr)
    result = df.astype(dtype)
    expected = DataFrame(arr.astype(dtype))
    tm.assert_frame_equal(result, expected)