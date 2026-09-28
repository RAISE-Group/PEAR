@pytest.mark.parametrize('unit', ['us', 'ms', 's', 'h', 'm', 'D'])
def test_astype_to_timedelta_unit(self, unit):
    dtype = 'm8[{}]'.format(unit)
    arr = np.array([[1, 2, 3]], dtype=dtype)
    df = DataFrame(arr)
    result = df.astype(dtype)
    expected = DataFrame(df.values.astype(dtype).astype(float))
    tm.assert_frame_equal(result, expected)