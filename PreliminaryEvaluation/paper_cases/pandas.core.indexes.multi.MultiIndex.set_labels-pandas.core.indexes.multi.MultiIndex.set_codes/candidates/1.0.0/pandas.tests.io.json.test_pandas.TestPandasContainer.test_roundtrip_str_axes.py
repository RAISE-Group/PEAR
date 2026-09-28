@pytest.mark.parametrize('dtype', [None, np.float64, np.int, 'U3'])
@pytest.mark.parametrize('convert_axes', [True, False])
@pytest.mark.parametrize('numpy', [True, False])
def test_roundtrip_str_axes(self, orient, convert_axes, numpy, dtype):
    df = DataFrame(np.zeros((200, 4)), columns=[str(i) for i in range(4)], index=[str(i) for i in range(200)], dtype=dtype)
    if numpy and dtype == 'U3' and (orient != 'split'):
        pytest.xfail("Can't decode directly to array")
    data = df.to_json(orient=orient)
    result = pd.read_json(data, orient=orient, convert_axes=convert_axes, numpy=numpy, dtype=dtype)
    expected = df.copy()
    if not dtype:
        expected = expected.astype(np.int64)
    if convert_axes and orient in ('split', 'index', 'columns'):
        expected.columns = expected.columns.astype(np.int64)
        expected.index = expected.index.astype(np.int64)
    elif orient == 'records' and convert_axes:
        expected.columns = expected.columns.astype(np.int64)
    assert_json_roundtrip_equal(result, expected, orient)