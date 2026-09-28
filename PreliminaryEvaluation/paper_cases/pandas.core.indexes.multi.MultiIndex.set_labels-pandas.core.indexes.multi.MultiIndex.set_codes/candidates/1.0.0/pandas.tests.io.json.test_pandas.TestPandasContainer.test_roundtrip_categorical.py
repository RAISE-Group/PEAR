@pytest.mark.parametrize('convert_axes', [True, False])
@pytest.mark.parametrize('numpy', [True, False])
def test_roundtrip_categorical(self, orient, convert_axes, numpy):
    if orient in ('index', 'columns'):
        pytest.xfail(f"Can't have duplicate index values for orient '{orient}')")
    data = self.categorical.to_json(orient=orient)
    if numpy and orient in ('records', 'values'):
        pytest.xfail(f'Orient {orient} is broken with numpy=True')
    result = pd.read_json(data, orient=orient, convert_axes=convert_axes, numpy=numpy)
    expected = self.categorical.copy()
    expected.index = expected.index.astype(str)
    expected.index.name = None
    if not numpy and orient == 'index':
        expected = expected.sort_index()
    assert_json_roundtrip_equal(result, expected, orient)