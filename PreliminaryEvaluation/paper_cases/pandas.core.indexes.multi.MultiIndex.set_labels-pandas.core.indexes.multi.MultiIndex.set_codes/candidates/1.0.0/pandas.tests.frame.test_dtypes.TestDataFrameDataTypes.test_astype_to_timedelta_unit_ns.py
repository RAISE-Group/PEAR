@pytest.mark.parametrize('unit', ['ns'])
def test_astype_to_timedelta_unit_ns(self, unit):
    dtype = 'm8[{}]'.format(unit)
    arr = np.array([[1, 2, 3]], dtype=dtype)
    df = DataFrame(arr)
    result = df.astype(dtype)
    expected = DataFrame(arr.astype(dtype))
    tm.assert_frame_equal(result, expected)