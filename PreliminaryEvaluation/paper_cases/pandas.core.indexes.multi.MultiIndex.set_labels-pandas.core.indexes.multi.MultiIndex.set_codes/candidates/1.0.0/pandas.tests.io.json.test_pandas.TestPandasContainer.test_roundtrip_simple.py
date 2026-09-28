@pytest.mark.parametrize('dtype', [False, float])
@pytest.mark.parametrize('convert_axes', [True, False])
@pytest.mark.parametrize('numpy', [True, False])
def test_roundtrip_simple(self, orient, convert_axes, numpy, dtype):
    data = self.frame.to_json(orient=orient)
    result = pd.read_json(data, orient=orient, convert_axes=convert_axes, numpy=numpy, dtype=dtype)
    expected = self.frame.copy()
    assert_json_roundtrip_equal(result, expected, orient)