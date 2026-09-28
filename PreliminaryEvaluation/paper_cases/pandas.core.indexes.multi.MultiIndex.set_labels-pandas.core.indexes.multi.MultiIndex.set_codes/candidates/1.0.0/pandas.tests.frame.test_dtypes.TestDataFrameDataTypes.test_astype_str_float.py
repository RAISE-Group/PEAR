def test_astype_str_float(self):
    result = DataFrame([np.NaN]).astype(str)
    expected = DataFrame(['nan'])
    tm.assert_frame_equal(result, expected)
    result = DataFrame([1.1234567890123457]).astype(str)
    val = '1.12345678901' if _np_version_under1p14 else '1.1234567890123457'
    expected = DataFrame([val])
    tm.assert_frame_equal(result, expected)