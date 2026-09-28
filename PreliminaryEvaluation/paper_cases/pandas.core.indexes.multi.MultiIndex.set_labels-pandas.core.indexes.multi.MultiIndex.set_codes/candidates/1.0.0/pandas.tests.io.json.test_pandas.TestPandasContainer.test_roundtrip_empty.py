@pytest.mark.parametrize('convert_axes', [True, False])
@pytest.mark.parametrize('numpy', [True, False])
def test_roundtrip_empty(self, orient, convert_axes, numpy):
    data = self.empty_frame.to_json(orient=orient)
    result = pd.read_json(data, orient=orient, convert_axes=convert_axes, numpy=numpy)
    expected = self.empty_frame.copy()
    if convert_axes:
        expected.index = expected.index.astype(float)
        expected.columns = expected.columns.astype(float)
    if numpy and orient == 'values':
        expected = expected.reindex([0], axis=1).reset_index(drop=True)
    tm.assert_frame_equal(result, expected)