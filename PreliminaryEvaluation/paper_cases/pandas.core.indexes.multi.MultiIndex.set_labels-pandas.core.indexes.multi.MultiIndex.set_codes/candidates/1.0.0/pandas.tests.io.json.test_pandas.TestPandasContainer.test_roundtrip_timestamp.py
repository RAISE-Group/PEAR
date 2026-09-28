@pytest.mark.parametrize('convert_axes', [True, False])
@pytest.mark.parametrize('numpy', [True, False])
def test_roundtrip_timestamp(self, orient, convert_axes, numpy):
    data = self.tsframe.to_json(orient=orient)
    result = pd.read_json(data, orient=orient, convert_axes=convert_axes, numpy=numpy)
    expected = self.tsframe.copy()
    if not convert_axes:
        idx = expected.index.astype(np.int64) // 1000000
        if orient != 'split':
            idx = idx.astype(str)
        expected.index = idx
    assert_json_roundtrip_equal(result, expected, orient)