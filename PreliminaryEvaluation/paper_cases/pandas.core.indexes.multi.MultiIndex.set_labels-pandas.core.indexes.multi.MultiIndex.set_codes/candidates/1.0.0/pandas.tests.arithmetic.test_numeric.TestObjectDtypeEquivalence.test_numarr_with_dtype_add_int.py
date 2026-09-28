@pytest.mark.parametrize('dtype', [None, object])
def test_numarr_with_dtype_add_int(self, dtype, box_with_array):
    box = box_with_array
    ser = pd.Series([1, 2, 3], dtype=dtype)
    expected = pd.Series([2, 3, 4], dtype=dtype)
    ser = tm.box_expected(ser, box)
    expected = tm.box_expected(expected, box)
    result = 1 + ser
    tm.assert_equal(result, expected)
    result = ser + 1
    tm.assert_equal(result, expected)