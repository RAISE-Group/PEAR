@pytest.mark.parametrize('convert_axes', [True, False])
@pytest.mark.parametrize('numpy', [True, False])
def test_roundtrip_mixed(self, orient, convert_axes, numpy):
    if numpy and orient != 'split':
        pytest.xfail("Can't decode directly to array")
    index = pd.Index(['a', 'b', 'c', 'd', 'e'])
    values = {'A': [0.0, 1.0, 2.0, 3.0, 4.0], 'B': [0.0, 1.0, 0.0, 1.0, 0.0], 'C': ['foo1', 'foo2', 'foo3', 'foo4', 'foo5'], 'D': [True, False, True, False, True]}
    df = DataFrame(data=values, index=index)
    data = df.to_json(orient=orient)
    result = pd.read_json(data, orient=orient, convert_axes=convert_axes, numpy=numpy)
    expected = df.copy()
    expected = expected.assign(**expected.select_dtypes('number').astype(np.int64))
    if not numpy and orient == 'index':
        expected = expected.sort_index()
    assert_json_roundtrip_equal(result, expected, orient)