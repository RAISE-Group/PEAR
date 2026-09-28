@pytest.mark.parametrize('dtype', [None, object])
def test_numarr_with_dtype_add_nan(self, dtype, box_with_array):
    box = box_with_array
    ser = pd.Series([1, 2, 3], dtype=dtype)
    expected = pd.Series([np.nan, np.nan, np.nan], dtype=dtype)
    ser = tm.box_expected(ser, box)
    expected = tm.box_expected(expected, box)
    result = np.nan + ser
    tm.assert_equal(result, expected)
    result = ser + np.nan
    tm.assert_equal(result, expected)