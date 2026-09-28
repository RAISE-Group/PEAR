@pytest.mark.parametrize('dtype', [False, np.int64])
@pytest.mark.parametrize('convert_axes', [True, False])
@pytest.mark.parametrize('numpy', [True, False])
def test_roundtrip_intframe(self, orient, convert_axes, numpy, dtype):
    data = self.intframe.to_json(orient=orient)
    result = pd.read_json(data, orient=orient, convert_axes=convert_axes, numpy=numpy, dtype=dtype)
    expected = self.intframe.copy()
    if numpy and (is_platform_32bit() or is_platform_windows()) and (not dtype) and (orient != 'split'):
        expected = expected.astype(np.int32)
    assert_json_roundtrip_equal(result, expected, orient)